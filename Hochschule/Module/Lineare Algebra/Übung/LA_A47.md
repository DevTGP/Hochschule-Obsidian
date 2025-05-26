![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=-Sw3qHqrLK6F4BgNnKj2P|100%]]

Es seien $A \in \mathbb{R}^{m \times n}, B \in \mathbb{R}^{n \times n}$
$Ker(B) \subset Ker(AB) \text{ oder } Ker(AB) \subset Ker(B)$

Es gilt (nach Def.):
$Kern (B):= \{x \in \mathbb{R}^{n}: Bx=0\}$
$Kern (AB):= \{x \in \mathbb{R}^{n}: ABx=0\}$

Sei $x\in Ker (B)$. Dann gilt

$ABx = A  \cdot 0 =0$
also folgt $x \in Ker(AB)$. Da $x \in Ker(B)$ beliebig war folgt \*

Zu Widerlegen:

$Ker(AB) \subset Ker(B)$
finde $x \in Ker(AB)$ wo gilt $ABx = 0, B\neq0$

Bsp. $A= \begin{pmatrix}0 & 0\end{pmatrix}, B=\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$

$x=\begin{pmatrix}1 \\ 2\end{pmatrix}$
$A  \cdot B=\begin{pmatrix}0 & 0\end{pmatrix} \cdot \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix} = \begin{pmatrix}0 & 0\end{pmatrix}$
$A  \cdot B \cdot x = \begin{pmatrix}0 & 0\end{pmatrix}  \cdot \begin{pmatrix}1 \\ 2\end{pmatrix} = 0$
$Bx=\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix} \cdot\begin{pmatrix}1 \\ 2\end{pmatrix}=\begin{pmatrix}1 \\ 0\end{pmatrix}$

$\begin{pmatrix}1 \\ 0\end{pmatrix}\neq0 ↯$
