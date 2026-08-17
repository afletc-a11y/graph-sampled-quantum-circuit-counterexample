#!/usr/bin/env python3
"""Exact supporting witnesses on seven vertices.

These are finite examples found by the exploratory graph census.  They are not
used by the primary six-qubit counterexample and are not presented as a family
theorem.

The two graphs are:
  * K7 minus a Hamiltonian 7-cycle C7;
  * K7 minus the disjoint union C3 + C4.

The heat-bath and permutation-basis reductions are compared at representative
points, including both sides of each crossover.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

from exact_markov import multiplicative_error as markov_error
from exact_permutation import multiplicative_error as permutation_error

N = 7
K7 = list(combinations(range(N), 2))
C7 = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
K7_MINUS_C7 = [e for e in K7 if e not in C7]

C3_UNION_C4 = {
    tuple(sorted(e))
    for e in (
        (0, 1), (1, 2), (2, 0),
        (3, 4), (4, 5), (5, 6), (6, 3),
    )
}
K7_MINUS_C3_C4 = [e for e in K7 if e not in C3_UNION_C4]

EXPECTED_WIDEST_SUB1 = {
    "K7-C7": {
        "s": 11,
        "graph": F(12179988456128649, 13792736767578125),
        "K7": F(2427499625871482657, 2585547026630859375),
        "width": F(5049582644841826906, 90494145932080078125),
    }
}


def exact_curve(edges, smax: int = 15):
    return {s: markov_error(N, edges, s)[0] for s in range(1, smax + 1)}


def crosscheck(name: str, edges, curve, depths) -> None:
    for s in depths:
        perm, _ = permutation_error(N, edges, s)
        assert perm == curve[s], (name, s, curve[s], perm)


def main() -> None:
    k7 = exact_curve(K7)
    g1 = exact_curve(K7_MINUS_C7)
    g2 = exact_curve(K7_MINUS_C3_C4)

    hits1 = [s for s in range(1, 16) if g1[s] < k7[s]]
    hits2 = [s for s in range(1, 16) if g2[s] < k7[s]]
    assert hits1 == list(range(6, 15)), hits1
    assert hits2 == [12, 13, 14], hits2

    w = EXPECTED_WIDEST_SUB1["K7-C7"]
    assert g1[w["s"]] == w["graph"]
    assert k7[w["s"]] == w["K7"]
    assert w["K7"] - w["graph"] == w["width"]

    # Representative agreement checks between the two equivalent exact
    # reductions, including entry/exit of the winning regimes.
    crosscheck("K7", K7, k7, (6, 11, 12, 14, 15))
    crosscheck("K7-C7", K7_MINUS_C7, g1, (6, 11, 14, 15))
    crosscheck("K7-(C3+C4)", K7_MINUS_C3_C4, g2, (11, 12, 14, 15))

    print("PASS: exact seven-vertex supporting witnesses")
    print("K7-C7 beats K7 at s=6,...,14 among s<=15")
    print("K7-(C3+C4) beats K7 at s=12,13,14 among s<=15")
    print(
        "K7-C7 s=11 interval: "
        f"[{w['graph']}, {w['K7']}) width={w['width']}"
    )
    print("Representative n=7 Markov/permutation comparisons agree exactly.")


if __name__ == "__main__":
    main()
