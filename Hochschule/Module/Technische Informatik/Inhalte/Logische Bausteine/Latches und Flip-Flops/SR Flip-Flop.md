[[Latches und Flip-flops]]

---

> [!check] Definition
> Ein **SR-FlipFlop** ist ein **bistabiles** Speicher-Element mit zwei Eingängen **S (Set)** und **R (Reset)**.

> [!tip] **Wahrheitstabelle:**
| S   | R   | $Q(n+1)$                          | 
| --- | --- | --------------------------------- |
| 0   | 0   | $Q(n)$ (keine Änderung)           |
| 0   | 1   | 0 (Reset)                         |
| 1   | 0   | 1 (Set)                           |
| 1   | 1   | **Ungültig** (instabiler Zustand) |
> 
> - **Speichert 1 oder 0**, bis ein neuer Impuls kommt
> - **Asynchron oder Taktgesteuert (synchrones SR-FlipFlop)**
> - **Problem:** S = R = 1 ist nicht definiert
>  
> ![[SR Flip-Flop Bild.png]]
