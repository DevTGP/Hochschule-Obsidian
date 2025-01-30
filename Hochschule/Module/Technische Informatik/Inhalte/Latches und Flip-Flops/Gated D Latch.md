[[Latches und Flip-flops]]

---

> [!check] Definition
> Ein **Gated D-Latch** ist ein **D-Latch** mit einer zusätzlichen **Taktsteuerung (Enable, E)**, die bestimmt, wann der Ausgang **Q** aktualisiert wird.

> [!tip] **Wahrheitstabelle:**
| E   | D   | $Q(n+1)$           |
| --- | --- | ------------------ |
| 0   | X   | $Q(n)$ (Speichern) |
| 1   | 0   | 0                  |
| 1   | 1   | 1                  |
> 
> - **E = 1**: Q folgt D (Transparenz)
> - **E = 0**: Q bleibt konstant (Speicherung)
> - **Verhindert Glitches**, da Änderungen nur bei E = 1 möglich sind
> - Grundlage für **D-FlipFlops**
>
> ![[Gated D Latch Zeichnung]]
