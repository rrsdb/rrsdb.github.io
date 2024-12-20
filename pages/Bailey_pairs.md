# Bailey Pairs & Bailey's lemma

## Definition {#definition}

A pair of sequences of functions $(\alpha_n(a,q),\beta_n(a,q))$ form a **Bailey pair relative to $a$** if

$$ \beta_n(a, q) = \sum_{r=0}^n \frac{\alpha_r(a,q)}{(q;q)_{n-r}(aq;q)_{n+r}} $$

holds for all integers $n \geq 0$.

An alternative form, often useful for computations, is given by

$$ \beta_n(a,q) = \frac{1}{(q;q)_n (aq;q)_n} \sum_{r=0}^n \frac{(q^{-n};q)_r}{(aq^{n+1};q)_r} (-1)^r q^{nr -r(r-1)/2} \alpha_r(a,q). $$

One could also invert and express $\alpha_n$ in terms of $\beta$:

$$ \alpha_n (a,q) = \frac{1-aq^{2n}}{1-a} \sum_{j=0}^n \frac{ (a;q)_{n+j} (-1)^{n-j} q^{(n-j)(n-j-1)/2}}{(q;q)_{n-j}} \beta_j(a,q). $$

The preceeding is equivalent to

$$ \alpha_n (a,q) = (-1)^n q^{n(n-1)/2} \frac{(1-aq^{2n})}{1-a} \frac{(a;q)_n}{(q;q)_n} \sum_{j=0}^n (aq^n;q)_j (q^{-n};q)_j q^j \beta_j(a,q). $$


## The strong Bailey lemma {#strong_Bailey_lemma}

