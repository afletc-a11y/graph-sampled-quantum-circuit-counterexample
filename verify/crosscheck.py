#!/usr/bin/env python3
"""Cross-check the independent exact evaluators on boundary and named graphs."""

from exact_markov import complete_graph, path_graph
from exact_markov import all_errors as markov_errors
from exact_permutation import all_errors as permutation_errors


def cycle_graph(n: int) -> list[tuple[int, int]]:
    return path_graph(n) + [(0, n - 1)]


def star_graph(n: int) -> list[tuple[int, int]]:
    return [(0, i) for i in range(1, n)]


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

    # One Haar-random two-qubit gate is already the global Haar second moment.
    assert max(markov_errors(2, [(0, 1)], 1)) == 0
    print(f"PASS: {checked} exact graph/depth cross-checks")


if __name__ == "__main__":
    main()
