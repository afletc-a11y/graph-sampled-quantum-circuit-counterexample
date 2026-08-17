# Status

Date: 2026-08-17

## Primary proved counterexample

For graph-sampled Haar-random two-qubit circuits on six qubits, in the paper's
multiplicative-error metric at `q=t=2`, let `O_6=K_{2,2,2}` be the octahedron
(`K_6` with a perfect matching removed). Then

\[
s_{5/6}(O_6)=9,\qquad s_{5/6}(K_6)=10.
\]

The adjacent exact values are

\[
\begin{aligned}
M_{O_6}(8)&=\frac{347115007}{303750000},\\
M_{O_6}(9)&=\frac{7432619383}{9112500000},\\
M_{K_6}(9)&=\frac{18928429830211}{22247314453125},\\
M_{K_6}(10)&=\frac{5197395863758829}{8342742919921875}.
\end{aligned}
\]

They satisfy

\[
M_{O_6}(8)>\frac56>M_{O_6}(9),\qquad
M_{K_6}(9)>\frac56>M_{K_6}(10).
\]

The exact depth-9 reversal interval is

\[
\left[
\frac{7432619383}{9112500000},
\frac{18928429830211}{22247314453125}
\right)
\]

with width

\[
\frac{8345455089959}{237304687500000}.
\]

## Exact finite-depth comparison

Exact rational evaluation through `s=45` gives

\[
M_{O_6}(s)<M_{K_6}(s)
\quad\Longleftrightarrow\quad
s\in\{6,7,8,9,10,11,12,13,14,15\}
\]

within that checked range. At `s=16` the inequality reverses exactly.

The maximizing diagonal experiment for both graphs is the all-sign experiment
(bitmask `63`, Hamming weight `6`) throughout `s=6,...,16`. Thus the crossover
at `15 -> 16` is not caused by a switch of maximizing Hamming weight.
Interpretations in terms of an "elbow" or "anarchy" mechanism should remain
interpretive unless separately derived from the spectrum/dynamics.

## Independent from-definition audit

`verify/full_eq59_from_definitions.py` does not use the heat-bath transition,
Walsh conjugation, or a hand-inserted `2/5` coefficient. It:

1. constructs the full permutation-state Gram matrix;
2. constructs each edge moment operator by solving for the `G`-orthogonal
   projector onto the equality subspace;
3. constructs the global Haar projector;
4. explicitly converts the coordinate action to the coefficient matrix used
   by Eq. 59; and
5. exhaustively maximizes Eq. 59 over all `4096` `(a,b)` pairs.

For both `O_6` and `K_6`, the full Eq. 59 maximum equals the diagonal maximum at
every audited depth `s=6,...,16`, as predicted by the paper's PSD diagonal
argument.

## Earlier secondary witness

The original certificate remains correct:

\[
s_{3/13}(K_{3,3})=14<15=s_{3/13}(K_6).
\]

However, `K_{3,3}` beats `K_6` only at `s=14` through `s=45`. At `s=14`, the
octahedron's epsilon window is wider by the exact factor

\[
\frac{83556125512633375224389442711}
     {52457551975595363824242958336}
\approx1.5928331073.
\]

## Additional exact finite witnesses

The exploratory census also led to two seven-vertex witnesses, subsequently
checked in exact rational arithmetic:

\[
M_{K_7-C_7}(s)<M_{K_7}(s)\quad\text{for }s=6,\ldots,14,
\]

and

\[
M_{K_7-(C_3\sqcup C_4)}(s)<M_{K_7}(s)
\quad\text{for }s=12,13,14,
\]

within the exact checked range through `s=15`. For `K_7-C_7`, the widest
sub-1 interval occurs at `s=11`:

\[
\left[
\frac{12179988456128649}{13792736767578125},
\frac{2427499625871482657}{2585547026630859375}
\right),
\]

with exact width

\[
\frac{5049582644841826906}{90494145932080078125}
\approx0.0558001028.
\]

This interval is about `1.5867x` as wide as the octahedron's widest sub-1
interval. The octahedron remains the primary witness because it already occurs
at `n=6`, admits the particularly clean `epsilon=5/6` threshold certificate,
and continues beating `K_6` down to substantially smaller multiplicative
errors (its `s=15` lower endpoint is about `0.189`, compared with about `0.432`
for `K_7-C_7` at `s=14`).

At `n=8`, an exact reduced calculation verifies that the cocktail-party graph
(`K_8` minus a perfect matching) satisfies

\[
M_{CP_8}(s)<M_{K_8}(s)\quad\text{for }s=6,\ldots,16,
\]

and loses again at `s=17`. The `n=8` checker explicitly compares the Markov
and permutation-basis reductions at `s=6,16,17`; this system size therefore no
longer rests on a single unchecked reduced representation.

All of these are recorded as finite supporting evidence only. No general
cocktail-party or deletion-family theorem is claimed.

## Equivalent reduced representations

The heat-bath and nonorthogonal permutation-basis evaluators agree exactly on
the cross-check suite. They are equivalent reductions of the same calculation,
not independent derivations. The separate from-definition Eq. 59 checker is
the independent audit.

## Exploratory only

The NetworkX/NumPy graph census is candidate-generation code, not part of the
proof. Among the four `n=6,7` candidates it returns, every graph can be written
as `K_n-H` where `H` is spanning and has maximum degree at most two:

- `K_6` minus a perfect matching;
- `K_6-(C_3\sqcup C_3)=K_{3,3}`;
- `K_7-C_7`;
- `K_7-(C_3\sqcup C_4)`.

This is only a search heuristic, not a characterization. The simplest converse
already fails in the same census: `K_6-C_6` (the triangular prism) is also the
complement of a spanning 2-regular graph but is not returned as a complete-
graph reversal in the searched range.

Numerical spectral observations suggest `K_6` has the better long-time decay
rate; the exact primary certificate itself only needs the finite-depth values.

## Not addressed

- A general cocktail-party-graph theorem.
- Whether complete-graph extremality can be repaired for all sufficiently
  small `epsilon` in a clean theorem.
- The smallest possible counterexample over every `epsilon`.
- Conjecture 4's newer `q=15` and `q=29` candidates, which still require the
  same independent full-Eq.-59 audit before repackaging.
