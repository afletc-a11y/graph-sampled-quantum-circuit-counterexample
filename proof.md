# Exact counterexample to complete-graph gate-count extremality

## Theorem

Let each step choose an edge uniformly from a connected graph on six qubits
and apply an independent Haar-random two-qubit unitary. Let `M_G(s)` be the
multiplicative error of the second-moment channel after `s` gates relative to
the global Haar second moment, and let

\[
s_\epsilon(G)=\min\{s:M_G(s)\leq\epsilon\}.
\]

Let `O_6=K_{2,2,2}` be the octahedron graph, equivalently `K_6` with the
perfect matching `[(0,3),(1,4),(2,5)]` removed. Then

\[
\boxed{s_{5/6}(O_6)=9<10=s_{5/6}(K_6).}
\]

Consequently Conjecture 3 of arXiv:2510.23726v2 is false as stated.

The older `K_{3,3}` certificate at `epsilon=3/13` remains valid but is retained
only as a secondary example.

## 1. From the paper's permutation-state definitions

For `t=2,q=2`, label the two local permutation states by `0` (identity) and
`1` (swap). Their single-site Gram matrix is

\[
B=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
\]

For `n=6`, the full permutation-state Gram matrix is therefore

\[
G_{x,y}=2^{-|x\oplus y|},\qquad x,y\in\{0,1\}^6.
\]

For an edge `e={u,v}`, the two-site Haar moment fixes exactly the subspace
spanned by permutation strings with equal endpoint labels, `x_u=x_v`. If `V_e`
is the selector matrix whose columns are those basis states, its coordinate
action is the `G`-orthogonal projector

\[
P_e=V_e(V_e^TGV_e)^{-1}V_e^TG.
\]

The checker `verify/full_eq59_from_definitions.py` constructs this projector by
exact rational Gaussian elimination. It does not assume the familiar `2/5`
coefficient. That coefficient emerges from the solved projector.

For a graph with `m` edges, one gate has coordinate action

\[
C_G=\frac1m\sum_{e\in E(G)}P_e.
\]

The global Haar projector is constructed in the same way from the two basis
states `0^6` and `1^6`.

## 2. Explicit Equation 59 evaluation

Appendix A.5 of the source paper writes the `t=2` multiplicative error as the
maximum in Eq. 59 over every pair of sign/trivial irrep labels
`(a,b) in {+1,-1}^6 x {+1,-1}^6`. The matrices appearing there are the
**coefficient matrices** of the moment operator in the nonorthogonal
permutation basis.

If `C` is the coordinate-action matrix in that basis, then its coefficient
matrix is

\[
M=C G^{-1},
\]

because the coordinate action satisfies `C=M G`. Thus, for depth `s`,

\[
M_G^{(s)}=C_G^sG^{-1}.
\]

The direct checker explicitly inverts the full Gram matrix, forms this
coefficient action, and evaluates Eq. 59 over all `64^2=4096` pairs. Pairs with
zero global-Haar denominator are omitted exactly as prescribed immediately
before Eq. 59 in the paper.

Appendix A.9 proves diagonal dominance for PSD-vectorized architectures. The
direct exhaustive calculation independently confirms that the full Eq. 59
maximum equals the diagonal maximum at every audited depth `s=6,...,16` for
both `O_6` and `K_6`.

## 3. Exact primary certificate at epsilon = 5/6

The requested neighboring values are

\[
\begin{array}{c|cc}
s&M_{O_6}(s)&M_{K_6}(s)\\ \hline
8&\frac{347115007}{303750000}
&\frac{1778369294789}{1483154296875}\\[4pt]
9&\frac{7432619383}{9112500000}
&\frac{18928429830211}{22247314453125}\\[4pt]
10&\frac{164340848531}{273375000000}
&\frac{5197395863758829}{8342742919921875}
\end{array}
\]

At `epsilon=5/6`,

\[
M_{O_6}(8)-\frac56
=\frac{93990007}{303750000}>0,
\]

\[
M_{O_6}(9)-\frac56
=-\frac{161130617}{9112500000}<0,
\]

\[
M_{K_6}(9)-\frac56
=\frac{778002238547}{44494628906250}>0,
\]

and

\[
M_{K_6}(10)-\frac56
=-\frac{3509779805685467}{16685485839843750}<0.
\]

Hence the claimed gate counts follow.

Equivalently, every epsilon in the exact sub-1 interval

\[
\boxed{
\left[
\frac{7432619383}{9112500000},
\frac{18928429830211}{22247314453125}
\right)
}
\]

gives `s_epsilon(O_6)=9<10=s_epsilon(K_6)`. Its exact width is

\[
\frac{8345455089959}{237304687500000}.
\]

## 4. Exact crossover window

The exact errors at every depth where the octahedron beats `K_6`, together
with the first reversed depth, are:

