# Partitions and generalizations

## Integer partitions {#integer_partitions}

A **partition** of an integer $n$ is a representation of $n$ as a sum of positive integers where the order of the summands is not taken into account. Each summand is called a **part** of the partition. Usually, a convention is adopted wherein the parts are written in weakly decreasing (or sometimes weakly increasing) order. For example, the five partitions of 4 are

$$ 4,\; 3+1,\; 2+2,\; 2+1+1,\; 1+1+1+1.$$

To emphasize that the parts are to be kept separate from each other the five partitions of 4 are often written as

$$ (4),\;(3,1),\; (2,2),\; (2,1,1),\; (1,1,1,1), $$

or, if there is no chance of confusion, as

$$ 4,\; 31,\; 22,\; 211,\; 1111,$$ 

or employing superscripts to indicate repetitions:

$$4,\; 3 1\; ,2^2,\; 2 1^2,\; 1^4.$$

The number of parts in a partition $\lambda$ is called the **length**, and may be denoted $\ell(\lambda)$. The **size** (or **weight**) of a partition $\lambda$, denoted $\vert \lambda \vert$, is the sum of the parts, i.e. the number being partitioned.

The number of times $i$ appears as a part in the partition $\lambda$ is the **multiplicity** of $i$ in $\lambda$ and may be denoted $m_i(\lambda)$
   (or simply $m_i$ if there is no chance of confusion). The multiplicity-superscript representation of a partition is

$$ \lambda = \langle 1^{m_1}2^{m_2}3^{m_3}\cdots \rangle, $$

where $m_i$ is often omitted if $m_i=1$ and $i^{m_i}$ is omitted if $m_i=0$.

Notice that the sequence of multiplicities $ (m_1, m_2, m_3, \dots) $ completely determines any partition $\lambda$, with

$$ \ell(\lambda) = \sum_{i \geq 0} m_i(\lambda) $$
and

$$ \vert \lambda \vert = \sum_{i \geq 0} i\, m_i(\lambda). $$

The unique partition of $0$ is the empty partition $\emptyset$. The empty partition
is the only partition of length zero.

It is standard to let $p(n)$ denote the number of partitions of $n$. The generating
function for $p(n)$ was given by Euler:

$$ \sum_{n=0}^\infty p(n) q^n = \frac{1}{(q;q)_\infty}  = \frac{1}{f(-q)}. $$

## Partitions with $k$ colors {#colored_partitions}

A **partition with $k$ colors** of an integer $n$ is a representation of $n$ as a sum of weakly deceasing positive integers where summands of a particular magnitude may occur in $k$ different distinguishable varieties (or colors).  For example, while there are two partitions of $2$, namely $(2)$, and $(1,1)$, there are nine partitions of 2 in three colors:

$$(2_1), (2_2), (2_3), (1_1, 1_1), (1_1, 1_2), (1_1, 1_3), (1_2, 1_2), (1_2, 1_3), 
    (1_3, 1_3) , $$

where we have distinguished colors 1, 2, and 3 by subscripts.

$$ \sum_{n=0}^\infty p^k(n) q^n = \frac{1}{(q;q)^k_\infty}
= \frac{1}{f(-q)^k}, $$

where $p^k(n)$ denotes the number of $k$-colored partitions of $n$.

## Overpartitions {#overpartitions}

An **overpartition** of an integer $n$ is a representation of $n$ as a sum of weakly deceasing positive integers where the last occurrence of any particular positive integer may be optionally distinguished with an overline. For example, whereas there are three partitions of $3$, namely
    $(3)$, $(2,1)$, and $(1,1,1)$, there are eight overpartitions of 3:

$$ (3), (\overline{3}), (2,1), (\overline{2},1), (2,\overline{1}), 
    (\overline{2}, \overline{1}), (1,1,1), (1,1,\overline{1}). $$

Overpartitions were formally introduced by Corteel and Lovejoy (2004), and
have since accumulated a vast literature. There are many results related
to partitions that have natural analogs in overpartitions. As with partitions, the generating function for the number of overpartitions $\overline{p}(n)$ of $n$ is the reciprocal of a [Ramanujan theta function](../q-series.html#theta_functions), specifically,

$$ \sum_{n=0}^\infty \overline{p}(n) q^n = \frac{(-q;q)_\infty}{(q;q)_\infty} = \frac{1}{\varphi(-q)}. $$

## References

- G. E. Andrews (1976) The Theory of Partitions, Encyclopedia of Mathematics and its Applications, vol. 2, Addison–Wesley: Reading, MA. Reissued, Cambridge University Press, 1998. [DOI](https://doi.org/10.1017/CBO9780511608650)
- S. Corteel and J. Lovejoy (2004) Overpartitions, Trans. Amer. Math. Soc. 356, 1623–1635. [PDF](https://www.ams.org/journals/tran/2004-356-04/S0002-9947-03-03328-2/S0002-9947-03-03328-2.pdf)
