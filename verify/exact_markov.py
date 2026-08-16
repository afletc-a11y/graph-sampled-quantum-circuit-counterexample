#!/usr/bin/env python3
"""Exact q=2, t=2 multiplicative error for graph-sampled Haar circuits.

This implementation uses the parity-conditioned heat-bath-chain reduction.
It depends only on Python's standard library.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def validate_graph(n: int, edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if n < 2:
        raise ValueError("n must be at least 2")
    normalized = sorted({tuple(sorted(edge)) for edge in edges})
    if len(normalized) != len(edges):
        raise ValueError("edges must be distinct")
    if any(u == v or u < 0 or v >= n for u, v in normalized):
        raise ValueError("invalid simple-graph edge")
    seen = {0}
    while True:
        grown = seen | {v for u, v in normalized if u in seen} | {
            u for u, v in normalized if v in seen
        }
        if grown == seen:
            break
        seen = grown
    if len(seen) != n:
        raise ValueError("graph must be connected")
    return normalized


def stationary_probability(n: int, state: int) -> Fraction:
    """Stationary mass in the parity class containing ``state``."""
    k = state.bit_count()
    sign = -1 if k & 1 else 1
    normalizer = 2 ** (n - 1) * (2**n + sign)
    return Fraction(3 ** (n - k), normalizer)


def _step_integer(
    n: int, edges: list[tuple[int, int]], vector: list[int]
) -> list[int]:
    """Multiply a row distribution by Q=(10|E|)K using integers."""
    out = [0] * (1 << n)
    for state, mass in enumerate(vector):
        if not mass:
            continue
        for u, v in edges:
            bu = (state >> u) & 1
            bv = (state >> v) & 1
            cleared = state & ~(1 << u) & ~(1 << v)
            if bu == bv:
                out[cleared] += 9 * mass
                out[cleared | (1 << u) | (1 << v)] += mass
            else:
                out[cleared | (1 << u)] += 5 * mass
                out[cleared | (1 << v)] += 5 * mass
    return out


def all_errors(n: int, edges: list[tuple[int, int]], steps: int) -> list[Fraction]:
    """Return exact relative-return errors for every experiment/state."""
    edges = validate_graph(n, edges)
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    scale = (10 * len(edges)) ** steps
    errors: list[Fraction] = []
    for start in range(1 << n):
        vector = [0] * (1 << n)
        vector[start] = 1
        for _ in range(steps):
            vector = _step_integer(n, edges, vector)
        return_probability = Fraction(vector[start], scale)
        errors.append(return_probability / stationary_probability(n, start) - 1)
    return errors


def multiplicative_error(
    n: int, edges: list[tuple[int, int]], steps: int
) -> tuple[Fraction, list[int]]:
    values = all_errors(n, edges, steps)
    maximum = max(values)
    return maximum, [state for state, value in enumerate(values) if value == maximum]


def complete_graph(n: int) -> list[tuple[int, int]]:
    return list(combinations(range(n), 2))


def path_graph(n: int) -> list[tuple[int, int]]:
    return [(i, i + 1) for i in range(n - 1)]


if __name__ == "__main__":
    for n in range(2, 7):
        for name, edges in (("K", complete_graph(n)), ("P", path_graph(n))):
            error, witnesses = multiplicative_error(n, edges, 10)
            print(n, name, error, witnesses)
