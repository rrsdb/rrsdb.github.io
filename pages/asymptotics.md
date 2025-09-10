# Asymptotics

A theorem of Meinardus (1954) provides an asymptotic formula for $r(n)$ when

$$ 1 + \sum_{n=1}^\infty r(n) q^n = \prod_{n=1}^\infty \frac{1}{(1-q^n)^{a_n}} $$

when the $a_n$ are nonnegative integers.  See Andrews (1976, Chapter 6) for an exposition in English. Todt (2011) strengthens Meinardus' result by showing that it can be extended to all real $a_n$ provided the $r(n)$ are a nondecreasing function of $n$. It is further conjectured that Meinardus' result would still hold for real $a_n$ if the $r(n)$ were *eventually* nondecreasing, but this has not been established rigorously.  The Meinardus asymptotic, as $ n\to\infty $, is

$$ r(n) \sim C n^\kappa \exp\left\{ n^{\alpha/(\alpha+1)} \left( 1 + \frac{1}{\alpha} \right) [A \Gamma(\alpha+1) \zeta(\alpha+1)]^{1/(\alpha+1)} \right\} , $$

where $\zeta(s)$ is the Riemann zeta-function, $\Gamma(s)$ is Euler's gamma function,

$$ C =  e^{D'(0)} (2\pi(1+\alpha))^{-1/2} \left( A\Gamma(\alpha+1)\zeta(\alpha+1) \right)^{(1-2D(0))/(2+2\alpha)} ,$$
$$ \kappa =  \frac{2D(0)-2-\alpha}{2(1+\alpha)}, $$
$$ D(s) = \sum_{n=1}^\infty \frac{a_n}{n^s}, $$

convergent for $\Re s>\alpha$, and possessing an analytic continuation to $\Re s\geq -C_0,$ (for some $C_0$ between 0 and 1) and that in this region $D(s)$ is analytic except for a simple pole at $s = \alpha$ with residue $A$.

For the infinite product with signature $m: (a_1, a_2, \dots, a_m)$, if the $a_j$ have the symmetry property that $a_j = a_{m-j}$ for $j = 1, 2, \dots, m-1$, the Meinardus asymptotic simplifies to

$$ r(n) \sim \frac{m^{a_m/2}}{2^{1+m\bar{\mathbf{a}}/2}} 
      \left( \frac{\bar{\mathbf{a}}}{6} \right)^{(1+a_m)/4} 
      \prod_{j=1}^{\lfloor (m-1)/2 \rfloor} \mathrm{csc}^{a_j} \left( \frac{j\pi}{m}  \right)
      n^{-(a_m+3)/4} \exp\left( \pi \sqrt{ \frac{2n\bar{\mathbf{a}}}{3}} \right) $$

as $n \to \infty$; see Sills (2018, p. 97, Cor. 2.58). Here $\bar{\mathbf{a}} := \frac{1}{m} \sum_{i=1}^m a_i$. 

## References

- G. E. Andrews (1976), The Theory of Partitions, Encyclopedia of Mathematics and its Applications, vol. 2, Addison–Wesley: Reading, MA.  Reissued, Cambridge University Press, 1998. [DOI](https://doi.org/10.1017/CBO9780511608650)
- G. Meinardus, Asymptotosche aussagen über Partitionen (1954) Math. Z. 59, 388—398. [DOI](https://doi.org/10.1007/BF01180268)
- A. V. Sills, An Invitation to the Rogers—Ramanujan Identities (2018) CRC Press: Boca Raton, FL. [Publisher's page](https://www.routledge.com/An-Invitation-to-the-Rogers-Ramanujan-Identities/Sills/p/book/9780367657611)
- H. Todt (2011), Asymptotics of Partition Functions, Ph.D. dissertation, Pennsylvania State University. [PDF](https://etda.libraries.psu.edu/files/final_submissions/2280")
