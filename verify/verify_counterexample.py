#!/usr/bin/env python3
"""Tiny exact checker for the K_3,3 counterexample (standard library only)."""

from fractions import Fraction as F

N = 6
EPSILON = F(3, 13)
K33 = [(u, v) for u in range(3) for v in range(3, 6)]
K6 = [(u, v) for u in range(N) for v in range(u + 1, N)]


def step(edges, vector):
    """Multiply a row distribution by (10|E|) times the exact kernel."""
    out = [0] * (1 << N)
    for x, mass in enumerate(vector):
        if not mass:
            continue
        for u, v in edges:
            z = x & ~(1 << u) & ~(1 << v)
            if ((x >> u) ^ (x >> v)) & 1:
                out[z | (1 << u)] += 5 * mass
                out[z | (1 << v)] += 5 * mass
            else:
                out[z] += 9 * mass
                out[z | (1 << u) | (1 << v)] += mass
    return out


def stationary(x):
    k = x.bit_count()
    sign = -1 if k & 1 else 1
    return F(3 ** (N - k), 2 ** (N - 1) * (2**N + sign))


def error(edges, gates):
    scale = (10 * len(edges)) ** gates
    values = []
    for start in range(1 << N):
        vector = [0] * (1 << N)
        vector[start] = 1
        for _ in range(gates):
            vector = step(edges, vector)
        values.append(F(vector[start], scale) / stationary(start) - 1)
    return max(values)


def main():
    values = {
        "K33_13": error(K33, 13),
        "K33_14": error(K33, 14),
        "K6_14": error(K6, 14),
        "K6_15": error(K6, 15),
    }
    expected = {
        "K33_13": F(274339976596040821, 919366980732421875),
        "K33_14": F(79546639693547185219, 344762617774658203125),
        "K6_14": F(61323079873072938701309, 263969600200653076171875),
        "K6_15": F(752104047129764606918347, 3959544003009796142578125),
    }
    assert values == expected
    assert values["K33_13"] > EPSILON > values["K33_14"]
    assert values["K6_14"] > EPSILON > values["K6_15"]
    print("PASS")
    print("s_(3/13)(K_3,3) = 14")
    print("s_(3/13)(K_6)   = 15")
    for name, value in values.items():
        print(f"{name}: {value} = {float(value):.15f}")


if __name__ == "__main__":
    main()
