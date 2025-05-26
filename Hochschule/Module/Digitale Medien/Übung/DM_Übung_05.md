![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=ukb7L0yY-3sWrO2Udz6AV|100%]]

(a)
Vektorgrafiken, da alles abgemessen ist, und in Vektorgrafiken präziser gespeichert wird.

(b)
(Rastergrafik, weil die Zeichnungen Farbverläufe und filigrane Muster beinhalten.)

(c)
Vektorgrafik, da die Diagramme eh auf Daten beruhen, und somit mit Vektorgrafiken genau und einfach dargestellt werden können.

(d)
Vektorgrafik, da auch hier mit mehr Präzision gearbeitet werden kann.

(e)
Rastergrafik, da die Karte viele harte Kanten hat, welche schwer als Vektorgrafik darzustellen sind.

(f)
Rastergrafik, da viele Farbverläufe und filigrane Muster nicht einfach mit einer Vektorgrafik erfassbar sind.

(g)
Vektorgrafik, besteht meist nur aus wenigen kurven und geraden, und gefüllten Flächen.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=cVMT_g9pUtkJBqsuGnHSa|100%]]

Linien:

- $2 Punkte \to((x_{1},y_{1}),(x_{2},y_{2}))$

Kantenzüge:

- $Polylinie \to $((x_{1},y_{1}, \dots, (x_{n},y_{n})))$$ (Das Ende jeder Linie ist der Start der jeweils nächsten Linie)
- $Polygon \to((x_{1},y_{1}, \dots, (x_{n},y_{n})))$ (Das Ende der letzten Linie ist mit dem Start der letzten Linie verbunden)

Kreise:

- $\text{ Koordinaten \& Radius } \to (x, y, r)$

Ellipsen:

- $\text{ Mittelpunktform }$
- $\text{ Parametrische Form }$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=qS1mQ4zkvm2MXNZOuYorr|100%]]

Bei der Skalierung wird die ganze Matrix skaliert. Jeder Punkt wird durch einen Vektor dargestellt, welche mit einem Skalar multipliziert werden. Somit verschieben sich die einzelnen Punkte.

![[DM_Übung_05_Anhang_1.excalidraw|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=G-xS7egXkYhvxAJAOnGkr|100%]]

Gegeben:
$Quadrat_{Seitenlänge}=2$
$Quadrat_{Position}=(4,4)$

$\begin{pmatrix}\cos 90 & -\sin 90 & 0 \\ \sin 90 & \cos90 & 0 \\ 0 & 0 & 1\end{pmatrix} \cdot\begin{pmatrix}1 & 0 & 2 \\ 0 & 1  & 2 \\ 0 & 0 & 1\end{pmatrix} \cdot0.5\begin{pmatrix}4 \\ 4 \\ 1\end{pmatrix}$
$=\begin{pmatrix}\cos \frac{\pi}{2} & -\sin \frac{\pi}{2} & 0 \\ \sin \frac{\pi}{2} & \cos \frac{\pi}{2} & 0 \\ 0 & 0 & 1\end{pmatrix} \cdot\begin{pmatrix}1 & 0 & 2 \\ 0 & 1  & 2 \\ 0 & 0 & 1\end{pmatrix} \cdot0.5 \cdot\begin{pmatrix}4 \\ 4 \\ 1\end{pmatrix}$
$=\begin{pmatrix}0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1\end{pmatrix} \cdot\begin{pmatrix}1 & 0 & 2 \\ 0 & 1  & 2 \\ 0 & 0 & 1\end{pmatrix} \cdot0.5 \cdot\begin{pmatrix}4 \\ 4 \\ 1\end{pmatrix}$
$=\begin{pmatrix}0 & -1 & -2 \\  1 & 0 & 2 \\ 0 & 0 & 1\end{pmatrix} \cdot0.5 \cdot\begin{pmatrix}4 \\ 4 \\ 1\end{pmatrix}$
$=\begin{pmatrix}0 & -.5 & -1 \\  .5 & 0 & 1 \\ 0 & 0 & .5\end{pmatrix}\cdot\begin{pmatrix}4 \\ 4 \\ 1\end{pmatrix}$
$=\begin{pmatrix}-3  \\ 3 \\ 0.5\end{pmatrix}$

$\to Quadrat_{Position_{Neu}}=(4,4)$

Es gibt 3 Permutationen.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=GYCa7W4v1xW64QB1tLZqP|100%]]

![[DM_Übung_05_Anhang_2.excalidraw|100%]]

$\text{ Kante } k \text{ - Endpunkte } p,q$
$\text{ Endpunktcodes } C(p), C(q)$
(1) Test: $C(p) OR C(q) == 0000$

- Beide Punkte liegen im Sicht
    $\to$ Beibehalten

(2) Test: $C(p) AND C(q) \neq 0000$

- Beide Punkte liegen oberhalb, unterhalb, links oder rechts des Sichtfenster
    $\to$ Ignorieren

(3) Test: $C(p) \neq 0000$

- Falls Linie $(p,q)$ Sichtfenster schneidet $(p,q)$ ersetzen durch $(s,q)$, wobei $s$ der erste Schnittpunkt der von $p$ ausgehenden Linie mit dem Rand des Sichtfensters ist
- Sonst: Ignorieren

(4) Test: $\text{ Analog für } C(q)$

(A)
$p=0000, q=0010$

1. $p\lor q = 0010 ↯$
2. $p \land q = 0000$
3. $p \neq 0000$
4. $q \neq 0000 ↯$

$\to$ Linie schneiden, falls mit Rand schneidet $\to (s,q)$

(B)
$p=0010, q=0010$

1. $p\lor q = 0010 ↯$
2. $p \land q = 0010 ↯$

$\to$ Linie außerhalb

(C)
$p=0000, q=0010$

1. $p\lor q = 0010 ↯$
2. $p \land q = 0000$
3. $p \neq 0000$
4. $q \neq 0000 ↯$

$\to$ Linie schneiden, falls mit Rand schneidet $\to (s,q)$

(D)
$p=0000, q=0100$

1. $p\lor q = 0100 ↯$
2. $p \land q = 0000$
3. $p \neq 0000$
4. $q \neq 0000 ↯$

$\to$ Linie schneiden, falls mit Rand schneidet $\to (s,q)$

(E)
$p=0100, q=0010$

1. $p\lor q = 0110 ↯$
2. $p \land q = 0000$
3. $p \neq 0000$
4. $q \neq 0000$

$\to$ Linie schneiden, falls mit Rand schneidet$\to (s,q)$

(F)
$p=0010, q=0110$

1. $p\lor q = 0110 ↯$
2. $p \land q = 0010 ↯$

$\to$ Linie außerhalb

(G)
$p=0100, q=0110$

1. $p\lor q = 0110 ↯$
2. $p \land q = 0100 ↯$

$\to$ Linie außerhalb

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=8uu9c4egVnS-_8BTw7tbq|100%]]

Der rechte Stern ist mit Hilfe der $\text{ Even Odd Rule }$ geschaffen.

Der linke Stern ist mit Hilfe der $\text{ Non-Zero Winding Rule }$ geschaffen.

![[DM_Übung_05_Anhang_3.excalidraw|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_05.excalidraw.md#^area=KK6n8N0jsS1VLZpQEf7hw|100%]]

![[DM_Übung_05_Anhang_4.svg|100%]]
