[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Halbaddierer** ist eine digitale Schaltung, die zwei **einstellige Binärzahlen** addiert, ohne einen vorherigen Übertrag zu berücksichtigen.

> [!info] Funktion
> - Grundbaustein für den **[[Voll-Addierer]]**.
>
| A   | B   | Summe (S) | Übertrag (C) |
| --- | --- | --------- | ------------ |
| 0   | 0   | 0         | 0            |
| 0   | 1   | 1         | 0            |
| 1   | 0   | 1         | 0            |
| 1   | 1   | 0         | 1            |

> [!tip] Aufbau
> **Eingänge:**
> - **A** (erstes Bit)
> - **B** (zweites Bit)
> 
> **Ausgänge:**
> - **Summe (S)** = $A \oplus B$ (XOR)
> - **Übertrag / Carry-Out (C)** = $A \wedge B$ (AND)
>
> ![[Halb-Addierer Bild.png]]