If $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a [Bailey pair](#definition) relative to $a$, then

$$
\frac{1}{(aq/\rho_1, aq/\rho_2;q)_n } \sum_{j=0}^n  \frac{(\rho_1,\rho_2;q)_j (\frac{aq}{\rho_1 \rho_2} ;q)_{n-j} }{(q;q)_{n-j} } \left( \frac{aq}{\rho_1 \rho_2}  \right)^j \beta_j(a,q) 
= \sum_{r=0}^n \frac{(\rho_1,\rho_2;q)_r }{(q;q)_{n-r} (aq;q)_{n+r} (aq/\rho_1, aq/\rho_2;q)_r } \left( \frac{aq}{\rho_1 \rho_2}  \right)^r \alpha_r(a,q).
$$

Equivalently, if $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a [Bailey pair](#definition) relative to $a$, then so does $\big(\alpha'_n(a,q), \beta'_n(a,q)\big)$, where

$$ \alpha'_r(a,q) = \frac{(\rho_1,\rho_2;q)_r}{(aq/\rho_1, aq\rho_2;q)_r} \left( \frac{aq}{\rho_1 \rho_2} \right)^r \alpha_r(a,q) $$

and

$$ \beta'_n(a,q) = \frac{1}{(aq/\rho_1, aq/\rho_2;q)_n} \sum_{j=0}^n \frac{(\rho_1,\rho_2;q)_j ( \frac{aq}{\rho_1 \rho_2} ;q)_{n-j} } {(q;q)_{n-j} } \left( \frac{aq}{\rho_1 \rho_2}   \right)^j \beta_j(a,q). $$

This latter formulation gives rise to the **Bailey chain**, as every Bailey pair immediately implies infinitely many others: see  Andrews (1984).


### The first op-Bailey lemma {#1st_op_Bailey_lemma}

The **first op-Bailey lemma** is a limiting case ($\rho_2, n\to\infty, \rho_1 =-{1},$ with $a$ specialized) of the [strong Bailey lemma](#strong_Bailey_lemma) and is so named because the infinite product prefactor on the righthand side is the generating function for $\overline{p}(n)$, the number of [overpartitions](partitions.html#overpartitions) of $n$.

If $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a [Bailey pair](#definition) relative to $a=1$, then

$$ \sum_{n=0}^\infty q^{n(n+1)/2} (-1;q)_n \beta_n(1,q) = 2\frac{(-q;q)_\infty}{(q;q)_\infty}\sum_{r=0}^\infty \frac{ q^{r(r+1)/2}}{1+q^r} \alpha_r(1,q). $$

If \(a\) is unspecialized,

$$ \sum_{n=0}^\infty a^n q^{n(n+1)/2} (-1;q)_n \beta_n(a,q) = \frac{(-aq;q)_\infty} {(aq;q)_\infty} \sum_{r=0}^\infty \frac{a^r q^{r(r+1)/2} (-1;q)_r}{ (-aq;q)_r } \alpha_r(a,q), $$

Notice here that the prefactor on the right hand side is

$$ \frac{(-aq;q)_\infty}{(aq;q)_\infty} = \sum_{n=0}^\infty \sum_{m=0}^\infty  \overline{p}(n,m) a^m q^n, $$

where $\overline{p}(n,m)$ denotes the number of overpartitions of $n$ with length $m$.


### The second op-Bailey lemma {#2nd_op_Bailey_lemma}

The **second op-Bailey lemma** is the limiting case ($\rho_2, n\to\infty$, $\rho_1 = -q$, and $a=q$) of the [strong Bailey lemma](#strong_Bailey_lemma) and is so named because the infinite product prefactor on the righthand side is the generating function for $\overline{p}(n)$, the number of [overpartitions](partitions.html#overpartitions) of $n$.

If $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a [Bailey pair](#definition) relative to $a=q$, then

$$ \frac{1}{1-q}\sum_{n=0}^\infty q^{n(n+1)/2} (-q;q)_n \beta_n(q,q) = \frac{(-q;q)_\infty}{(q;q)_\infty} \sum_{r=0}^\infty  q^{r(r+1)/2} \alpha_r(q,q). $$


### The p-Bailey lemma {#p_Bailey_lemma}

The **p-Bailey lemma** is a limiting case ($\rho_1, \rho_2, n\to\infty$ with $a$ specialized) of the [strong Bailey lemma](#strong_Bailey_lemma) and is so named because of the infinite product prefactor on the righthand side is the generating function for $p(n)$, the number of [unrestricted partitions](partitions.html#integer_partitions) of $n$.

If $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a [Bailey pair](#definition) relative to $a=1$, then

$$ \sum_{n=0}^\infty q^{n^2} \beta_n(1,q) = \frac{1}{(q;q)_\infty} \sum_{r=0}^\infty q^{r^2} \alpha_r(1,q). $$

If $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a Bailey pair relative to $a=q$, then

$$ \sum_{n=0}^\infty q^{n^2+n} \beta_n(q,q) = \frac{1}{(q^2;q)_\infty} \sum_{r=0}^\infty q^{r^2+r} \alpha_r(q,q). $$

If $a$ is left unspecialized, we have the **ap-Bailey lemma**, also known in the literature as the [_weak Bailey lemma_](https://dlmf.nist.gov/17.12):

$$ \sum_{n=0}^\infty a^n q^{n^2} \beta_n(a,q) = \frac{1}{(aq;q)_\infty} \sum_{r=0}^\infty a^r q^{r^2} \alpha_r(a,q), $$

for any Bailey pair $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ relative to $a$.  Notice here that the prefactor on the right hand side is

$$ \frac{1}{(aq;q)_\infty} = \sum_{n=0}^\infty \sum_{m=0}^\infty p(n,m) a^m q^n, $$

where $p(n,m)$ denotes the number of partitions of $n$ of length $m$.


### The pod-Bailey lemma {#pod_Bailey_lemma}

The **pod-Bailey lemma** is a limiting case ($\rho_2, n\to\infty, \rho_1 = -\sqrt{q}$, with $a$ specialized, then $q$ replaced by $q^2$ throughout) of the [strong Bailey lemma](#strong_Bailey_lemma) and is so named because of the infinite product prefactor on the righthand side is the generating function for $pod(n)$, the number of partitions of $n$ in which no odd part is repeated. 

If $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a [Bailey pair](#definition) relative to $a=1$,  then

$$ \sum_{n=0}^\infty q^{n^2} (-q;q^2)_n \beta_n(1,q^2) = \frac{(-q;q^2)_\infty}{(q^2;q^2)_\infty} \sum_{r=0}^\infty q^{r^2} \alpha_r(1,q^2). $$


If$\big(\alpha_n(a,q), \beta_n(a,q)\big)$ form a Bailey pair relative to $a=q$, then

$$ \sum_{n=0}^\infty q^{n^2+2n} \beta_n(q^2,q^2) = \frac{(-q;q^2)_\infty}{(q^4;q^2)_\infty} \sum_{r=0}^\infty \frac{ q^{r^2+2r}}{1+q^{2r+1}} \alpha_r(q^2,q^2). $$


If $a$ is left unspecialized, we have the **apod-Bailey lemma**:

$$ \sum_{n=0}^\infty a^n q^{n^2} (-q;q^2)_n \beta_n(a,q^2) = \frac{(-aq;q^2)_\infty} {(aq^2;q^2)_\infty} \sum_{r=0}^\infty \frac{a^r q^{r^2} (-q;q^2)_r}{ (-aq;q^2)_r } \alpha_r(a,q^2), $$

for any Bailey pair $\big(\alpha_n(a,q), \beta_n(a,q)\big)$ relative to
$a$. Notice here that the prefactor on the right hand side is

$$ \frac{(-aq;q^2)_\infty}{(aq^2;q^2)_\infty} = \sum_{n=0}^\infty \sum_{m=0}^\infty pod(n,m) a^m q^n, $$

where $pod(n,m)$ denotes the number of partitions of $n$ of length $m$ in which no odd part is repeated.


## References

- G. E. Andrews (1984) Multiple series Rogers–Ramanujan type identities, Pacific J. Math. 114, 267–283. [Open Access](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-114/issue-2/Multiple-series-Rogers-Ramanujan-type-identities/pjm/1102708707.full)
- W. N. Bailey (1948) Identities of the Rogers–Ramanujan type, Proc. London Math. Soc. (2) 50, 1–10. [DOI](https://doi.org/10.1112/plms/s2-50.1.1)
