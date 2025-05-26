![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_06.excalidraw.md#^area=ZrgPgaTzboKnVPoiQiNAE|100%]]

(a)

| $x_{1}$ | $x_{2}$ | $x_{2} \Leftrightarrow x_{1}$ |
| ------- | ------- | ----------------------------- |
| $0$     | $0$     | $1$                           |
| $0$     | $1$     | $0$                           |
| $1$     | $0$     | $0$                           |
| $1$     | $1$     | $1$                           |

$\eta = 1$

| Epoche | Trainingseinheit | Erw. Eingabe $(x_{0};x_{1};x_{2})$ | Gewichte $(w_{0};w_{1};w_{2})$ | $x  \cdot w$ | Ausgabe $y$ | Zielausgabe $t$ | $t-y$ | Neue Gewichte    |
| ------ | ---------------- | ---------------------------------- | ------------------------------ | ------------ | ----------- | --------------- | ----- | ---------------- |
| $1$    | $1$              | $(1;0;0)$                          | $(0;0.5;-0.5)$                 | $0$          | $0$         | $1$             | $1$   | $(1;0.5;-0.5)$   |
| $1$    | $2$              | $(1;0;1)$                          | $(1;0.5;-0.5)$                 | $0.5$        | $1$         | $0$             | $-1$  | $(0;0.5;-1.5)$   |
| $1$    | $3$              | $(1;1;0)$                          | $(0;0.5;-1.5)$                 | $0.5$        | $1$         | $0$             | $-1$  | $(-1;-0.5;-1.5)$ |
| $1$    | $4$              | $(1;1;1)$                          | $(-1;-0.5;-1.5)$               | $-3$         | $0$         | $1$             | $1$   | $(0;0.5;-0.5)$   |
| $2$    | $1$              | $(1;0;0)$                          | $(0;0.5;-0.5)$                 | $0$          | $0$         | $1$             | $1$   | $(1;0.5;-0.5)$   |
| $2$    | $2$              | $(1;0;1)$                          | $(1;0.5;-0.5)$                 | $0.5$        | $1$         | $0$             | $-1$  | $(0;0.5;-1.5)$   |
| $2$    | $3$              | $(1;1;0)$                          | $(0;0.5;-1.5)$                 | $0.5$        | $1$         | $0$             | $-1$  | $(-1;-0.5;-1.5)$ |
| $2$    | $4$              | $(1;1;1)$                          | $(-1;-0.5;-1.5)$               | $-3$         | $0$         | $1$             | $1$   | $(0;0.5;-0.5)$   |

(b)
Die erste und zweite und auch jede weitere Epoche haben eine identische Entwicklung.

(c)
Das Perzeptron ist nicht lernfähig, da das Perzeptron nach jeder Epoche wieder auf seinen Anfangswerten liegt.

(d)
![[KI_Übung_06_Anhang_1]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_06.excalidraw.md#^area=YcTv-XarA1TMnkX-V8idJ|100%]]

(a)
![[KI_Übung_06_Anhang_2.png]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_06.excalidraw.md#^area=_SgbTqmdfNrpYNBup31EE|100%]]

(a)

| Attribut          | Wert   | Min-Max-Skalierung $x' = \frac{x-x_{min}}{x_{max}-x_{min}}$ | $\mu = \frac{1}{n} \sum_{i=1}^{n}x_{i}$ | $\sigma = \sqrt{ \frac{1}{n-1}\sum_{i=1}^{n}(x_{i}-\mu)^{2} }$ | Standardisierung (Z-Transformation) $x' = \frac{x-\mu}{\sigma}$ |
| ----------------- | ------ | ----------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| bill_length_mm    | $39.1$ | $0.4$                                                       | $39$                                    | $2.301$                                                        | $0.043$                                                         |
|                   | $38.8$ | $0.357$                                                     |                                         |                                                                | $-0.087$                                                        |
|                   | $36.3$ | $0.0$                                                       |                                         |                                                                | $-1.173$                                                        |
|                   | $38.2$ | $0.271$                                                     |                                         |                                                                | $-0.348$                                                        |
|                   | $39.0$ | $0.386$                                                     |                                         |                                                                | $0.0$                                                           |
|                   | $43.3$ | $1.0$                                                       |                                         |                                                                | $1.869$                                                         |
|                   |        |                                                             |                                         |                                                                |                                                                 |
|                   |        |                                                             |                                         |                                                                |                                                                 |
|                   |        |                                                             |                                         |                                                                |                                                                 |
| bill_depth_mm     | $18.7$ | $0.783$                                                     | $18$                                    | $2.2$                                                          | $0.318$                                                         |
|                   | $17.2$ | $0.533$                                                     |                                         |                                                                | $-0.364$                                                        |
|                   | $19.5$ | $0.913$                                                     |                                         |                                                                | $0.682$                                                         |
|                   | $20.0$ | $1.0$                                                       |                                         |                                                                | $0.909$                                                         |
|                   | $17.1$ | $0.517$                                                     |                                         |                                                                | $-0.409$                                                        |
|                   | $14.0$ | $0.0$                                                       |                                         |                                                                | $-1.818$                                                        |
|                   |        |                                                             |                                         |                                                                |                                                                 |
|                   |        |                                                             |                                         |                                                                |                                                                 |
|                   |        |                                                             |                                         |                                                                |                                                                 |
| flipper_length_mm | $181$  | $0.036$                                                     | $190$                                   | $10.06$                                                        | $-0.895$                                                        |
|                   | $180$  | $0.0$                                                       |                                         |                                                                | $-0.994$                                                        |
|                   | $190$  | $0.357$                                                     |                                         |                                                                | $0.0$                                                           |
|                   | $190$  | $0.357$                                                     |                                         |                                                                | $0.0$                                                           |
|                   | $191$  | $0.393$                                                     |                                         |                                                                | $0.099$                                                         |
|                   | $208$  | $1.0$                                                       |                                         |                                                                | $1.789$                                                         |
|                   |        |                                                             |                                         |                                                                |                                                                 |
|                   |        |                                                             |                                         |                                                                |                                                                 |
|                   |        |                                                             |                                         |                                                                |                                                                 |
| body_mass_g       | $3750$ | $0.459$                                                     | $3812$                                  | $484.704$                                                      | $-0.128$                                                        |
|                   | $3800$ | $0.492$                                                     |                                         |                                                                | $-0.025$                                                        |
|                   | $3800$ | $0.492$                                                     |                                         |                                                                | $-0.025$                                                        |
|                   | $3900$ | $0.557$                                                     |                                         |                                                                | $0.182$                                                         |
|                   | $3050$ | $0.0$                                                       |                                         |                                                                | $-1.572$                                                        |
|                   | $4575$ | $1.0$                                                       |                                         |                                                                | $1.574$                                                         |

```python
import math

def min_max(l):
	for i in l:
		print(round((i-min(l))/(max(l)-min(l)) ,3))
	print()

min_max([39.1,38.8,36.3,38.2,39.0,43.3])
min_max([18.7,17.2,19.5,20.0,17.1,14.0])
min_max([181,180,190,190,191,208])
min_max([3750,3800,3800,3900,3050,4575])


def z_transformation(l):
	mu = round(1/len(l) *sum(l))
	sigma = 0
	for i in l:
		sigma += (i-mu)**2
	sigma *= 1/(len(l)-1)
	sigma = round(math.sqrt(sigma), 3)
	print(f'Mittelwert: {mu}')
	print(f'Standardabweichung: {sigma}')
	for i in l:
		print(round((i-mu)/sigma,3))
	print()

z_transformation([39.1,38.8,36.3,38.2,39.0,43.3])
z_transformation([18.7,17.2,19.5,20.0,17.1,14.0])
z_transformation([181,180,190,190,191,208])
z_transformation([3750,3800,3800,3900,3050,4575, 15000])
```

(b)
![[KI_Übung_06_Anhang_3.png]]

(c)
oben $i$. $d$. Tabelle

(d)
![[KI_Übung_06_Anhang_4.png]]

(e)

Ansonsten würden der Test-Datensatz Einfluss auf den Trainingsdatensatz nehmen, und wir könnten keine unabhängigen Tests erzielen.
