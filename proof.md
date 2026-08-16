# Exact counterexample to complete-graph gate-count extremality

## Theorem

Let each step choose an edge uniformly from a connected graph on six qubits
and apply an independent Haar-random two-qubit unitary.  Let `M_G(s)` be the
multiplicative error of the second-moment channel after `s` gates relative to
the global Haar second moment, and let

\[
s_\epsilon(G)=\min\{s:M_G(s)\leq\epsilon\}.
\]

Then

\[
s_{3/13}(K_{3,3})=14<15=s_{3/13}(K_6).
\]

Consequently Conjecture 3 of arXiv:2510.23726v2 is false as stated.

## 1. Exact `t=2,q=2` transfer operator

Use the paper's local permutation states `|0>` and `|1>` for the identity and
swap.  Their Gram matrix at `q=2` is

\[
B=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
\]

On an edge, the Haar second moment is the orthogonal projector onto the span
of `|00>` and `|11>`.  Projecting the two mixed basis states with the Gram
matrix gives

\[
G|00\rangle=|00\rangle,\qquad G|11\rangle=|11\rangle,
\]

\[
G|01\rangle=G|10\rangle=\frac25(|00\rangle+|11\rangle).
\]

Indeed, both overlaps of `|01>` with `|00>,|11>` are `1/2`, while the Gram
matrix of `|00>,|11>` is

\[
\begin{pmatrix}1&1/4\\1/4&1\end{pmatrix};
\]

multiplication by its inverse gives coefficients `(2/5,2/5)`.

For a graph with `m` edges the one-gate transfer operator is exactly

\[
H_G=\frac1m\sum_{e\in E(G)}G_e.
\]

## 2. Walsh conjugation gives a heat-bath chain

Let `W_2` be the order-four Walsh matrix, with columns
`((-1)^{a\cdot x})_x`.  Direct exact multiplication gives

\[
\frac14W_2GW_2=
\begin{pmatrix}
9/10&0&0&1/10\\
0&1/2&1/2&0\\
0&1/2&1/2&0\\
9/10&0&0&1/10
\end{pmatrix}.
\]

Read as a row transition matrix, an updated edge obeys the rule

- equal endpoint bits: replace them by `00` with probability `9/10` and by
  `11` with probability `1/10`;
- unequal endpoint bits: replace them by `01` or `10`, each with probability
  `1/2`.

Let `K_G` be the average of this update over the graph's edges.  It preserves
the parity of the number of one-bits.  Within the parity class of a state
`a` of Hamming weight `k`, its stationary probability is

\[
\pi(a)=\frac{3^{n-k}}{2^{n-1}(2^n+(-1)^k)}. \tag{1}
\]

This follows either by detailed balance or by summing the product weights
`3^{n-k}` separately over even and odd `k`:

\[
\sum_{k\equiv p\pmod2}\binom nk3^{n-k}
=2^{n-1}(2^n+(-1)^p).
\]

## 3. Identification with multiplicative error

For an experiment `a`, let `w_a(x)=(-1)^{a\cdot x}`.  The paper's cobasis
state is

\[
|\Psi(a)\rangle=\bigotimes_i(|\widetilde0\rangle
 +(-1)^{a_i}|\widetilde1\rangle).
\]

The inverse single-site Gram matrix is

\[
B^{-1}=\begin{pmatrix}4/3&-2/3\\-2/3&4/3\end{pmatrix}.
\]

Thus the left boundary coordinates are `w_a`, while the right boundary
coordinates are

\[
\frac{2^n}{3^{n-k}}w_a.
\]

Walsh conjugation now gives

\[
\langle\Psi(a)|H_G^s|\Psi(a)\rangle
=\frac{2^{2n}}{3^{n-k}}K_G^s(a,a). \tag{2}
\]

Equation (68) of the source paper gives the corresponding global-Haar value

\[
\langle\Psi(a)|H_{\rm Haar}|\Psi(a)\rangle
=\frac{2}{1+(-1)^k2^{-n}}. \tag{3}
\]

Dividing (2) by (3), and applying the paper's Theorem 1, yields the exact
classical formula

\[
M_G(s)=\max_{a\in\{0,1\}^n}
\left(\frac{K_G^s(a,a)}{\pi(a)}-1\right). \tag{4}
\]

No spectral-gap substitution or anticoncentration approximation appears in
(4); it is the full multiplicative error.

Each edge update is a heat-bath projection in `L^2(pi)`.  Hence `K_G` is a
positive-semidefinite self-adjoint contraction.  Its spectral expansion shows
that every quantity in parentheses in (4), and therefore their maximum, is
nonincreasing in `s`.  This justifies identifying the exact threshold from
two adjacent gate counts.

## 4. Integer certificate

For a graph with `m` edges, define the integer matrix `Q_G=10m K_G`.  One row
step is implemented without any division:

- for each selected equal-bit edge, add weights `9` and `1` to the `00` and
  `11` successors;
- for each selected unequal-bit edge, add weights `5` and `5` to the two
  orientations.

Therefore

\[
K_G^s(a,a)=\frac{Q_G^s(a,a)}{(10m)^s},
\]

and (1)--(4) are evaluated using integers and rational arithmetic only.  Full
enumeration of all 64 states gives

\[
\begin{array}{c|c|c}
G&s&M_G(s)\\ \hline
K_{3,3}&13&274339976596040821/919366980732421875\\
K_{3,3}&14&79546639693547185219/344762617774658203125\\
K_6&14&61323079873072938701309/263969600200653076171875\\
K_6&15&752104047129764606918347/3959544003009796142578125
\end{array}
\]

Subtracting `3/13` gives, respectively,

\[
\frac{808318753551265048}{11951770749521484375}>0,
\]

\[
-\frac{181537307861201528}{4481914031070556640625}<0,
\]

\[
\frac{5291237747988974601392}{3431604802608489990234375}>0,
\]

\[
-\frac{2101279396342448537795864}{51474072039127349853515625}<0.
\]

The claimed gate counts follow by monotonicity.  The file
`verify/verify_counterexample.py` reconstructs every displayed rational and
checks every inequality.
