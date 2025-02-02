[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Volladdierer** ist eine digitale Schaltung, die **drei Binärwerte** (zwei Operanden und einen Eingangsübertrag) addiert.

> [!info] Funktion
> - Wird in **ALUs und Prozessoren** für **mehrstellige Addition** verwendet.
> - Kann zu **n-Bit-Addierern** kaskadiert werden.
>
| A   | B   | $C_{in}$ | Summe (S) | $C_{out}$ |
| --- | --- | ---- | --------- | ----- |
| 0   | 0   | 0    | 0         | 0     |
| 0   | 0   | 1    | 1         | 0     |
| 0   | 1   | 0    | 1         | 0     |
| 0   | 1   | 1    | 0         | 1     |
| 1   | 0   | 0    | 1         | 0     |
| 1   | 0   | 1    | 0         | 1     |
| 1   | 1   | 0    | 0         | 1     |
| 1   | 1   | 1    | 1         | 1     |

> [!tip] Aufbau
> **Eingänge:**
> - **A** (erstes Bit)
> - **B** (zweites Bit)
> - **$C_{in}$** (Eingangsübertrag)
> 
> **Ausgänge:**
> - **Summe (S)** = $A \oplus B \oplus C_{in} (XOR)$
> - **Übertrag ($C_{out}$)** = $(A \wedge B) \vee (C_{in} \wedge (A \oplus B))$
>
> ![[Volladdierer Bild.png]]
