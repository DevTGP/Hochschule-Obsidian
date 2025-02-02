[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Encoder** ist eine digitale Schaltung, die eine **aktive Eingangssignalkombination in einen binären Code umwandelt**.

> [!info] Funktion
> **Funktionsweise:**
> - **Eingänge ($2^n$ Stück)**: Genau **ein Eingang ist aktiv (HIGH)**.
> - **Ausgänge (n Bit)**: Der binäre Wert des aktiven Eingangs wird ausgegeben.
> - **Kodierung**: Jeder Eingang hat eine eindeutige **binäre Repräsentation**.
>
> **Beispiel: 8-zu-3-Encoder**
> - **Eingänge**: $Y_{0}, Y_{1}, Y_{2}, Y_{3}, Y_{4}, Y_{5}, Y_{6}, Y_{7}$
> - **Ausgänge**: $S_{0}, S_{1}, S_{2}$
> - **Funktion**:
>
| $S_{2}$ | $S_{1}$ | $S_{0}$    | $Y_{7}$ | $Y_{6}$ | $Y_{5}$ | $Y_{4}$ | $Y_{3}$ | $Y_{2}$ | $Y_{1}$ | $Y_{0}$ |
| ------- | ------- | --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 0       | 0       | 0   | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 1       |
| 0       | 0       | 1   | 0       | 0       | 0       | 0       | 0       | 0       | 1       | 0       |
| 0       | 1       | 0   | 0       | 0       | 0       | 0       | 0       | 1       | 0       | 0       |
| 0       | 1       | 1   | 0       | 0       | 0       | 0       | 1       | 0       | 0       | 0       |
| 1       | 0       | 0   | 0       | 0       | 0       | 1       | 0       | 0       | 0       | 0       |
| 1       | 0       | 1   | 0       | 0       | 1       | 0       | 0       | 0       | 0       | 0       |
| 1       | 1       | 0   | 0       | 1       | 0       | 0       | 0       | 0       | 0       | 0       |
| 1       | 1       | 1   | 1       | 0       | 0       | 0       | 0       | 0       | 0       | 0       |

> [!tip] Aufbau
> - **Eingänge**: Mehrere Leitungen (z. B. $2^n$ Eingänge).
> - **Ausgänge**: n Bit, die die aktivierte Eingangsnummer kodieren.
>
> ![[Encoder Bild.png]]
