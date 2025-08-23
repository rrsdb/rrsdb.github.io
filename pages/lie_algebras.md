
# Specializations of characters of affine Lie algebras

## Notation

An affine Kac--Moody Lie algebra $\la{g}$ is characterized by its affine Dynkin diagram. Such Dynkin diagrams fall into seven infinite families $A_n^{(1)} (n\geq 1)$, $B_n^{(1)} (n\geq 3)$, $C_n^{(1)} (n\geq 2)$, 
$D_n^{(1)} (n\geq 4)$, $A_{2n}^{(2)} (n\geq 1)$, $A_{2n-1}^{(2)} (n\geq 3)$,  $D_{n+1}^{(1)} (n\geq 2)$, and then we also have seven members
$E_6^{(1)}, E_7^{(1)}, E_8^{(1)}, F_4^{(1)}, G_2^{(1)}, E_6^{(2)}, D_4^{(3)}$ which do not fall into these families.


The nodes of these affine Dynkin diagrams are numbered $0,1,\cdots, r$ as in the given figures (\sk{Todo: add affine Dynkin diagrams}). To each node $i$ in a Dynkin diagram is associated a number called its comark denoted by $c_i$, a simple root $\alpha_i$, and a fundamental weight $\Lambda_i$.

We will be considering characters of standard (i.e., integrable highest-weight modules) for $\la{g}$. These modules are necessarily irreducible. Further, (upto isomorphisms) these modules are characterized by their highest weight $\lambda$ of the form:
$$ \begin{aligned}
\lambda = j_0\Lambda_0 + j_1\Lambda_1+\cdots+j_r\Lambda_r,
\end{align}
with $j_0,j_1,\cdots, j_r\in\ZZ_{\geq 0}$. We will denote the corresponding standard module by $L(\lambda)$.
The level of the module $L(\lambda)$ (or the highest weight $\lambda$) is the number
\begin{align}
    \ell = j_0 c_0 +\cdots j_r c_r,
\end{aligned}
$$
where we recall that $c_0,\cdots, c_r$ are the comarks for $\la{g}$.

## Example

Upto isomorphisms, there are $\ell+1$ $(\ell\in\ZZ_{\geq 0})$ standard modules for $A_1^{(1)}$ of level $\ell$, with highest weights given as:
$$ \begin{aligned}
a\Lambda_0 + b\Lambda_1,\quad (a+b=\ell, a,b\in\ZZ_{\geq 0}).
\end{aligned}
$$

## Example

Upto isomorphisms, there are two standard modules for $A_2^{(2)}$ of level $3$, with highest weights given as:
$$\begin{aligned}
\Lambda_0+\Lambda_1,\quad 3\Lambda_1.
\end{align}$$

## Example

Upto isomorphisms, there are three standard modules for $D_4^{(3)}$ of level $3$, with highest weights given as:
$$\begin{aligned}
3\Lambda_0,\quad \Lambda_0+\Lambda_1,\quad \Lambda_2.
\end{aligned}$$

## Principally specialized characters

Given a standard module $L(\lambda)$, its character is an object in the formal power series ring:
\begin{align}
\ch(L(\lambda)) \in e^{\lambda}\ZZ[[e^{-\alpha_0}, \cdots, e^{-\alpha_r}]].
\end{align}
Principal specialization of the ring $\ZZ[[e^{-\alpha_0},\cdots,e^{-\alpha_r}]]$ is the homomorphism uniquely determined by
$$\begin{aligned}
\prspec: \ZZ[[e^{-\alpha_0},\cdots,e^{-\alpha_r}]] \rightarrow \ZZ[[q]] \notag\\
e^{-\alpha_0}\mapsto q, e^{-\alpha_1}\mapsto q,\cdots, e^{-\alpha_r}\mapsto q,\notag
\end{aligned}$$
where $q$ is a formal variable.

We will consider principally specialized characters, which we obtain as
$$\prspec(e^{-\lambda}\ch(L(\lambda))).$$


Several sources in the literature provide explicit evaluations of principally specialized characters,
some of which have been compiled in \cite{Sil-book}.
The following may not be the original sources which give these formulas. 

Recall the standard $q$-series notation:
$$\begin{aligned}
(a;b)_j &= (1-a)(1-ab)\cdots (1-ab^{j-1}),\\
(a_1,a_2,\cdots,a_k;b)_j &= (a_1;b)_j(a_2;b)_j\cdots(a_k;b)_j,\\
\theta(a;b) &= (a;b)_{\infty}(b/a;b)_\infty,\\
\theta(a_1,a_2,\cdots,a_k;b) &= \theta(a_1;b)\theta(a_2;b)\cdots\theta(a_k;b).
\end{aligned}$$

