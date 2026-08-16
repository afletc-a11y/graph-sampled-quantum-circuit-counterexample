# Literature and priority audit

Audit date: 2026-08-15.

## Primary target

Daniel Belkin, James Allen, and Bryan K. Clark,
[*Apparent Universal Behavior in Second Moments of Random Quantum Circuits*](https://arxiv.org/abs/2510.23726),
arXiv:2510.23726v2, revised 2026-07-24.

- Section 2 and Appendix A define multiplicative error and prove Theorem 1,
  reducing the `t=2` error under local invariance and PSD vectorization to the
  finite product experiments used here.
- Section 3 defines graph-sampled architectures as i.i.d. uniform edge choices
  followed by independent Haar-random two-site unitaries.
- Conjecture 3 says: "No other graph on n qudits forms an epsilon-approximate
  t-design with fewer gates than the complete graph."
- Conjecture 4 concerns **connection count**, not gate count.  Appendix B
  defines it through the maximum connected-block decomposition over equivalent
  architectures and explicitly says no guaranteed computation is known; the
  paper's naive and greedy algorithms provide lower bounds only.

The target paper itself distinguishes the exact multiplicative error from its
spectral gap and from anticoncentration.  The certificate in this package
computes the exact multiplicative error, not either proxy.

## Directly relevant prior work

Daniel Belkin, James Allen, and Bryan K. Clark,
[*Absence of censoring inequalities in random quantum circuits*](https://arxiv.org/abs/2502.15995),
arXiv:2502.15995v2, revised 2025-05-16.

- This is important negative prior art: adding/deleting gates or graph edges
  need not be monotone for several scrambling measures.
- For graph-sampled architectures it compares a lollipop graph with a path,
  first at the spectral-gap level, and uses general inequalities to infer that
  some additive- and multiplicative-error reversal exists.
- It does not show that any graph beats the complete graph.  The same authors
  subsequently stated complete-graph extremality as Conjecture 3 in
  arXiv:2510.23726v2.

Daniel Belkin et al.,
[*Approximate t-designs in generic circuit architectures*](https://arxiv.org/abs/2310.19783),
arXiv:2310.19783v3, revised 2024-05-17; published as PRX Quantum 5, 040344.

- Relates generic-architecture bounds to connected blocks and spectral gaps.
- It supplies context for connection-based upper bounds, not an exact
  multiplicative-error extremality theorem.

James Allen, Daniel Belkin, and Bryan K. Clark,
[*Conditional t-independent spectral gap for random quantum circuits and implications for t-design depths*](https://arxiv.org/abs/2411.13739),
arXiv:2411.13739v2, revised 2025-02-03.

- Gives strong spectral-gap results and explains their small-epsilon relevance.
- A gap comparison alone would not establish the finite-error claim attacked
  here; the present certificate evaluates the full finite-depth error.

## Follow-up search

Searches were run using:

- the exact paper title and arXiv identifier;
- exact language from Conjecture 3;
- combinations of "complete graph", "graph-sampled", "multiplicative error",
  and "approximate 2-design";
- the candidate graph names `K3,3` and `K_{3,3}`.

No paper or announcement resolving Conjecture 3 or giving this counterexample
was located.  The latest target version is only three weeks old and continues
to state the conjecture.  Accordingly, the correct priority language is:

> The exact `K_{3,3}` counterexample appears new in the searched literature as
> of 2026-08-15, but priority has not yet been confirmed by the authors or peer
> review.

This audit does not claim that an unindexed private note or very recent result
cannot exist.
