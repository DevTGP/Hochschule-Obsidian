[[Latches und Flip-flops]]

---

> [!check] Definition
> Ein **SR-Latch** ist ein **bistabiles** Speicher-Element mit **Set (S)** und **Reset (R)** Eingängen. Es kann **asynchron** oder **getaktet (synchron)** sein.

> [!tip] **Wahrheitstabelle:**
| S   | R   | $Q(n+1)$       | Bedeutung          |
| --- | --- | ------------ | ------------------ |
| 0   | 0   | $Q(n)$         | Speichern          |
| 0   | 1   | 0            | Reset              |
| 1   | 0   | 1            | Set                |
| 1   | 1   | **Ungültig** | Instabiler Zustand |
> 
> - **Asynchrones Speicherelement**
> - **Problem:** S = R = 1 ist **nicht definiert**
> - Wird oft mit **Enable-Signal (E)** zu einem **gesteuerten SR-Latch** erweitert>
>
> ![[SR Latch Zeichnung]]
