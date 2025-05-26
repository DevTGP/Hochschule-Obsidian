![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=j2UlLKhhl0NXzGctE1Uds|100%]]

a)
z.z.
$\forall v,w \in U_{1} \cap U_{2} \implies v +w \in U_{1} \cap U_{2}$
$\forall v \in U_{1} \cap U_{2}, \forall\lambda \in \mathbb{R} \implies\lambda v \in U_{1} \cap U_{2}$

Def. 4.1

$U_{1} \cap U_{2}$ ist ein Unterraum

(1)
Es sei $U \in \mathbb{R}^{n}, U \neq \emptyset$
$0 \in \mathbb{R}^{n}$

4.1.1
(2) Addition
$\forall_{v,w \in U}$ gilt $v+w \in U$
gilt $v,w \in U_{1}$ und $v,w \in U_{2}$
daraus folgt $v+w \in U_{1}$ und $v+w \in U_{2}$
also muss gelten $v+w \in U_{1} \cap U_{2}$

4.1.2 Skalarmultiplikation
$\forall \lambda \in \mathbb{R}$ und $\forall v \in U$ gilt $\lambda v \in U$ | gilt für Unterraum

Folgt: $\forall\lambda \in \mathbb{R}$ und $\forall v \in U_{1} \cap U_{2}$
gilt $v \in U_{1}$ und $v \in U_{2}$

daraus folgt: $\lambda v \in U_{1}$ und $\lambda v \in U_{2}$
also muss gelten $\lambda v  \in U_{1} \cap U_{2}$
$\blacksquare$

b)
Für $x_{1} \in U_{1}\setminus U_{2}$ und $x_{2} \in U_{2} \setminus U_{1}$ ist $x_{1}+x_{2}\not\in U_{1} \cup U_{2}$

angenommen:
$x_{1}+ x_{2} \in U_{1}$, da $x_{1} \in U_{1}$, da $U_{1}$ ein UR ist
$\implies (x_{1}+x_{2})-x_{1}=x_{2} \in U_{1} ↯$
angenommen:
$x_{1}+ x_{2} \in U_{2}$, da $x_{1} \in U_{2}$, da $U_{2}$ ein UR ist
$\implies (x_{1}+x_{2})-x_{1}=x_{2} \in U_{2} ↯$
$\blacksquare$
