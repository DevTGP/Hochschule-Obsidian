![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=1bX9CxjvscBcf0SqDiESD|100%]]

$B := (\begin{pmatrix}5 \\ -1 \\ 4\end{pmatrix}, \begin{pmatrix}3 \\ 2 \\ 0\end{pmatrix},\begin{pmatrix}0 \\ 3 \\ 1\end{pmatrix}), v = \begin{pmatrix}8 \\ -2 \\ 3\end{pmatrix}, u = \begin{pmatrix}8 \\ 1 \\ 4\end{pmatrix}$

$\begin{pmatrix}5 & 3 & 0 & | & 8 \\ -1 & 2 & 3 & | & -2 \\ 4 & 0 & 1 & | & 3\end{pmatrix}$
$\lambda_{1}=1,\lambda_{2}=1,\lambda_{3}=-1$
$\to$ es können alle ausgetauscht werden

$\begin{pmatrix}8 & 3 & 0 & | & 8 \\ -2 & 2 & 3 & | & 1 \\ 3 & 0 & 1 & | & 4\end{pmatrix}$
$\lambda_{1}=1,\lambda_{2}=0,\lambda_{3}=1$
$\to\lambda_{3}$ kann ausgetauscht werden

$B := (\begin{pmatrix}8 \\ 1 \\ 4\end{pmatrix}, \begin{pmatrix}8 \\ -2 \\ 3\end{pmatrix}, \begin{pmatrix}3 \\ 2 \\ 0\end{pmatrix})$

$\to$ Test ob auch alle linear unabhängig

$\begin{pmatrix}I & 8 & 8 & 3 & | & 0 \\II &  1 & -2 & 2 & | & 0 \\III &  4 & 3 & 0 & | & 0\end{pmatrix}$
$\to II = (-1)  \cdot I + 8  \cdot II$
$\to III = (-1)  \cdot I + 2  \cdot III$

$\begin{pmatrix}8 & 8 & 3 & | & 0 \\ 0 & -24 & 13 & | & 0 \\ 0 & -2 & -3 & | & 0\end{pmatrix}$
$\to III = (-1)  \cdot I + 12  \cdot III$

$\begin{pmatrix}8 & 8 & 3 & | & 0 \\ 0 & -24 & 13 & | & 0 \\ 0 & 0 & -49 & | & 0\end{pmatrix}$
$\to$ Linear unabhängig