We then have:
1. Type $A_n^{(1)}$. Given $\lambda = j_0\Lambda_0+\cdots+j_n\Lambda_n$ with $j_0,\cdots,j_n\in \ZZ_{\geq 0}$ and $\ell=j_0+\cdots+j_n$,  consider a sequence of integers $\mu_0,\cdots, \mu_n$ such that:
$$\begin{aligned}
\mu_0-\mu_1 = j_0,\,\, \mu_1-\mu_2=j_1,\,\,\cdots,\,\, \mu_n=j_n.
\label{eqn:lambdamuAC}
\end{aligned}$$
Then,
% \begin{align}
% \prch(L(\lambda))=\dfrac{(q^{n+1};q^{n+1})_\infty(q^{n+\ell+1};q^{n+\ell+1})^{n}_{\infty}}{(q)_\infty^{n+1}}\prod_{\substack{1\leq a\leq n\\0\leq b\leq n}}
% (q^{j_b+j_{b+1}+\cdots+j_{a+b-1}+a};q^{n+\ell+1})_\infty,
% \end{align}
$$\begin{aligned}
\prspec(e^{-\lambda}\ch(L(\lambda)))=\dfrac{(q^{n+1};q^{n+1})_\infty(q^{n+\ell+1};q^{n+\ell+1})^{n}_{\infty}}{(q)_\infty^{n+1}}\prod_{\substack{0\leq a<b\leq n}}
 \theta(q^{\mu_a-\mu_b-a+b};q^{n+\ell+1}),
 \end{aligned}$$
This formula can be deduced by combining \cite[Eq.\ 5.2]{AndSchWar} with \cite[Eq.\ 5]{FodWel}.

2. Type $C_n^{(1)}$. Given $\lambda = j_0\Lambda_0+\cdots+j_n\Lambda_n$ with $j_0,\cdots,j_n\in \ZZ_{\geq 0}$, define $\mu$'s as in \eqref{eqn:lambdamuAC}.
Further define $\kappa = 2n+2\mu_0+2$.
Then, we have:
$$\begin{aligned}
\prspec(e^{-\lambda}\ch(L(\lambda)))&=
\dfrac{(q^2;q^2)_\infty(q^{\kappa/2};q^{\kappa/2})_\infty(q^\kappa;q^\kappa)^{n-1}_\infty}{(q)_\infty^{n+1}}\notag\\
&\times\prod_{a=1}^n\theta(q^{\mu_a+n-a+1};q^{\kappa/2})
\prod_{1\leq a<b\leq n}\theta(q^{\mu_a-\mu_b-a+b};q^{\kappa})
\theta(q^{\mu_a+\mu_b+2n+2-a-b};q^{\kappa}).
\end{aligned}$$
This formula can be found as \cite[Eq.\ 3.19]{GriOnoWar}

3. Type $D_n^{(1)}$. This description is provided in \cite{Sil-book}. Needs to be typed.

4. Type $A_{2n}^{(2)}$. This description could be extracted from \cite{ButKozPri}, but will need a lot more work to figure out and type.

5. Type $D_{n+1}^{(2)}$. This description could be extracted from \cite{ButKozPri}, but will need a lot more work to figure out and type.

## Vacuum spaces

Lepowsky and Wilson, building on an earlier work of Lepowsky and Milne showed that the Rogers--Ramanujan identities reside in a certain substructure of the level $3$ standard modules for $A_1^{(1)}$. In general, this substructure is the vacuum space of $L(\lambda)$ with respect to the principal Heisenberg subalgebra of $\la{g}$.  We denote this by $\Omega(\lambda)$. This vacuum space also has a character which is then principally specialized to obtain infinite periodic products.

In general, we have 
$$\begin{aligned}
\prspec(e^{-\lambda}\ch(L(\lambda))) = F_\la{g} \cdot \prspec(e^{-\lambda}\ch(\Omega(\lambda))),
\end{aligned}$$
where $F_{\la{g}}$ is a factor that depends only on $\la{g}$ and not the module.

If $\la{g}$ is of the type $X_n^{(t)}$ where $X\in \{A,D,E\}$ and $t\in \{1,2,3\}$ as appropriate, then principally specialized characters of all the level $1$ standard modules coincide and equal the factor $F_\la{g}$. In these cases, we tabulate this factor as below.


## Example

Let $\lambda=j_0\Lambda_0+j_1\Lambda_1$ be a highest weight of a level $\ell=j_0+j_1$ standard module for $A_1^{(1)}$. Then, we have:
$$\begin{aligned}
\prspec(e^{-\lambda}\ch(\Omega(\lambda))) &=\dfrac{1}{F_{\la{g}}}\prspec(e^{-\lambda}\ch(L(\lambda)))\notag\\
&=\dfrac{(q;q)_\infty}{(q^2;q^2)_\infty}\times
\dfrac{(q^2;q^2)_\infty(q^{\ell+2};q^{\ell+2})_\infty}{(q)_\infty^{2}}
\theta(q^{j_1+1};q^{\ell+2})
=\dfrac{(q^{j_0+1},q^{j_1+1},q^{\ell+2};q^{\ell+2})_\infty}{(q)_\infty}.
\end{aligned}$$

