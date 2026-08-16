# Status

Date: 2026-08-15

## Proved

For graph-sampled Haar-random two-qubit circuits on six qubits, in the paper's
multiplicative-error metric at `q=t=2`,

\[
s_{3/13}(K_{3,3})=14,\qquad s_{3/13}(K_6)=15.
\]

The four exact values bracketing the threshold are

\[
\begin{aligned}
M_{K_{3,3}}(13)
 &=\frac{274339976596040821}{919366980732421875},\\
M_{K_{3,3}}(14)
 &=\frac{79546639693547185219}{344762617774658203125},\\
M_{K_6}(14)
 &=\frac{61323079873072938701309}{263969600200653076171875},\\
M_{K_6}(15)
 &=\frac{752104047129764606918347}{3959544003009796142578125}.
\end{aligned}
\]

They satisfy

\[
M_{K_{3,3}}(13)>\frac3{13}>M_{K_{3,3}}(14),\qquad
M_{K_6}(14)>\frac3{13}>M_{K_6}(15).
\]

The proof depends on:

1. Theorem 1 and Appendix A of arXiv:2510.23726v2, which reduce `t=2`
   multiplicative error for graph-sampled circuits to finitely many product
   experiments.
2. The exact two-site Haar-projector rule derived in `proof.md`.
3. Exhaustive integer recurrence over 64 states for the four graph/depth
   pairs above.

## Independently checked

- The exact Markov evaluator and exact nonorthogonal permutation-basis
  evaluator agree on 207 graph/depth cases.
- Boundary case `n=2`: one gate gives the global Haar second moment and zero
  error.
- All computed experiment errors are nonnegative, as required by PSD
  vectorization.
- Maximum error is nonincreasing with gate count on the cross-check suite.
- Named-family behavior agrees qualitatively with the source paper: complete
  graphs beat paths, cycles, and stars at the source's small-system tests.

## Exploratory only

An unlabeled connected-graph census using the NetworkX Graph Atlas and
floating-point eigendecomposition found no complete-graph violation for
`n<=5` through 200 gates.  It found the exact `K_{3,3}` candidate at `n=6`,
as well as other early-depth candidates.  These census statements are not
part of the proof and are not used for a minimality claim.

## Novelty status

The latest source version, arXiv:2510.23726v2 dated 2026-07-24, still states
Conjecture 3.  Searches by title, arXiv identifier, statement language, and
the candidate graph found no follow-up resolving it through 2026-08-15.
The authors' earlier censoring paper proves that graph-edge deletion can help
in other graph comparisons, so the phenomenon is not new in general; the
specific complete-graph extremality counterexample appears new but should be
confirmed with the authors before making an unconditional priority claim.

## Not addressed

- Conjecture 4 and its exact architecture-equivalence connection count.
- Whether `K_n` is extremal for every sufficiently small `epsilon`.
- Whether the conjecture holds asymptotically at fixed `epsilon=0.01`.
- The smallest possible counterexample over every `epsilon` (the search only
  establishes an exact example at `n=6`).