\[
\begin{array}{c|cc}
s&M_{O_6}(s)&M_{K_6}(s)\\ \hline
6&33599/13500&688547549/263671875\\
7&670763/405000&6895839979/3955078125\\
8&347115007/303750000&1778369294789/1483154296875\\
9&7432619383/9112500000&18928429830211/22247314453125\\
10&164340848531/273375000000&5197395863758829/8342742919921875\\
11&3742792966739/8201250000000&58801416885883483/125141143798828125\\
12&87497699793367/246037500000000&17076032469901475669/46927928924560546875\\
13&2091179994376783/7381125000000000&40565330678290716119/140783786773681640625\\
14&50883397954775963/221433750000000000&61323079873072938701309/263969600200653076171875\\
15&1255671691351725707/6643012500000000000&752104047129764606918347/3959544003009796142578125\\
16&31321978687651130143/199290375000000000000&233071489177475058812811749/1484829001128673553466796875
\end{array}
\]

For `s=6,...,15` the left entry is smaller. At `s=16`,

\[
M_{O_6}(16)-M_{K_6}(16)
=\frac{403370653013498662089332657}
{2027286529541015625000000000000}>0,
\]

so `K_6` retakes the lead. The exact reduced evaluator checks through `s=45`
and finds no later octahedron win in that range.

The widest epsilon interval occurs at `s=6`,

\[
\left[\frac{33599}{13500},\frac{688547549}{263671875}\right),
\]

of width

\[
\frac{129268321}{1054687500}.
\]

Because this interval lies above `epsilon=1`, the main statement instead uses
the cleaner sub-1 `s=9` interval and `epsilon=5/6`.

## 5. Maximizing experiment near the crossover

At every depth `s=6,...,16`, both `O_6` and `K_6` have the same unique diagonal
maximizer: bitmask `63`, Hamming weight `6` (the all-sign experiment in this
encoding). Therefore the reversal between `s=15` and `s=16` is not an optimizer
or Hamming-weight switch. Any explanation in terms of an "elbow" or "anarchy"
mechanism remains interpretation until its spectral/dynamical content is
separately established.

## 6. Comparison with the earlier K_3,3 witness

The old result

\[
s_{3/13}(K_{3,3})=14<15=s_{3/13}(K_6)
\]

is still exact. Through `s=45`, however, `K_{3,3}` beats `K_6` only at `s=14`.
At that depth the octahedron's reversal interval is wider by

\[
\frac{83556125512633375224389442711}
{52457551975595363824242958336}
\approx1.5928331073.
\]

This is why `O_6` is the primary witness in the repository.

## 7. Additional exact finite witnesses

Two additional seven-vertex witnesses were found by the exploratory census
and then checked exactly. The first is `K_7-C_7`, which satisfies

\[
M_{K_7-C_7}(s)<M_{K_7}(s)\qquad(s=6,\ldots,14),
\]

within the exact checked range through `s=15`. Its widest sub-1 interval is at
`s=11`:

\[
\left[
\frac{12179988456128649}{13792736767578125},
\frac{2427499625871482657}{2585547026630859375}
\right),
\]

with exact width

\[
\frac{5049582644841826906}{90494145932080078125}.
\]

The second is `K_7-(C_3\sqcup C_4)`, which beats `K_7` at `s=12,13,14`
within the same checked range. The first interval is about `1.5867x` wider than
the octahedron's widest sub-1 interval, but the octahedron is retained as the
primary witness because it occurs at smaller `n`, gives the clean `5/6`
certificate, and reaches a substantially lower-error reversal regime.

The exact reduced evaluator also checks the cocktail-party graph `CP_8`,
`K_8` with a perfect matching removed. It finds

\[
M_{CP_8}(s)<M_{K_8}(s)\qquad(s=6,\ldots,16),
\]

with reversal at `s=17`. For example,

\[
M_{CP_8}(16)=
\frac{37222906637142989511155183}{65303470080000000000000000}
<
\frac{4008961629021877754048110238049}
{6945004265973760000000000000000}
=M_{K_8}(16),
\]

whereas the inequality reverses at `s=17`.

The `n=8` checker explicitly compares the Markov and permutation-basis
reductions at `s=6,16,17`. These additional `n=7,8` examples are finite
evidence only; no general cocktail-party or deletion-family theorem is
claimed.

The four `n=6,7` census hits share a suggestive structural feature: each is
`K_n-H` for a spanning deleted graph `H` of maximum degree at most two. This is
not a characterization. In particular `K_6-C_6` has the same broad form but
does not appear as a reversal in the exploratory census range.

## 8. Verification architecture

There are three layers:

1. `full_eq59_from_definitions.py`: independent construction from the paper's
   Gram matrix/projector definitions and exhaustive Eq. 59 maximum;
2. `exact_permutation.py`: equivalent exact permutation-basis reduction using
   the locally derived two-site rule;
3. `exact_markov.py`: equivalent parity-conditioned heat-bath reduction.

The latter two are useful mutually checking implementations, but should be
called **equivalent representations**, not independent derivations.
