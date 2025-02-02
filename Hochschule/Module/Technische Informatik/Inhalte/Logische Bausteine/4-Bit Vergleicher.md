[[Logische Bausteine]]

---

> [!check] Definition
> Ein **4-Bit-Vergleicher** ist eine digitale Schaltung, die zwei **4-Bit-Binärzahlen** vergleicht und deren Verhältnis bestimmt.[[Logische Bausteine]]

> [!info] Funktion
> Eingaben:
> - Zwei 4-Bit-Zahlen: **$A (A_{0}, A_{1}, A_{2}, A_{3})$** und **$B (B_{0}, B_{1}, B_{2}, B_{3})$**
>
> Ausgaben:
> 1. **$A = B** \to 1$, wenn beide Zahlen gleich sind.
> 2. **$A > B** \to 1$, wenn A größer als B ist.
> 3. **$A < B** \to 1$, wenn A kleiner als B ist.
>
> Funktionsweise:
> - Vergleicht die Bits von **MSB (höchstes Bit) bis LSB (niedrigstes Bit)**.
> - Gibt das Ergebnis basierend auf den höchsten ungleichen Bits aus.

> [!tip] Aufbau
> ![[4-Bit Vergleicher Bild.png]]
