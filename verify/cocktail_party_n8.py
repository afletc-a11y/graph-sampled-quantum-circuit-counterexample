#!/usr/bin/env python3
"""Exact supporting evidence for the n=8 cocktail-party graph.

This is deliberately not advertised as a general family theorem.  It uses the
exact heat-bath reduction already cross-checked against the permutation-basis
representation and checks only the finite n=8 claim.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

from exact_markov import _step_integer, stationary_probability, validate_graph

N = 8
K8 = list(combinations(range(N), 2))
MATCHING = {(i, i + N // 2) for i in range(N // 2)}
CP8 = [e for e in K8 if e not in MATCHING]

EXPECTED = {
    ("CP8", 6): F(293242219, 21600000),
    ("K8", 6): F(230164152993, 16807000000),
    ("CP8", 16): F(37222906637142989511155183, 65303470080000000000000000),
    ("K8", 16): F(4008961629021877754048110238049, 6945004265973760000000000000000),
    ("CP8", 17): F(6062032651990349691461374520233, 12853682015846400000000000000000),
    ("K8", 17): F(229123049355054299943024454340127, 486150298618163200000000000000000),
}


def curve(edges, smax=17):
    edges = validate_graph(N, edges)
    scale0 = 10 * len(edges)
    vals = [[] for _ in range(smax + 1)]
    for start in range(1 << N):
        vector = [0] * (1 << N)
        vector[start] = 1
        scale = 1
        pi = stationary_probability(N, start)
        for s in range(1, smax + 1):
            vector = _step_integer(N, edges, vector)
            scale *= scale0
            vals[s].append(F(vector[start], scale) / pi - 1)
    out = {}
    for s in range(1, smax + 1):
        best = max(vals[s])
        out[s] = (best, [a for a, value in enumerate(vals[s]) if value == best])
    return out


def main() -> None:
    cp = curve(CP8)
    k8 = curve(K8)
    hits = [s for s in range(1, 18) if cp[s][0] < k8[s][0]]
    assert hits == list(range(6, 17)), hits
    for (name, s), expected in EXPECTED.items():
        actual = cp[s][0] if name == "CP8" else k8[s][0]
        assert actual == expected, (name, s, actual, expected)
    assert cp[16][0] < k8[16][0]
    assert cp[17][0] > k8[17][0]
    print("PASS: CP8 beats K8 exactly at s=6,...,16 among s<=17")
    print(f"s=16: CP8={cp[16][0]} < K8={k8[16][0]}")
    print(f"s=17: CP8={cp[17][0]} > K8={k8[17][0]}")
    print("Evidence at n=8 only; no general family theorem is claimed.")


if __name__ == "__main__":
    main()
