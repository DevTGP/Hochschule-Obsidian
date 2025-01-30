[[Latches und Flip-flops]]

---

> [!check] Definition
> Ein **T-FlipFlop** (Toggle-FlipFlop) ist ein **bistabiles Speicher-Element**, das bei jeder **Taktflanke (Clock, CLK)** umschaltet, wenn der Eingang **T = 1** ist.

> [!tip] **Wahrheitstabelle:**
| T   | $Q(n)$ | $Q(n+1)$                |
| --- | ---- | --------------------- |
| 0   | $Q(n)$ | $Q(n)$ (keine Änderung) |
| 1   | 0    | 1 (Toggle)            | 
| 1   | 1    | 0 (Toggle)            |
> 
> - **T = 0**: Kein Wechsel, Zustand bleibt erhalten.
> - **T = 1**: Ausgang toggelt bei jeder Taktflanke.
> - **Dient als Frequenzteiler**, da es die Taktrate halbiert.
> - **Kann aus einem JK-FlipFlop** mit J = K = 1 abgeleitet werden.
>
> ![[T Flip-Flop Zeichnung]]

