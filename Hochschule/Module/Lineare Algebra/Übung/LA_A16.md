![[LA_Aufgabensammlung_01.excalidraw#^area=xG4RaUo9b_kkH-7uxHeiC|100%]]

# a)

Multiplikationen von $Ax$: $m\cdot n$
Additionen von $Ax$: $m \cdot (n-1)$

Beispiel:

$$
\begin{flalign*}
&m=5, n=3&\\
&\implies\mathbb{R}^{5x3}\cdot \mathbb{R}^{3}\\
&\implies \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
a_{41} & a_{42} & a_{43} \\
a_{51} & a_{52} & a_{53}
\end{pmatrix}\begin{pmatrix}
b_{1} \\
b_{2} \\
b_{3}
\end{pmatrix}&= \begin{pmatrix}
a_{11}*b_{1} + a_{12}*b_{2} + a_{13}*b_{3} \\
a_{21}*b_{1} + a_{22}*b_{2} + a_{23}*b_{3} \\
a_{31}*b_{1} + a_{32}*b_{2} + a_{33}*b_{3} \\
a_{41}*b_{1} + a_{42}*b_{2} + a_{43}*b_{3} \\
a_{51}*b_{1} + a_{52}*b_{2} + a_{53}*b_{3}
\end{pmatrix}&\\
&\\&\\
&\implies \text{Multiplikationen: }5\cdot 3=5&\\
&\implies \text{Additionen: }(5-1)\cdot 3=10
\end{flalign*}
$$

# b)

Multiplikationen von $Ax$: $n$
Additionen von $Ax$: $0$

Beispiel:

$$
\begin{flalign*}
&m=n=5&\\
&\implies\mathbb{R}^{5x5}\cdot \mathbb{R}^{5}\\
&\implies \begin{pmatrix}
a_{11} & 0 & 0 & 0 & 0 \\
0 & a_{22} & 0 & 0 & 0 \\
0 & 0 & a_{33} & 0 & 0 \\
0 & 0 & 0 & a_{44} & 0 \\
0 & 0 & 0 & 0 & a_{55}
\end{pmatrix}\begin{pmatrix}
b_{1} \\
b_{2} \\
b_{3} \\
b_{4} \\
b_{5}
\end{pmatrix}&=
\begin{pmatrix}
a_{11}*b_{1} & 0 & 0 & 0 & 0 \\
0 & a_{22}*b_{2} & 0 & 0 & 0 \\
0 & 0 & a_{33}*b_{3} & 0 & 0 \\
0 & 0 & 0 & a_{44}*b_{4} & 0 \\
0 & 0 & 0 & 0 & a_{55}*b_{5}
\end{pmatrix}
&\\&\\
&\implies \text{Multiplikationen: }n&\\
&\implies \text{Additionen: }0
\end{flalign*}
$$
