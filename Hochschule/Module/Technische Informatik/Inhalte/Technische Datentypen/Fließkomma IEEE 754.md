[[Technische Informatik]]

---

> [!check] Definition
> Der **IEEE 754** Standard definiert das Format für **Fließkommazahlen** in Computern. Eine Zahl besteht aus drei Teilen:
> 
> 1. **Vorzeichenbit (1 Bit)** – 0 für positiv, 1 für negativ
> 2. **Exponentenfeld (8 Bit für Single, 11 Bit für Double)** – Biased-Exponent
> 3. **Mantisse (23 Bit für Single, 52 Bit für Double)** – Normierte Gleitkommadarstellung

> [!tip] Darstellung
> Binär:
> 
| Vorzeichen / S (Sign) | Exponent / E (Exponent) | Mantisse / F       (Fraction | 
| --------------------- | ----------------------- | ---------------------------- |
| 1                     | 10010001                | 10001110001000000000000      |
> 
> Mathematisch:
> $(-1)^S \times 1.F \times 2^{(E - Bias)}$
> 
> - **Bias**: 127 für Single, 1023 für Double
> - **Spezielle Werte**:
>     - $E = 255, F = 0 \to\pm \infty$
>     - $E = 255, F \neq 0 \to NaN$
>     - $E = 0 \to$ Subnormale Zahlen oder Null

> [!example] Inhalt
> 1. [[Normalisiert]]
> 2. [[Denormalisiert]]
> 3. [[IEEE 754 Standards]]

> [!caution] Wichtige Werte
> ![[IEEE 754 Representation#^main]]
