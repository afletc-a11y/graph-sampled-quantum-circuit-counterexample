#!/usr/bin/env python3
"""Independent exact evaluator in the nonorthogonal permutation basis.

For q=2 the two-site Haar projector has the rules
  00 -> 00, 11 -> 11, 01/10 -> (2/5)(00+11).
This checker never uses the Markov-chain transition or its stationary law.
"""

from __future__ import annotations

from fractions import Fraction

from exact_markov import validate_graph


def _step_integer(
    n: int, edges: list[tuple[int, int]], vector: list[int]
) -> list[int]:
    """Multiply a column by P=(5|E|)T in the permutation basis."""
    out = [0] * (1 << n)
    for state, amplitude in enumerate(vector):
        if not amplitude:
            continue
        for u, v in edges:
            bu = (state >> u) & 1
            bv = (state >> v) & 1
            if bu == bv:
                out[state] += 5 * amplitude
            else:
                cleared = state & ~(1 << u) & ~(1 << v)
                out[cleared] += 2 * amplitude
                out[cleared | (1 << u) | (1 << v)] += 2 * amplitude
    return out


def all_errors(n: int, edges: list[tuple[int, int]], steps: int) -> list[Fraction]:
    edges = validate_graph(n, edges)
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    scale = (5 * len(edges)) ** steps
    errors: list[Fraction] = []
    for experiment in range(1 << n):
        character = [
            -1 if (experiment & state).bit_count() & 1 else 1
            for state in range(1 << n)
        ]
        vector = character[:]
        for _ in range(steps):
            vector = _step_integer(n, edges, vector)
        quadratic_numerator = sum(x * y for x, y in zip(character, vector))
        k = experiment.bit_count()
        parity_sign = -1 if k & 1 else 1
        prefactor = Fraction(2**n + parity_sign, 2 * 3 ** (n - k))
        errors.append(prefactor * Fraction(quadratic_numerator, scale) - 1)
    return errors


def multiplicative_error(
    n: int, edges: list[tuple[int, int]], steps: int
) -> tuple[Fraction, list[int]]:
    values = all_errors(n, edges, steps)
    maximum = max(values)
    return maximum, [state for state, value in enumerate(values) if value == maximum]
