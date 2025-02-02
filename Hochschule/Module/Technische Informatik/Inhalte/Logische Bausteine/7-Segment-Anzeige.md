[[Logische Bausteine]]

---

> [!check] Definition
> Eine **7-Segment-Anzeige** ist eine digitale Anzeige, die aus **sieben leuchtenden Segmenten** besteht und zur Darstellung von Zahlen und einigen Buchstaben verwendet wird.

> [!tip] Aufbau
> - Die Segmente sind als **a, b, c, d, e, f, g** bezeichnet.
> - Durch gezieltes Ein- und Ausschalten lassen sich Ziffern von **0–9** und einige Buchstaben (z. B. A, b, C, d, E, F) darstellen.
>
> ![[7-Segment-Anzeige Bild.png]]

> [!info] Logiktabelle
| x3  | x2  | x1  | x0  | Zeichen | a   | b   | c   | d   | e   | f   | g   |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0       | 1   | 1   | 1   | 1   | 1   | 1   | 0   |
| 0   | 0   | 0   | 1   | 1       | 0   | 1   | 1   | 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   | 2       | 1   | 1   | 0   | 1   | 1   | 0   | 1   |
| 0   | 0   | 1   | 1   | 3       | 1   | 1   | 1   | 1   | 0   | 0   | 1   |
| 0   | 1   | 0   | 0   | 4       | 0   | 1   | 1   | 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   | 5       | 1   | 0   | 1   | 1   | 0   | 1   | 1   |
| 0   | 1   | 1   | 0   | 6       | 1   | 0   | 1   | 1   | 1   | 1   | 1   |
| 0   | 1   | 1   | 1   | 7       | 1   | 1   | 1   | 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 0   | 8       | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| 1   | 0   | 0   | 1   | 9       | 1   | 1   | 1   | 1   | 0   | 1   | 1   |
| 1   | 0   | 1   | 0   | a       | 1   | 1   | 1   | 0   | 1   | 1   | 1   |
| 1   | 0   | 1   | 1   | b       | 0   | 0   | 1   | 1   | 1   | 1   | 1   |
| 1   | 1   | 0   | 0   | c       | 1   | 0   | 0   | 1   | 1   | 1   | 0   |
| 1   | 1   | 0   | 1   | d       | 0   | 1   | 1   | 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 0   | e       | 1   | 0   | 0   | 1   | 1   | 1   | 1   |
| 1   | 1   | 1   | 1   | f       | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 
