![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=mkAbmRLz_V6JAOazdrSMv|100%]]

$A \in \mathbb{R}^{m \times n}$
z.z. $Ker(A)$ ist ein Unterraum von $\mathbb{R}^{n}$

$\implies$ z.z. Nullvektor enthalten

(1)
$\forall_{v,w} \in Ker(A)$ gilt
$v+w \in Ker(A)$

(2)
$\forall_{\lambda \in \mathbb{R},v \in Ker(A)}:\Lambda  \cdot v \in Ker(A)$

Seien gegeben: $v,w \in Ker(A)$
$Ker(A) = \{x \in \mathbb{R}^{n};Ax=0\}$
$\implies A \cdot v=0 \land \mathbb{A} \cdot w=0$

Es gilt: $A(v+w)= Av + Aw = 0 \implies v+w \in Ker(A)$

z.z. $\forall_{x \in Ker(A),\lambda\in \mathbb{R}}:(\lambda \cdot x) \in Ker(A)$
$A(\lambda \cdot x) =\lambda  \cdot Ax =\lambda \cdot 0=0 \implies (\lambda \cdot x) \in Ker(A)$

$\blacksquare$
