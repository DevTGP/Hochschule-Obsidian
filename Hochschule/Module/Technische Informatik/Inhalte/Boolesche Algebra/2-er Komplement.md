[[Negative Binärzahlen]]
[[Binärsystem]]

---

> [!success] Definition
> Das Zweierkomplement ist eine Methode, um negative Zahlen im Binärsystem darzustellen. Es wird definiert als:
> 
> - **Für eine n-Bit-Zahl**: Das Zweierkomplement einer Zahl x ist $2^n - x$.
> - **Praktische Umsetzung**:
> 	1. Invertiere alle Bits der Zahl ([[1-er Komplement]]).
> 	2. Addiere 1 zum Ergebnis.

> [!tip] Darstellung
> Für x = 5 in einem 4-Bit-System:
> 1. 5 = 0101.
> 2. [[1-er Komplement]]: 1010.
> 3. Addiere 1: 1010 + 1 = 1011.
> 
> Das Zweierkomplement von 5 ist 1011, was -5 darstellt.

> [!example]- Berechnung
> ![[2-er Komplement Addition#^main]]
> ![[2-er Komplement Subtraktion#^main]]
