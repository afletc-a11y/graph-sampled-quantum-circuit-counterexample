#!/usr/bin/env python3
"""Cross-check two equivalent exact reduced representations."""

from itertools import combinations

from exact_markov import complete_graph, path_graph
from exact_markov import all_errors as markov_errors
from exact_permutation import all_errors as permutation_errors


def cycle_graph(n: int) -> list[tuple[int, int]]:
    return path_graph(n) + [(0, n - 1)]


def star_graph(n: int) -> list[tuple[int, int]]:
    return [(0, i) for i in range(1, n)]


def octahedron_graph() -> list[tuple[int, int]]:
    matching = {(0, 3), (1, 4), (2, 5)}
    return [e for e in combinations(range(6), 2) if e not in matching]


def main() -> None:
    families = {
        "complete": complete_graph,
        "path": path_graph,
        "cycle": cycle_graph,
        "star": star_graph,
    }
    checked = 0
    for n in range(2, 8):
        for name, constructor in families.items():
            if name == "cycle" and n < 3:
                continue
            edges = constructor(n)
            for steps in range(0, 9):
                left = markov_errors(n, edges, steps)
                right = permutation_errors(n, edges, steps)
                assert left == right, (n, name, steps)
                assert min(left) >= 0, (n, name, steps, min(left))
                if steps:
                    previous = markov_errors(n, edges, steps - 1)
                    assert max(left) <= max(previous), (n, name, steps)
                checked += 1

    # Add the primary witness through its crossover.
    oct_edges = octahedron_graph()
    for steps in range(0, 17):
        left = markov_errors(6, oct_edges, steps)
        right = permutation_errors(6, oct_edges, steps)
        assert left == right, (6, "octahedron", steps)
        checked += 1

    # One Haar-random two-qubit gate is already the global Haar second moment.
    assert max(markov_errors(2, [(0, 1)], 1)) == 0
    print(f"PASS: {checked} exact graph/depth cross-checks")
    print("Representations agree; they are equivalent reductions, not independent derivations.")


if __name__ == "__main__":
    main()
