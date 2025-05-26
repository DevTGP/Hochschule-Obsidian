![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=PuaLBtGixCgfr7Us5Tu3H|100%]]

(1)
$f: \mathbb{R}\to\mathbb{R}, f(x) = x^{n} \text{ mit } n \in \mathbb{N}>1$

$I: f(1+1) = 2^{n}$
$II: f(1) + f(1) = 1^{n} + 1^{n} = 2$
$I = II ↯$

Es gilt keine Linearität.

(2)
$f: \mathbb{R}^{2}\to \mathbb{R}^{2}, f(\begin{pmatrix}x_{1} \\ x_{2}\end{pmatrix})=\begin{pmatrix}x_{1}+2x_{2} \\ -5x_{1}\end{pmatrix}$

$b=\begin{pmatrix}b_{1} \\ b_{2}\end{pmatrix}$
$v=\begin{pmatrix}v_{1} \\ v_{2}\end{pmatrix}$

$I: f(b+v)=f(\begin{pmatrix}b_{1}+v_{1} \\ b_{2}+v_{2}\end{pmatrix}) = \begin{pmatrix}(b_{1}+v_{1})+2(b_{2}+v_{2}) \\ -5(b_{1}+v_{1})\end{pmatrix}$
$II: f(b)+f(v) =f(\begin{pmatrix}b_{1} \\ b_{2}\end{pmatrix})+f(\begin{pmatrix}v_{1} \\ v_{2}\end{pmatrix}) = \begin{pmatrix}(b*{1}+v*{1})+2(b*{2}+v*{2}) \\ -5(b*{1}+v*{1})\end{pmatrix}$
$I = II$

$I: f(\lambda b)=f(\begin{pmatrix}\lambda b_{1} \\\lambda b_{2}\end{pmatrix}) = \begin{pmatrix}\lambda b_{1} + 2\lambda b_{2} \\ -5\lambda b_{1}\end{pmatrix}$
$II: \lambda f( b)=\lambda f(\begin{pmatrix} b_{1} \\ b_{2}\end{pmatrix}) = \begin{pmatrix}\lambda b_{1} + 2\lambda b_{2} \\ -5\lambda b_{1}\end{pmatrix}$
$I = II$

Somit gilt Linearität.

(3)
$f: \mathbb{R}^{n}\to\mathbb{R}, f(x) =\vert\vert x\vert\vert$

$b,v \in \mathbb{R}^{n}$
$I: f(b+v) = \vert \vert b+v\vert\vert$
$II: f(b) + f(v) = \vert\vert b\vert\vert + \vert\vert v\vert\vert$

Somit gibt es nach der Dreiecksungleichung $b,v$ mit denen $I=II$ nicht mehr gilt.
