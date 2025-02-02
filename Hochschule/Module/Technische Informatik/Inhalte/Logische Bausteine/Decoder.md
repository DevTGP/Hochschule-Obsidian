[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Decoder** ist eine digitale Schaltung, die eine **kodierte Eingabe in eine eindeutige Ausgangskombination** umwandelt.

> [!info] Funktion
> **Funktionsweise:**
> - **Eingangssignale**: Der Decoder erhält eine **n-Bit-Steuerleitung**.
> - **Adressierung der Ausgänge**: Es gibt **$2^n$ Ausgänge**, wobei genau **einer aktiv (HIGH)** ist.
> - **Binärzuordnung**: Jeder mögliche Eingangswert aktiviert genau einen Ausgang.
>
> **Beispiel: 3-zu-8-Decoder**
> - **Eingänge**: $S_{0}, S_{1}, S_{2}$
> - **Ausgänge**: $Y_{0}, Y_{1}, Y_{2}, Y_{3}, Y_{4}, Y_{5}, Y_{6}, Y_{7}$
> - **Funktion**: Der gesetzte Binärwert wählt einen aktiven Ausgang:
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
> - **Eingänge**: n Steuerbits.
> - **Ausgänge**: $2^n$ verschiedene Signale.
> - **Aktiver Ausgang**: Nur einer ist aktiv (HIGH), alle anderen sind LOW.
>
> ![[Decoder Bild.png]]
