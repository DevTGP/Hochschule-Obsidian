![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=MC5iUUKgoTzb0QRT116Ly|100%]]

Es sei $v, v_{1}, v_{2} \in \mathbb{R}^{n}$ und $c \in \mathbb{R}$ so, dass $\langle v, u_{1} \rangle < c, \langle v, u_{2} \rangle < c$ gilt.

$\text{ z.z. }\lambda \in [0,1]$ und $w =\lambda u_{1} + (1-\lambda) u_{2}$ gilt

$\langle v,w \rangle$
$= \langle v,\lambda u_{1} + (1-\lambda) u_{2} \rangle$
$=\lambda \langle v,u_{1} \rangle + (1-\lambda) \langle v, u_{2} \rangle$
$=\lambda c + (1-\lambda)c$
$= (\lambda + (1-\lambda))c$
$= c$

Beispiel
![[LA_A27_Anhang_1.excalidraw|100%]]

$u_{1}=\begin{pmatrix}0 \\ -3\end{pmatrix}$
$u_{2}=\begin{pmatrix}0 \\ -5\end{pmatrix}$
$v=\begin{pmatrix}0 \\ 5\end{pmatrix}$
$c = 0$

$w =\lambda u_{1} +(1-\lambda)u_{2}$
$=\begin{pmatrix}-\lambda \cdot 0 \\ -\lambda  \cdot (-3)\end{pmatrix}+\begin{pmatrix}(1-\lambda)  \cdot 0 \\ (1-\lambda) \cdot(-5)\end{pmatrix}$
$=\begin{pmatrix}0 \\ 8\lambda -5\end{pmatrix}$

für $\lambda = -1$
