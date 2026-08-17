#!/usr/bin/env python3
"""Compact exact certificate for the octahedron-vs-K6 Conjecture 3 witness."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

from exact_markov import _step_integer, stationary_probability, validate_graph

N = 6
EPSILON = F(5, 6)
K6 = list(combinations(range(N), 2))
MATCHING = {(0, 3), (1, 4), (2, 5)}
OCT = [e for e in K6 if e not in MATCHING]
K33 = [(u, v) for u in range(3) for v in range(3, 6)]

EXPECTED = {
    "OCT": {
        6: F(33599, 13500),
        7: F(670763, 405000),
        8: F(347115007, 303750000),
        9: F(7432619383, 9112500000),
        10: F(164340848531, 273375000000),
        11: F(3742792966739, 8201250000000),
        12: F(87497699793367, 246037500000000),
        13: F(2091179994376783, 7381125000000000),
        14: F(50883397954775963, 221433750000000000),
        15: F(1255671691351725707, 6643012500000000000),
        16: F(31321978687651130143, 199290375000000000000),
    },
    "K6": {
        6: F(688547549, 263671875),
        7: F(6895839979, 3955078125),
        8: F(1778369294789, 1483154296875),
        9: F(18928429830211, 22247314453125),
        10: F(5197395863758829, 8342742919921875),
        11: F(58801416885883483, 125141143798828125),
        12: F(17076032469901475669, 46927928924560546875),
        13: F(40565330678290716119, 140783786773681640625),
        14: F(61323079873072938701309, 263969600200653076171875),
        15: F(752104047129764606918347, 3959544003009796142578125),
        16: F(233071489177475058812811749, 1484829001128673553466796875),
    },
}

OLD_K33 = {
    13: F(274339976596040821, 919366980732421875),
    14: F(79546639693547185219, 344762617774658203125),
}


def error_curve(edges: list[tuple[int, int]], smax: int):
    edges = validate_graph(N, edges)
    scale0 = 10 * len(edges)
    per_depth = [[] for _ in range(smax + 1)]
    for start in range(1 << N):
        vector = [0] * (1 << N)
        vector[start] = 1
        scale = 1
        pi = stationary_probability(N, start)
        for s in range(1, smax + 1):
            vector = _step_integer(N, edges, vector)
            scale *= scale0
            per_depth[s].append(F(vector[start], scale) / pi - 1)
    out = {}
    for s in range(1, smax + 1):
        best = max(per_depth[s])
        args = [a for a, value in enumerate(per_depth[s]) if value == best]
        out[s] = (best, args)
    return out


def main() -> None:
    oct_curve = error_curve(OCT, 45)
    k6_curve = error_curve(K6, 45)
    k33_curve = error_curve(K33, 45)

    for s, value in EXPECTED["OCT"].items():
        assert oct_curve[s][0] == value, ("OCT", s, oct_curve[s][0], value)
    for s, value in EXPECTED["K6"].items():
        assert k6_curve[s][0] == value, ("K6", s, k6_curve[s][0], value)
    for s, value in OLD_K33.items():
        assert k33_curve[s][0] == value, ("K33", s, k33_curve[s][0], value)

    assert oct_curve[8][0] > EPSILON > oct_curve[9][0]
    assert k6_curve[9][0] > EPSILON > k6_curve[10][0]

    # Certify the threshold definitions directly: these are the first
    # gate counts at which the error is at most epsilon = 5/6.
    assert min(s for s in range(1, 46) if oct_curve[s][0] <= EPSILON) == 9
    assert min(s for s in range(1, 46) if k6_curve[s][0] <= EPSILON) == 10

    oct_hits = [s for s in range(1, 46) if oct_curve[s][0] < k6_curve[s][0]]
    k33_hits = [s for s in range(1, 46) if k33_curve[s][0] < k6_curve[s][0]]
    assert oct_hits == list(range(6, 16)), oct_hits
    assert k33_hits == [14], k33_hits

    assert oct_curve[16][0] > k6_curve[16][0]
    assert oct_curve[16][0] - k6_curve[16][0] == F(
        403370653013498662089332657,
        2027286529541015625000000000000,
    )

    for s in range(6, 17):
        assert oct_curve[s][1] == [63], ("OCT argmax", s, oct_curve[s][1])
        assert k6_curve[s][1] == [63], ("K6 argmax", s, k6_curve[s][1])

    width9 = k6_curve[9][0] - oct_curve[9][0]
    assert width9 == F(8345455089959, 237304687500000)
    ratio14 = (k6_curve[14][0] - oct_curve[14][0]) / (
        k6_curve[14][0] - k33_curve[14][0]
    )
    assert ratio14 == F(
        83556125512633375224389442711,
        52457551975595363824242958336,
    )

    print("PASS")
    print("s_(5/6)(K_2,2,2) = 9")
    print("s_(5/6)(K_6)     = 10")
    print("octahedron beats K_6 exactly at s=6,...,15 among s<=45")
    print("K_3,3 beats K_6 only at s=14 among s<=45")
    print(f"depth-9 epsilon interval = [{oct_curve[9][0]}, {k6_curve[9][0]})")
    print(f"depth-9 interval width   = {width9}")
    print(f"s=14 width ratio vs K_3,3 = {ratio14}")


if __name__ == "__main__":
    main()
