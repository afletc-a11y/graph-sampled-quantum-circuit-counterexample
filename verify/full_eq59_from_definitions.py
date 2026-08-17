#!/usr/bin/env python3
"""Independent full-Eq.-59 audit from the paper's permutation-state definitions.

This checker intentionally does NOT use the heat-bath transition, Walsh
conjugation, or a hand-inserted 2/5 coefficient.  It constructs the q=t=2
permutation-state Gram matrix, solves the G-orthogonal projection problem for
each edge, constructs the global Haar projector, converts coordinate-action
matrices to the coefficient matrices that appear in Eq. 59, and exhaustively
checks all 64^2 (a,b) pairs at depths 6,...,16.

Standard library only; all arithmetic is exact fractions/integers.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

NQ = 6
DIM = 1 << NQ
Q = 2
K6 = list(combinations(range(NQ), 2))
MATCHING = {(0, 3), (1, 4), (2, 5)}
OCT = [e for e in K6 if e not in MATCHING]

EXPECTED_OCT = {
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
}
EXPECTED_K6 = {
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
}


def inverse(matrix: list[list[F]]) -> list[list[F]]:
    n = len(matrix)
    aug = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            f = aug[row][col]
            aug[row] = [x - f * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def matvec(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def int_matvec(matrix: list[list[int]], vector: list[F]) -> list[F]:
    return [sum(F(a) * b for a, b in zip(row, vector)) for row in matrix]


def gram() -> list[list[F]]:
    return [[F(1, Q ** ((x ^ y).bit_count())) for y in range(DIM)] for x in range(DIM)]


G = gram()
GINV = inverse(G)


def g_projector(keep: list[int]) -> list[list[F]]:
    """Coordinate action of the exact G-orthogonal projector onto span(keep)."""
    k = len(keep)
    vt_g = [[G[keep[i]][j] for j in range(DIM)] for i in range(k)]
    vt_g_v = [[vt_g[i][keep[j]] for j in range(k)] for i in range(k)]
    inv = inverse(vt_g_v)
    inner = [
        [sum(inv[i][t] * vt_g[t][j] for t in range(k)) for j in range(DIM)]
        for i in range(k)
    ]
    p = [[F(0)] * DIM for _ in range(DIM)]
    for i, basis_state in enumerate(keep):
        p[basis_state] = inner[i]

    # Exact structural audit: range is the requested subspace, every kept basis
    # vector is fixed, and the residual is G-orthogonal to that subspace.
    keep_set = set(keep)
    for i in range(DIM):
        if i not in keep_set:
            assert all(x == 0 for x in p[i])
    for col in keep:
        for row in range(DIM):
            assert p[row][col] == F(row == col)
    for r in keep:
        for col in range(DIM):
            projected_overlap = sum(G[r][i] * p[i][col] for i in keep)
            assert G[r][col] - projected_overlap == 0
    return p


EDGE_PROJECTORS = {}
for edge in K6:
    u, v = edge
    keep = [x for x in range(DIM) if ((x >> u) & 1) == ((x >> v) & 1)]
    EDGE_PROJECTORS[edge] = g_projector(keep)

HAAR = g_projector([0, DIM - 1])


def character(mask: int) -> list[F]:
    return [F(-1 if (mask & x).bit_count() & 1 else 1) for x in range(DIM)]


CHARS = [character(a) for a in range(DIM)]
GINV_CHARS = [matvec(GINV, v) for v in CHARS]
HAAR_COEFF_ACTION = [matvec(HAAR, x) for x in GINV_CHARS]
HAAR_DEN = [
    [sum(CHARS[a][i] * HAAR_COEFF_ACTION[b][i] for i in range(DIM)) for b in range(DIM)]
    for a in range(DIM)
]


def transfer_integer(edges: list[tuple[int, int]]) -> tuple[list[list[int]], int]:
    """Derive A=5|E| C_G from the solved projectors, asserting integrality."""
    acc = [[F(0)] * DIM for _ in range(DIM)]
    for edge in edges:
        p = EDGE_PROJECTORS[edge]
        for i in range(DIM):
            for j in range(DIM):
                acc[i][j] += p[i][j]
    # C_G = acc / |E|, hence 5|E| C_G = 5 acc.
    a = []
    for row in acc:
        int_row = []
        for value in row:
            value5 = 5 * value
            assert value5.denominator == 1
            int_row.append(value5.numerator)
        a.append(int_row)
    return a, 5 * len(edges)


def full_curve(edges: list[tuple[int, int]], expected: dict[int, F], name: str):
    a_matrix, scale0 = transfer_integer(edges)
    evolved = [x[:] for x in GINV_CHARS]
    scale = 1
    results = {}

    for depth in range(1, 17):
        evolved = [int_matvec(a_matrix, vec) for vec in evolved]
        scale *= scale0
        if depth < 6:
            continue

        best = F(-1)
        best_pairs = []
        diagonal_best = F(-1)
        diagonal_args = []
        for aa in range(DIM):
            va = CHARS[aa]
            for bb in range(DIM):
                den = HAAR_DEN[aa][bb]
                if den == 0:
                    continue
                num = sum(va[i] * evolved[bb][i] for i in range(DIM)) / scale
                value = abs(num / den - 1)
                if value > best:
                    best = value
                    best_pairs = [(aa, bb)]
                elif value == best:
                    best_pairs.append((aa, bb))
                if aa == bb:
                    if value > diagonal_best:
                        diagonal_best = value
                        diagonal_args = [aa]
                    elif value == diagonal_best:
                        diagonal_args.append(aa)

        assert best == diagonal_best, (name, depth, best, diagonal_best, best_pairs)
        assert best == expected[depth], (name, depth, best, expected[depth])
        assert diagonal_args == [63], (name, depth, diagonal_args)
        results[depth] = best
        print(f"{name} s={depth}: full Eq.59 = {best}; maximizing diagonal experiment = 63")
    return results


def main() -> None:
    # Sanity checks on the full Gram inverse.
    for i in range(DIM):
        for j in range(DIM):
            value = sum(G[i][k] * GINV[k][j] for k in range(DIM))
            assert value == F(i == j)

    oct_results = full_curve(OCT, EXPECTED_OCT, "K_2,2,2")
    k6_results = full_curve(K6, EXPECTED_K6, "K_6")
    assert [s for s in range(6, 17) if oct_results[s] < k6_results[s]] == list(range(6, 16))
    assert oct_results[16] > k6_results[16]
    print("PASS: direct Gram/projector construction and all-pair Eq.59 audit")


if __name__ == "__main__":
    main()
