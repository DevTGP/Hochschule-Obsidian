[[Fließkomma IEEE 754]]

---

> [!check] Definition
> **Normalisierte IEEE 754 Fließkommazahlen** sind Zahlen, bei denen der Exponent **$E \neq 0$** ist, sodass die Mantisse immer die Form **1.xxxxx** hat.

> [!tip] Darstellung
> **Format:**
> 
> $(-1)^S \times 1.F \times 2^{(E - \text{Bias})}$
> 
> - **Vorzeichenbit (S)**: 0 = positiv, 1 = negativ
> - **Exponentenfeld (E)**: 1≤E≤2541 \leq E \leq 254 (für Single-Precision)
> - **Mantisse (F)**: 23 Bits (Single), 52 Bits (Double), führende **1 ist implizit**
> - **Bias**: 127 (Single), 1023 (Double)

> [!note] **Beispiel (Single-Precision, 32 Bit):** 
> 0 | 1000 0001 | 100 0000 0000 0000 0000 0000  
> S = 0, E = 129, F = 1.5
> 
> Ergebnis:
> - $1.5 \times 2^{(129 - 127)} = 1.5 \times 2^2 = 6.0$
