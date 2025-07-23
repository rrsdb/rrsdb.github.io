# $q$-series: notations, definitions, basic results

## The rising $q$-factorial, or $q$-shifted factorial, or $q$-Pochhammer symbol {#q-Pochhammer}

For a positive integer $n$, the $q$-Pochhammer symbol is defined

$$ (a;q)_n := \prod_{k=0}^{n-1} (1-aq^k) $$

$$ (a;q)_{-n} := \prod_{k=1}^n \frac{1}{1-aq^{-k}} = \frac{(-1)^n q^{n(n+1)/2}}{a^n (q/a;q)_n} $$

with $(a;q)_0 = 1$. For complex $\vert q \vert < 1$,

$$ (a;q)_\infty := \prod_{k=0}^\infty (1-aq^k) $$

and for real $n$,

$$ (a;q)_n := \frac{(a;q)_\infty}{(aq^n;q)_\infty}. $$

For positive integers $r$ and $n \in \mathbb{Z} \cup \{\infty\}$,
the product of $q$-Pochhammer symbols is written

$$ (a_1, a_2, a_3, \dots, a_r; q)_n = \prod_{k=1}^r (a_k;q)_n. $$


## The $q$-binomial coefficient {#q-binomial}

The **Gaussian polynomial**, or the $q$-**binomial coefficient**, is given by

$$ \left[ \genfrac{}{}{0pt}{}{n}{k} \right]_q := \frac{(q;q)_n}{(q;q)_k(q;q)_{n-k}}, $$

when $0 \leq k \leq n$ and $0$ otherwise. A nonzero $q$-binomial coefficient is a polynomial of degree $k(n-k)$.

$$ \left[ \genfrac{}{}{0pt}{}{n}{k} \right]_q = \sum_{j = 0}^{k(n-k)} p_{k,n-k}(j) q^j, $$

where $p_{k,n-k}(j)$ denotes the number of partitions of $j$ of length at most $k$ and parts no greater than $n-k$.


## $q$-hypergeometric series {#q-hypergeometric}

A **basic hypergeometric series** with base $q$, also called a $q$-hypergeometric series, is given by

$$ { {}_{r}\phi_{s} \left[ \genfrac{}{}{0pt}{}{a_1, a_2, \dots, a_r} {b_1, b_2, \dots, b_s} ; {q},{z} \right]} := \sum_{k=0}^\infty \frac{(a_1, a_2, \dots, a_r; q)_k }{(q;q)_k (b_1, b_2, \dots, b_s;q)_k} z^k \left( (-1)^k q^{k(k-1)/2} \right)^{1+s-r}, $$

where $r$ and $s$ are nonnegative integers.

A basic hypergeometric series is **balanced** (or Saalschützian in the older literature) if $r=s+1$ and $a_1 a_2 \cdots a_{s+1} = q b_1 b_2\cdots b_s$, and **well-poised** if $r=s+1$ and there exists a permutation of the numerator parameters so that $a_1 q = a_2 b_1 = \cdots = a_{s+1} b_s$. A well-poised hypergeometric series **very well-poised** if additionally $a_2 = -a_3 = q\sqrt{a}$.

The **bilateral basic hypergeometric series** with base $q$ is

$$ { {}_{r}\psi_{s} \left[ \genfrac{}{}{0pt}{}{a_1, a_2, \dots, a_r} {b_1, b_2, \dots, b_s} ; {q},{z} \right]} := \sum_{k=0}^\infty \frac{(a_1, a_2, \dots, a_r; q)_k }{(b_1, b_2, \dots, b_s;q)_k} z^k \left( (-1)^k q^{k(k-1)/2} \right)^{s-r}, $$

where $r$ and $s$ are nonnegative integers.

See [here](fundamental_q-hypergeometric_sums.html) for a list of some notable $q$-hypergeometric summation identities.


## Ramanujan's theta functions {#theta_functions}

Ramanujan's **theta function** is given by the infinite series

$$ f(a,b) := \sum_{n=-\infty}^\infty a^{n(n+1)/2} b^{n(n-1)/2}. $$

Using the [triple product identity](#triple_product), we can also write

$$ f(a,b) = (-a, -b, ab; ab)_\infty. $$

Ramanujan defined three special cases of $f(a,b)$ as follows:

$$ \varphi(q) := f(q,q) = \frac{(-q;-q)_\infty}{(q;-q)_\infty}, $$
$$ f(-q) :=  f(-q, -q^2) = (q;q)_\infty, $$
$$ \psi(q) := f(q,q^3) = \frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}. $$

Note that the reciprocals of the three functions above are important as generating functions:

