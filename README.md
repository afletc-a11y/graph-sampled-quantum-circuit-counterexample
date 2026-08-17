# Complete-graph extremality counterexample for graph-sampled random quantum circuits

[![Verify exact certificate](https://github.com/afletc-a11y/graph-sampled-quantum-circuit-counterexample/actions/workflows/verify.yml/badge.svg)](https://github.com/afletc-a11y/graph-sampled-quantum-circuit-counterexample/actions/workflows/verify.yml)

## Result

Conjecture 3 of Belkin--Allen--Clark, *Apparent Universal Behavior in Second
Moments of Random Quantum Circuits* (arXiv:2510.23726v2), is false as literally
stated. A six-qubit counterexample occurs already at

\[
q=t=2,\qquad \epsilon=\frac56.
\]

Let `K_{2,2,2}` denote the octahedron graph, equivalently `K_6` with a perfect
matching removed. For the graph-sampled architecture that chooses an edge
uniformly and applies an independent Haar-random two-qubit gate,

\[
s_{5/6}(K_{2,2,2})=9 < 10=s_{5/6}(K_6).
\]

The exact depth-9 errors are

\[
M_{K_{2,2,2}}(9)=\frac{7432619383}{9112500000},\qquad
M_{K_6}(9)=\frac{18928429830211}{22247314453125}.
\]

Thus every

\[
\epsilon\in
\left[
\frac{7432619383}{9112500000},
\frac{18928429830211}{22247314453125}
\right)
\]

gives the same one-gate reversal `s_epsilon(K_{2,2,2})=9 < 10=s_epsilon(K_6)`.
The interval has exact width

\[
\frac{8345455089959}{237304687500000}
\approx 0.0351676791.
\]

The octahedron actually has smaller exact multiplicative error than `K_6` at
every gate count `s=6,...,15`, with the ordering reversing at `s=16`. The
widest finite-depth error window occurs at `s=6`, but that interval lies
entirely above `epsilon=1`:

\[
\left[\frac{33599}{13500},\frac{688547549}{263671875}\right).
\]

The earlier `K_{3,3}` witness remains valid but is weaker: it beats `K_6` only
at `s=14` (through the checked range `s<=45`).

## Verification

The core certificate uses exact integer/rational arithmetic only.

Run:

```bash
python3 verify/verify_counterexample.py
```

This checks the `epsilon=5/6` threshold, the exact values at `s=8,9,10`, the
full octahedron-vs-`K_6` crossover through `s=45`, and the older `K_{3,3}`
example.

For a direct audit from the paper's permutation-state definitions, run:

```bash
python3 verify/full_eq59_from_definitions.py
```

That checker independently constructs the `64 x 64` permutation-state Gram
matrix, constructs every two-site Haar moment operator as the `G`-orthogonal
projector onto the equality subspace, constructs the global Haar projector,
converts the coordinate action to the coefficient matrix used in Eq. 59, and
exhaustively evaluates all `64^2=4096` `(a,b)` experiments. It verifies the
full Eq. 59 maximum at every depth `s=6,...,16` for both the octahedron and
`K_6`.

Two faster exact evaluators are also retained:

```bash
python3 verify/crosscheck.py
```

They are **equivalent representations/reductions** of the same `q=t=2`
calculation (a parity-conditioned heat-bath chain and a nonorthogonal
permutation-basis transfer rule), not independent derivations. The
from-definition Eq. 59 checker above is the independent audit layer.

Finally,

```bash
python3 verify/cocktail_party_n8.py
```

checks the supporting `n=8` observation exactly: the cocktail-party graph
`K_8` minus a perfect matching beats `K_8` at `s=6,...,16` and loses again at
`s=17`. This is evidence for a pattern at `n=6,8`, **not** a claimed general
family theorem.

GitHub Actions runs the exact verification suite on every push and pull
request.

## Files

- `proof.md`: derivation and exact certificate.
- `STATUS.md`: what is proved, independently audited, exploratory, and open.
- `verify/verify_counterexample.py`: compact exact primary certificate.
- `verify/full_eq59_from_definitions.py`: independent full-Eq.-59 audit from
  the paper's Gram/projector definitions.
- `verify/exact_markov.py`: exact heat-bath reduction.
- `verify/exact_permutation.py`: equivalent exact permutation-basis reduction.
- `verify/crosscheck.py`: agreement checks between the two reduced evaluators.
- `verify/cocktail_party_n8.py`: exact `n=8` supporting evidence.
- `data/counterexample.json`: graph definitions and exact rational outputs.
- `search/census_float.py`: exploratory unlabeled-graph search, clearly
  separated from the proof.
- `requirements-search.txt`: optional dependencies for exploratory search only.
- `literature.md`: source and priority audit.
- `.github/workflows/verify.yml`: continuous exact verification.
- `CITATION.cff`: citation metadata.
- `LICENSE`: MIT license.

## Scope and caveats

One finite instance is enough to refute Conjecture 3 as written. This result
does **not** show that deleting a perfect matching is always beneficial, nor
that the cocktail-party graphs form a counterexample family.

The advantage is an intermediate-depth/intermediate-error effect. `K_6`
retakes the exact finite-depth lead at `s=16` and remains ahead through the
checked range `s<=45`. Numerically, its subleading decay mode is also smaller,
so the long-time/sufficiently-small-error regime favors the complete graph.
The repository does not promote that numerical spectral observation to a new
standalone theorem.

Conjecture 4 is separate. The valid `q=5,n=3` path-versus-triangle
counterexample is not packaged here, and later candidate witnesses at `q=15`
and `q=29` should not be promoted until they receive the same independent
full-Eq.-59 audit.

## Citation and research status

Citation metadata is provided in `CITATION.cff`. The counterexample is exact
and mechanically reproducible, but it has not yet been peer reviewed. See
`literature.md` for the searched literature and priority caveat.
