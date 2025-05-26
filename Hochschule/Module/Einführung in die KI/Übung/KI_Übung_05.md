![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_05.excalidraw.md#^area=QZ738fyy6jfzEIk5zUGT_|100%]]

a)

$\text{ Gewichtete Entropy } = \sum_{v\in A} \frac{p}{p+q}  \cdot Entropy(A_{v})$
$Gain(S, A) = Entropy(S) - Gewichtete Entropy(S)$

| $v$          | $\lvert S_{v} \rvert$ | $q$            | $Entropy(S_{v})$ |
| ------------ | --------------------- | -------------- | ---------------- |
| $Morning$    | $4$                   | $\frac{2}{4}$  | $1$              |
| $Afternoon$  | $3$                   | $\frac{0}{3}$  | $0$              |
| $Evening$    | $4$                   | $\frac{2}{4}$  | $1$              |
| $Night$      | $3$                   | $\frac{2}{3}$  | $0.918$          |
|              |                       |                |                  |
| $Desktop$    | $6$                   | $\frac{0}{6}$  | $0$              |
| $Mobile$     | $8$                   | $\frac{6}{8}$  | $0.811$          |
|              |                       |                |                  |
| $CreditCard$ | $7$                   | $\frac{4}{7}$  | $0.985$          |
| $Paypal$     | $7$                   | $\frac{2}{7}$  | $0.863$          |
|              |                       |                |                  |
| $Gesamt$     | $14$                  | $\frac{6}{14}$ | $0.985$          |

$GewichteteEntropy(TimeOfDay) = 0.768$
$GewichteteEntropy(Device) = 0.464$
$GewichteteEntropy(PaymentMethod) = 0.924$

$Gain(S, TimeOfDay) = 0.985-0.768=0.217$
$Gain(S, Device) = 0.985-0.464=0.421$
$Gain(S, PaymentMethod) = 0.985-0.924=0.061$

b)
![[KI_Übung_05_Anhang_1.excalidraw|100%]]

