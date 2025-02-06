[[Latches und Flip-flops]]

---

> [!check] Definition
> Ein **JK-FlipFlop** ist ein bistabiles Speicher-Element mit zwei Eingängen **J** (Jump [set]) und **K** (Kill [reset]), das als **erweiterte Form des SR-FlipFlops** gilt und den verbotenen Zustand vermeidet.

> [!tip] **Wahrheitstabelle:**
| J   | K   | $Q(n+1)$                       |
| --- | --- | ---------------------------- |
| 0   | 0   | $Q(n)$ (keine Änderung)        | 
| 0   | 1   | 0 (Reset)                    |
| 1   | 0   | 1 (Set)                      |
| 1   | 1   | **$Q(n)$ invertiert** (Toggle) |
> 
> - **Taktgesteuert** (synchron)
> - **Toggelt** bei J = K = 1
> - **Dient als Frequenzteiler** bei J = K = 1
>
> ![[JK Flip-Flop Bild.png]]
