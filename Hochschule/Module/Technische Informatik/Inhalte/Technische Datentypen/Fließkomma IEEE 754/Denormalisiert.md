[[Fließkomma IEEE 754]]

---

> [!check] Definition
> **Denormalisierte IEEE 754 Fließkommazahlen** sind Zahlen mit **E = 0**, wodurch die führende **1 in der Mantisse entfällt**.

> [!tip] Darstellung
> **Format:**
> 
> $(-1)^S \times 0.M \times 2^{(1 - \text{Bias})}$
> 
> - **Vorzeichenbit (S)**: 0 = positiv, 1 = negativ
> - **Exponentenfeld (E = 0)**: Spezieller Exponent für denormalisierte Werte
> - **Mantisse (F)**: 23 Bits (Single), 52 Bits (Double) **ohne führende 1**
> - **Bias**: 127 (Single), 1023 (Double)

> [!info] **Eigenschaften:**
> - Ermöglichen eine **weiche Unterlaufgrenze** für sehr kleine Zahlen
> - Kleinster positiver Wert in Single-Precision: 
> 	- $1.0 \times 2^{-126} \quad \text{(normalisiert)}$
> 	- $0.000...01\times 2^{-126} \quad \text{(denormalisiert)}$
