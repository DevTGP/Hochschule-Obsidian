[[Latches und Flip-flops]]

---

> [!check] Definition
> Ein **Gated SR-Latch** ist ein **SR-Latch mit einer zusätzlichen Taktsteuerung (Enable, E)**, die bestimmt, wann Änderungen möglich sind.

> [!tip] **Wahrheitstabelle:**
| E   | S   | R   | $Q(n+1)$       | Bedeutung      |
| --- | --- | --- | ------------ | -------------- |
| 0   | X   | X   | $Q(n)$         | Speichern      |
| 1   | 0   | 0   | $Q(n)$         | Keine Änderung |
| 1   | 0   | 1   | 0            | Reset          |
| 1   | 1   | 0   | 1            | Set            |
| 1   | 1   | 1   | **Ungültig** | Instabil       | 
>
> - **E = 0**: Speichert den letzten Zustand.
> - **E = 1**: Funktioniert wie ein normales SR-Latch.
> - **Problem**: S = R = 1 bleibt **undefiniert**.
> - **Verwendet in synchronen Schaltungen**, um unkontrollierte Änderungen zu verhindern.
>
> ![[Gated SR Latch Zeichnung]]