$$ \frac{1}{\varphi(-q)} = \frac{(-q;q)_\infty}{(q;q)_\infty} = \sum_{n=0}^\infty \bar{p}(n) q^n, $$
$$ \frac{1}{f(-q)} = \frac{1}{(q;q)_\infty} = \sum_{n=0}^\infty p(n) q^n , $$
$$ \frac{1}{\psi(-q)} =  \frac{(-q;q^2)_\infty}{(q^2;q^2)_\infty} \sum_{n=0}^\infty pod(n) q^n, $$

where $p(n)$ is the number of [unrestricted partitions](partitions.html#integer_partitions) of $n$, $\bar{p}(n)$ is the number of [overpartitions](partitions.html#overpartitions) of $n$, and $pod(n)$ is the number of partitions of $n$ in which no odd part is repeated. 


## The triple product identity {#triple_product}

Jacobi's (1829) **triple product identity** appears in the literature in many different forms. In terms of [Ramanujan's theta function](#theta_functions), it is given by

$$ f(a,b) = (-a, -b, ab; ab)_\infty, $$

where $|ab|<1.$ In the context of Rogers-Ramanujan type identities, we often encounter the triple product identity in the forms

$$ \sum_{n=-\infty}^\infty (-1)^n q^{\frac a2 n^2 - \frac b2 n} = (q^{(a-b)/2}, q^{(a+b)/2}, q^a; q^a)_\infty $$
$$ \sum_{n=-\infty}^\infty q^{\frac a2 n^2 - \frac b2 n} = (-q^{(a-b)/2}, -q^{(a+b)/2}, q^a; q^a)_\infty $$

for positive integers $a > b$, where $\vert q \rvert < 1$.


## The quintuple product identity {#quintuple_product}

The **quintuple product identity** has been discovered and re-discovered many times. See Cooper (2006) for a comprehensive history the identity. The first explicit appearance in the literature seems to be Fricke (1916), although Ramanujan independently discovered it around the same time and made use of many special cases. A form that is particularly useful in the context of Rogers—Ramanujan type identities is as follows:

$$ Q(w,x) := f(-wx^3, -w^2 x^{-3}) + x f(-wx^{-3},-w^2 x^3) = (-w/x, -x, w; w)_\infty (w/x^2, wx^2; w^2)_\infty, $$

where $w$ and $x$ are each equal to $ \pm q^{m} $ for some positive integer or half-integer $ m $ and $ |q| < 1 $ to ensure convergence. Another form of the quintuple product identity is

$$ (z^{-1},zq,q; q)_\infty (z^{-2}q, z^2q; q^2)_\infty =\sum_{n=-\infty}^\infty q^{n(3n+1)/2} ( z^{3n} - z^{-3n-1}), $$

where $z\neq 0$ and $|q|<1$.


## Bailey's triple product dissection {#dissection}

Bailey (1951) gives another identity that allows a sum of certain theta functions into a single theta function.  Equivalently, it dissects a theta function into even and odd parts:

$$ f(z^2 q, z^{-2} q^3) + z f(z^2 q^3, z^{-2}q) = f(z, q/z). $$


## Polygonal number identities {#polygonal_number_identities}

Euler's pentagonal number theorem is

$$ f(-q) = (q;q)_\infty = \sum_{n=-\infty}^\infty (-1)^n q^{n(3n-1)/2}. $$

Gauss's square number and hexagonal number theorems are, respectively

$$ \varphi(-q) = \frac{(q;q)_\infty}{(-q;q)_\infty} = \sum_{n=-\infty}^\infty (-1)^n q^{n^2} $$

and

$$ \psi(-q) = \frac{(q^2;q^2)_\infty}{(-q;q^2)_\infty} = \sum_{n=-\infty}^\infty (-1)^n q^{2n^2-n}. $$


## References

- W. N. Bailey (1951) On the simplification of some identities of Rogers—Ramanujan type, Proc. London Math. Soc. s3-1, 217—221. [DOI](https://doi.org/10.1017/CBO9780511526251) 
- S. Cooper (2006) The quintuple product idenitity, Int. J. Number Theory 2, 115—161. [DOI](https://doi.org/10.1142/S1793042106000401)
- R. Fricke (1916) Die Elliptischen Funktionen und ihre Anwendungen (Erste Teil, Teubner, Leipzig).
- G. Gasper and M. Rahman (2004) Basic Hypergeometric Series, 2nd ed., Encyclopedia of Mathematics and its Applications vol. 96, Cambridge University Press, Cambridge. [DOI](https://doi.org/10.1017/CBO9780511526251)
- C. G. J. Jacobi (1829) Fundamenta Nova Theoriae Functionum Ellipticarum (in Latin), Borntraeger: Königsberg. [Internet Archive](https://archive.org/details/fundamentanovat00jacogoog/mode/)
