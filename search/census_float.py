#!/usr/bin/env python3
"""Exploratory connected-unlabeled-graph census (not a proof checker).

Dependencies: numpy and networkx.  Exact reconstruction belongs in verify/.
"""

from __future__ import annotations

import networkx as nx
import numpy as np


def stationary(n: int) -> np.ndarray:
    return np.array(
        [
            3 ** (n - x.bit_count())
            / (2 ** (n - 1) * (2**n + (-1 if x.bit_count() & 1 else 1)))
            for x in range(1 << n)
        ]
    )


def kernel(graph: nx.Graph) -> np.ndarray:
    n = len(graph)
    size = 1 << n
    m = graph.number_of_edges()
    matrix = np.zeros((size, size))
    for x in range(size):
        for u, v in graph.edges():
            z = x & ~(1 << u) & ~(1 << v)
            if ((x >> u) ^ (x >> v)) & 1:
                matrix[x, z | (1 << u)] += 0.5 / m
                matrix[x, z | (1 << v)] += 0.5 / m
            else:
                matrix[x, z] += 0.9 / m
                matrix[x, z | (1 << u) | (1 << v)] += 0.1 / m
    return matrix


def curve(graph: nx.Graph, max_gates: int) -> np.ndarray:
    pi = stationary(len(graph))
    transition = kernel(graph)
    symmetric = np.sqrt(pi)[:, None] * transition / np.sqrt(pi)[None, :]
    eigenvalues, eigenvectors = np.linalg.eigh(symmetric)
    powers = eigenvalues[:, None] ** np.arange(max_gates + 1)[None, :]
    returns = (eigenvectors * eigenvectors) @ powers
    return np.max(returns / pi[:, None] - 1, axis=0)


def main() -> None:
    atlas = nx.graph_atlas_g()
    max_gates = 200
    for n in range(2, 8):
        graphs = [g for g in atlas if len(g) == n and nx.is_connected(g)]
        complete_curve = curve(nx.complete_graph(n), max_gates)
        violations = []
        for index, graph in enumerate(graphs):
            difference = curve(graph, max_gates) - complete_curve
            gate = int(np.argmin(difference[1:])) + 1
            if difference[gate] < -1e-8:
                violations.append(
                    {
                        "atlas_index_within_n": index,
                        "gate": gate,
                        "difference": float(difference[gate]),
                        "edges": sorted(graph.edges()),
                    }
                )
        print(f"n={n}: {len(graphs)} graphs, {len(violations)} candidates")
        for item in violations:
            print(item)


if __name__ == "__main__":
    main()
