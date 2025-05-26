![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_04.excalidraw.md#^area=2t_-cM9ml6jq07MvR0B9A|100%]]

| Nummer | Outlook  | Humidity | Wind   | PlayTennis |
| ------ | -------- | -------- | ------ | ---------- |
| 1      | Sunny    | High     | Weak   | No         |
| 2      | Sunny    | High     | Strong | No         |
| 3      | Overcast | High     | Weak   | Yes        |
| 4      | Rain     | High     | Weak   | Yes        |
| 5      | Rain     | Normal   | Weak   | Yes        |
| 6      | Rain     | Normal   | Strong | No         |
| 7      | Overcast | Normal   | Strong | Yes        |
| 8      | Sunny    | High     | Weak   | No         |
| 9      | Sunny    | Normal   | Weak   | Yes        |
| 10     | Rain     | Normal   | Weak   | Yes        |
| 11     | Sunny    | Normal   | Strong | Yes        |
| 12     | Overcast | High     | Strong | Yes        |
| 13     | Overcast | Normal   | Weak   | Yes        |
| 14     | Rain     | High     | Strong | No         |

a)
$p_{1}=\frac{9}{14}$ Anteil Positiv Beispiele
$p_{2}=\frac{9}{14}$ Anteil Negativ Beispiele
$S$ = Menge der Trainingsbeispiele
$A \in \{Outlook, Humidity, Wind\}$

$q = p_{1} = \frac{9}{14}$
$(1-q) = p_{2} = \frac{5}{14}$

$Gini(S)= 1- \sum_{i=1}^{n}p_{i}^{2} \text{ | } n=2$ 2 Klassen (Positiv / Negativ)
$=1 - (p_{1}^{2}+p_{2}^{2})$
$= 1 - p_{1}^{2}-p_{2}^{2}$
$= 1- q^{2}-(1-q)^{2}$
$= 1- q^{2}- (1-2q+q^{2})$
$= 1- q^{2}+ 1+2q-q^{2}$
$= -2q^{2}+2q$
$= -2q(-q+1)$
$= -2q(1-q)$ | $q$ einsetzen
$= -2 \cdot \frac{9}{14} \left( 1-\frac{9}{14} \right)$
$= -\frac{18}{14} \left( 1-\frac{9}{14} \right)$

Maximale Reinheit
$p=0$: $Gini(S)=0$
$p=1$: $Gini(S)=0$
Maximale Unreinheit
$p=0.5$: $Gini(S)=0.5$

b)
$q = \frac{9}{14}$
$Gini(S) = Gini(\{x_{1},\dots,x_{2}\})$
$=2q(1-q)$
$=2 \left( \frac{9}{14} \right)\left( \frac{5}{14} \right)$
$=\frac{90}{14^{2}}$
$\approx 0.45918673$

c)

| $v$        | $│S_{v}│$ | $q$           | $Gini(S_{v})=2q(1-q)$ |
| ---------- | --------- | ------------- | --------------------- |
| $Sunny$    | $5$       | $\frac{3}{5}$ | $0.48$                |
| $Overcast$ | $4$       | $1$           | $0$                   |
| $Rain$     | $5$       | $\frac{3}{5}$ | $0.48$                |
|            |           |               |
| $High$     | $7$       | $\frac{3}{7}$ | $0.48$                |
| $Normal$   | $7$       | $\frac{6}{7}$ | $0.24$                |
|            |           |               |
| $Strong$   | $6$       | $\frac{3}{6}$ | $0.5$                 |
| $Weak$     | $8$       | $\frac{6}{8}$ | $0.38$                |

$\text{ Gini-Index}(S, \text{ Outlook }) = \sum_{v \in Values(Outlook)} \frac{|S_{v}|}{|S|} \cdot Gini(S_{v})$
$= \frac{5}{14} \cdot 0.48 + \frac{4}{14}\cdot0+\frac{5}{14}\cdot0.48$
$=0.343$

$\text{ Gini-Index}(S, \text{ Humidity }) = \sum_{v \in Values(Outlook)} \frac{|S_{v}|}{|S|} \cdot Gini(S_{v})$
$= \frac{7}{14} \cdot 0.48 + \frac{7}{14}\cdot0.24$
$=0.36$

$\text{ Gini-Index}(S, \text{ Wind }) = \sum_{v \in Values(Outlook)} \frac{|S_{v}|}{|S|} \cdot Gini(S_{v})$
$= \frac{6}{14} \cdot 0.5 + \frac{8}{14}\cdot0.38$
$=0.431$

kleinster Wert ist am besten $\implies$ Outlook

d)

$\text{ Gini-Index(S, Nummer)} = \sum_{v=1}^{14} \frac{1}{14}\cdot0$
$=0$

$\implies$ Es sind keine Verallgemeinerten Aussagen mithand des Attributwertes möglich
Oder:
Der Entscheidungsbaum lernt die Beispiele auswendig.

e)

$S = \{x_{1},\dots, x_{2}\}$

$p$ positivbeispiele

$m \cdot p$ negativbeispiele

$q = \frac{p}{p+m}=\frac{p}{m}$ der Anteil der Positivbeispiele

![[KI_Übung_04__Anhang_1.excalidraw]]

$P(Falsch Klassifizieren) = P(A=p) \cdot P(K=p) +P(A=n) \cdot P(K=n)$
$=q \cdot (1-q) + (1-q) \cdot q$
$=2q \cdot (1-q)$
$=Gini(S)$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_04.excalidraw.md#^area=6WQ4bnZvB-q5VmnJGMxVP|100%]]

1.
2.

Klassifikation A

|        | GP            | GN            | Precision     |
| ------ | ------------- | ------------- | ------------- |
| SP     | $\frac{3}{8}$ | $\frac{2}{8}$ | $\frac{3}{5}$ |
| SN     | $\frac{1}{8}$ | $\frac{2}{8}$ | $\frac{1}{3}$ |
| Recall | $\frac{3}{4}$ | $\frac{1}{2}$ | $Accuracy=$   |

Klassifikation B

|        | GP            | GN            | Precision     |
| ------ | ------------- | ------------- | ------------- |
| SP     | $\frac{2}{8}$ | $\frac{2}{8}$ | $\frac{1}{2}$ |
| SN     | $\frac{2}{8}$ | $\frac{2}{8}$ | $\frac{1}{2}$ |
| Recall | $\frac{1}{2}$ | $\frac{1}{2}$ | $Accuracy=$   |

3.  a)
    $$
    Comp(E, F)= \begin{cases}
    \left( 1- \frac{|E_{error} \cap F_{error}|}{E_{error}} \right) \cdot 100, &falls E_{error} \neq \emptyset \\
    0, & sonst
    \end{cases}
    $$

b)

Der Wert sagt aus, wie viele Fehler Klassifikator $A$ nicht erkennt, aber Klassifikator $B$ erkennt.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_04.excalidraw.md#^area=tngX0LUj9z2vJSnXctIKf|100%]]

|        | GP      | GN      | Precision |
| ------ | ------- | ------- | --------- |
| SP     | $93$    | $18$    | $0.838$   |
| SN     | $18$    | $49$    | $0.731$   |
| Recall | $0.838$ | $0.731$ | $0.798$   |
