# Literature and priority audit

Audit updated: 2026-08-17.

## Primary target

Daniel Belkin, James Allen, and Bryan K. Clark,
[*Apparent Universal Behavior in Second Moments of Random Quantum Circuits*](https://arxiv.org/abs/2510.23726),
arXiv:2510.23726v2, revised 2026-07-24.

- Section 2 and Appendix A define multiplicative error and prove the finite
  `t=2` experiment reduction.
- Section 3 defines graph-sampled architectures as i.i.d. uniform edge choices
  followed by independent Haar-random two-site unitaries.
- Conjecture 3 says: "No other graph on n qudits forms an ϵ-approximate
  t-design with fewer gates than the complete graph, which requires
  Θ(n log n) gates."
- Appendix A.5 gives the full `t=2` maximum in Eq. 59; Appendix A.9 proves that
  a diagonal experiment saturates it for the PSD-vectorized architectures at
  issue here.
- Conjecture 4 concerns **connection count**, not gate count, and is separate
  from this repository's Conjecture 3 certificate.

The certificate computes the exact multiplicative error, not a spectral-gap or
anticoncentration proxy. The trailing asymptotic clause in Conjecture 3 is
important context: the present result refutes the literal finite gate-count
extremality statement, while leaving open repaired statements restricted to a
sufficiently small error regime or an asymptotic interpretation.

## Directly relevant prior work

Daniel Belkin, James Allen, and Bryan K. Clark,
[*Absence of censoring inequalities in random quantum circuits*](https://arxiv.org/abs/2502.15995),
arXiv:2502.15995v2, revised 2025-05-16.

- Adding/deleting gates or graph edges need not be monotone for several
  scrambling measures.
- It does not show that a graph beats the complete graph in the gate-count
  extremality claim later stated as Conjecture 3.

Daniel Belkin et al.,
[*Approximate t-designs in generic circuit architectures*](https://arxiv.org/abs/2310.19783),
arXiv:2310.19783v3; PRX Quantum 5, 040344.

James Allen, Daniel Belkin, and Bryan K. Clark,
[*Conditional t-independent spectral gap for random quantum circuits and implications for t-design depths*](https://arxiv.org/abs/2411.13739),
arXiv:2411.13739v2.

These works provide architecture, connection-count, and spectral-gap context,
but not this exact finite-error complete-graph counterexample.

## Follow-up search

Searches through 2026-08-17 used the target title/arXiv identifier, Conjecture 3
language, and combinations of `complete graph`, `graph-sampled`,
`multiplicative error`, `K_{3,3}`, `K_{2,2,2}`, `octahedron`, and
`cocktail-party graph`. No paper or announcement resolving Conjecture 3 or
giving the present six-qubit witness was located.

The authors have publicly presented the broader work, including the claim that
the *parallel* complete-graph architecture is not quite the fastest scrambler;
that is a different architecture/comparison and does not supply the present
graph-sampled Conjecture 3 counterexample.

Accordingly, the appropriate priority language is:

> The exact six-qubit graph-sampled counterexample appears new in the searched
> literature as of 2026-08-17, but priority has not yet been confirmed by the
> authors or peer review.

This audit cannot exclude unindexed private notes or very recent work.
