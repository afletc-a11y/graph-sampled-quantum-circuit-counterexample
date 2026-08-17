#!/usr/bin/env python3
"""Exact supporting evidence for the n=8 cocktail-party graph.

This is deliberately not advertised as a general family theorem.  The full
curve is computed with the exact heat-bath reduction, and representative
points at n=8 are checked independently against the equivalent exact
permutation-basis reduction.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

from exact_markov import _step_integer, stationary_probability, validate_graph
from exact_permutation import _step_integer as permutation_step_integer

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



def permutation_selected(edges, depths=(6, 16, 17)):
    """Permutation-basis maxima at selected depths in one evolution pass."""
    depths = tuple(sorted(depths))
    scale0 = 5 * len(edges)
    values = {s: [] for s in depths}
    for experiment in range(1 << N):
        character = [
            -1 if (experiment & state).bit_count() & 1 else 1
            for state in range(1 << N)
        ]
        vector = character[:]
        scale = 1
        k = experiment.bit_count()
        parity_sign = -1 if k & 1 else 1
        prefactor = F(2**N + parity_sign, 2 * 3 ** (N - k))
        for s in range(1, max(depths) + 1):
            vector = permutation_step_integer(N, edges, vector)
            scale *= scale0
            if s in values:
                quadratic = sum(x * y for x, y in zip(character, vector))
                values[s].append(prefactor * F(quadratic, scale) - 1)
    return {s: max(v) for s, v in values.items()}

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

    # The general reduced-representation cross-check only covers n<=7, so
    # explicitly validate n=8 at the start of the winning regime and on both
    # sides of the crossover.
    for name, edges, curve_values in (("CP8", CP8, cp), ("K8", K8, k8)):
        perm = permutation_selected(edges)
        for s in (6, 16, 17):
            assert perm[s] == curve_values[s][0], (name, s, curve_values[s][0], perm[s])

    print("PASS: CP8 beats K8 exactly at s=6,...,16 among s<=17")
    print("PASS: n=8 Markov/permutation cross-checks at s=6,16,17")
    print(f"s=16: CP8={cp[16][0]} < K8={k8[16][0]}")
    print(f"s=17: CP8={cp[17][0]} > K8={k8[17][0]}")
    print("Evidence at n=8 only; no general family theorem is claimed.")


if __name__ == "__main__":
    main()