c)
![[KI_Übung_05_A1_KNIME_DECISION_TREE.png|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_05.excalidraw.md#^area=4__9--Iz1a7vkr6m-sOVz|100%]]

$x_{0}=1,w_{0}=0.5, w_{1}=1.0, w_{2}=-1.0$

$y=\varphi(\vec{x}  \cdot \vec{w}) = \begin{cases}1 & , \text{wenn } \vec{x}  \cdot \vec{w} > 0 \\ 0 & ,\text{sonst }\end{cases}$

$w_{i}^{neu}=w_{i}^{alt}+\Delta w_{i}$ mit $\Delta w_{i}=\eta  \cdot(t-y) \cdot x_{i}$ für $i= 0,\dots,n,\eta > 0$

(1)
$\vec{x} = (1;0;1)$
$\vec{w} = (0.5;1.0;-1.0)$

$\vec{x} \cdot \vec{w}=\begin{pmatrix}1 \\ 0 \\ 1\end{pmatrix} \cdot \begin{pmatrix}0.5 \\ 1.0 \\ -1.0\end{pmatrix}=-0.5$

$y =\varphi(\vec{x} \cdot \vec{w})=\varphi(-0.5)=0$

(2)
$t=1,\eta=1$

$\Delta w_{1}=\eta  \cdot(t-y) \cdot x_{1}=1  \cdot(1-0)  \cdot 1=1$
$w_{1}^{neu}=w_{1}^{alt}+\Delta w_{1} =0.5 + 1=1.5$

$\Delta w_{2}=\eta  \cdot(t-y) \cdot x_{2}=1  \cdot(1-0)  \cdot 0=0$
$w_{2}^{neu}=w_{2}^{alt}+\Delta w_{2} =1.0 + 0=1.0$

$\Delta w_{3}=\eta  \cdot(t-y) \cdot x_{3}=1  \cdot(1-0)  \cdot 1=1$
$w_{3}^{neu}=w_{3}^{alt}+\Delta w_{3} =-1.0 + 1=0$

$\vec{w} = \begin{pmatrix}1.5 \\ 1.0 \\ 0.0\end{pmatrix}$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_05.excalidraw.md#^area=TP_XKVs9IQtmhxM7f12h2|100%]]

(1)
(2)

| $x_{0}$ | $x_{1}$ | $x_{2}$ | $x_{2}\to x_{1}$ |
| ------- | ------- | ------- | ---------------- |
| 1       | 0       | 0       | 1                |
| 1       | 0       | 1       | 0                |
| 1       | 1       | 0       | 1                |
| 1       | 1       | 1       | 1                |

$\eta = 1$

| n   | Erw. Eingabe $(x_{0};x_{1};x_{2})$ | Gewichte $(w_{0};w_{1};w_{2})$ | $x  \cdot w$ | Ausgabe $y$ | Zielausgabe $t$ | $t-y$ | Neue Gewichte        |
| --- | ---------------------------------- | ------------------------------ | ------------ | ----------- | --------------- | ----- | -------------------- |
| 1   | $(1;0;0)$                          | $(-1.0;1.0;-2.0)$              | $-1.0$       | $0$         | $1$             | $1$   | $(0.0;1.0;-2.0)$     |
| 2   | $(1;0;1)$                          | $(0.0;1.0;-2.0)$               | $-2.0$       | $0$         | $0$             | $0$   | $(0.0;1.0;-2.0)$     |
| 3   | $(1;1;0)$                          | $(0.0;1.0;-2.0)$<br>           | $1$          | $1$         | $1$             | $0$   | $(0.0;1.0;-2.0)$     |
| 4   | $(1;1;1)$                          | $(0.0;1.0;-2.0)$<br>           | $-1.0$       | $0$         | $1$             | $1$   | $(1.0;2.0;-1.0)$<br> |
| 1   | $(1;0;0)$                          | $(1.0;2.0;-1.0)$<br>           | $1$          | $1$         | $1$             | $0$   | $(1.0;2.0;-1.0)$<br> |
| 2   | $(1;0;1)$                          | $(1.0;2.0;-1.0)$<br>           | $0$          | $0$         | $0$             | $0$   | $(1.0;2.0;-1.0)$<br> |
| 3   | $(1;1;0)$                          | $(1.0;2.0;-1.0)$<br>           | $3$          | $1$         | $1$             | $0$   | $(1.0;2.0;-1.0)$<br> |
| 4   | $(1;1;1)$                          | $(1.0;2.0;-1.0)$<br>           | $2$          | $1$         | $1$             | $0$   | $(1.0;2.0;-1.0)$<br> |

(3)
(1. Neues Gewicht)
$x_{2}​=-\frac{w_{1}}{w_{2}}​​x_{1}​− \frac{w_{0}}{w_{2}}​​​$
$x_{2}=- \frac{1.0}{-2.0} \cdot x_{1} - \frac{0.0}{-2.0}=0.5x_{1}$

(2. Neues Gewicht)
$x_{2}​=-\frac{w_{1}}{w_{2}}​​x_{1}​− \frac{w_{0}}{w_{2}}​​​$
$x_{2}=- \frac{2.0}{-1.0} \cdot x_{1} - \frac{1.0}{-1.0}=2x_{1} + 1$

$x_{2}​=-\frac{w_{1}}{w_{2}}​​x_{1}​− \frac{w_{0}}{w_{2}}​​​$
$\to y$ bestimmen
![[KI_Übung_05_Anhang_2.excalidraw|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_05.excalidraw.md#^area=A6auO8OlK3hmMvwJ5RFJp|100%]]

a)

> [! note]
> Ableiten
> $f(x)=x^{-1} \to f'(x)=-x^{-2}$

$\varphi(x) = (1+e^{-x})^{-1}$

$I.$
$\varphi'(x) = -(1+e^{-x})^{-2}  \cdot (-e^{-x})$
$=-\frac{1}{(1+e^{-x})^{2}}  \cdot(-e^{-x})$
$=\frac{e^{-x}}{(1+e^{-x})^{2}}$
$=\frac{1}{e^{x}(1+e^{-x})^{2}}$

$II.$
$\frac{1}{1+e^{-x}} \cdot (1-1+e^{-x})$
$=\frac{1}{1+e^{-x}} - \frac{1}{(1+e^{-x})^{2}}$
$=\frac{1+e^{-x}}{(1+e^{-x})^{2}} - \frac{1}{(1+e^{-x})^{2}}$
$=\frac{1}{e^{x}(1+e^{-x})^{2}}$

$\to I. = II.$

b)

$\varphi(-x) = 1-\varphi(x) \Leftrightarrow 1-\frac{1}{1+e^{-x}}$
$\frac{1+e^{-x}}{1+e^{-x}}-\frac{1}{1+e^{-x}}=\frac{e^{-x}}{1+e^{-x}} \cdot \frac{e^{x}}{e^{x}}$
$=\frac{1}{e^{x}+1}=\frac{1}{1+e^{x}}$
