# Complete-graph extremality for graph-sampled random quantum circuits

[![Verify exact certificate](https://github.com/afletc-a11y/graph-sampled-quantum-circuit-counterexample/actions/workflows/verify.yml/badge.svg)](https://github.com/afletc-a11y/graph-sampled-quantum-circuit-counterexample/actions/workflows/verify.yml)

## Result

Conjecture 3 of Belkin--Allen--Clark, *Apparent Universal Behavior in
Second Moments of Random Quantum Circuits* (arXiv:2510.23726v2), is false as
literally stated.  A six-qubit counterexample already occurs at

\[
q=t=2,\qquad \epsilon=\frac{3}{13}.
\]

For the graph-sampled architecture that chooses an edge uniformly and applies
an independent Haar-random two-qubit gate,

\[
s_{3/13}(K_{3,3})=14 < 15=s_{3/13}(K_6).
\]

Thus a connected graph other than the complete graph reaches the specified
multiplicative-error approximate 2-design threshold with one fewer gate.

The result is an exact finite calculation, not floating-point evidence.  The
trusted checker uses only integer arithmetic and `fractions.Fraction` from the
Python standard library.

## Verify

From this directory, run:

```bash
python3 verify/verify_counterexample.py
```

Expected first three lines:

```text
PASS
s_(3/13)(K_3,3) = 14
s_(3/13)(K_6)   = 15
```

For a stronger cross-check using two independent exact representations, run:

```bash
python3 verify/crosscheck.py
```

This compares the parity-conditioned heat-bath evaluator with a separate
permutation-basis Haar-projector evaluator on complete graphs, paths, cycles,
and stars for `n=2,...,7` and gate counts `0,...,8`.

GitHub Actions runs both commands automatically on every push and pull request.

## Optional exploratory census

The proof and trusted checker have no third-party dependencies. To rerun the
floating-point graph census used to locate candidates:

```bash
python3 -m pip install -r requirements-search.txt
python3 search/census_float.py
```

The census is exploratory only and is not used by the proof.

## Files

- `proof.md`: derivation from the paper's exact multiplicative-error formula.
- `STATUS.md`: what is proved, audited, and still open.
- `verify/verify_counterexample.py`: minimal trusted checker.
- `verify/exact_markov.py`: reusable exact heat-bath evaluator.
- `verify/exact_permutation.py`: independent exact permutation-basis evaluator.
- `verify/crosscheck.py`: boundary and named-family cross-checks.
- `data/counterexample.json`: edge lists and exact rational outputs.
- `search/census_float.py`: exploratory unlabeled-graph search, clearly
  separated from the proof.
- `requirements-search.txt`: optional dependencies for the exploratory census.
- `literature.md`: source and priority audit through 2026-08-15.
- `.github/workflows/verify.yml`: continuous exact verification.
- `CITATION.cff`: citation metadata.
- `LICENSE`: MIT license.

## Scope

This refutes Conjecture 3 because that conjecture quantifies over all graphs,
qudit dimensions, design orders, and errors; one `q=t=2` instance suffices.
It does **not** disprove a possible repaired statement restricted to a fixed
small error such as `0.01`, to sufficiently small error, or to asymptotic
leading-order gate counts.  Conjecture 4, involving exact connection count,
is not addressed here.

## Citation and research status

Citation metadata is provided in `CITATION.cff`. The result is an exact,
independently cross-checked computational counterexample, but it has not yet
been peer reviewed. The searched literature and current priority assessment
are recorded in `literature.md`.
