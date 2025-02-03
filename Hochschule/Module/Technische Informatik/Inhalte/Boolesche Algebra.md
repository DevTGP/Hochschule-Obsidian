[[Technische Informatik]]

---

> [!check] Definition
> Die boolesche Algebra ist ein mathematisches System zur Verarbeitung logischer Werte (0 und 1) mit Operatoren wie **UND (∧), ODER (∨), NICHT (¬)**. Sie wird in der Digitaltechnik und Schaltalgebra verwendet.

> [!tip] Darstellung
> - **UND (AND):** $A \cdot B$ oder $A \land B$
> - **ODER (OR):** $A+B$ oder $A \lor B$
> - **NICHT (NOT):** $\overline{A}$ oder $\neg A$
> - **XOR:** $A \oplus B$
> - **NAND:** $\overline{A \cdot B}$
> - **NOR:** $\overline{A + B}$
>
> Dabei gibt es vor allem 2 Darstellungsformen
> - [[Sum of Products]]
> - [[Product of Sums]]

> [!example] Inhaltsverzeichnis
> 1. [[Additionsregeln]]
> 2. [[Multiplikationsregeln]]
> 3. [[Algebraische Umformungen]]
> 4. [[Minimierungstechniken]]

> [!error] Übersicht der Regeln
| Op mit 0                       | $A + 0 = A$                                 | $0A =0$                                   |
| ------------------------------ | ------------------------------------------- | ----------------------------------------- |
| Op mit 1                       | $A+1=1$                                     | $1A=A$                                    |
| Idempotenz                     | $A+A=A$                                     | $AA=A$                                    |
| Komplementär                   | $A+\overline{A}=1$                          | $A\overline{A}=0$                         |
| Doppelte Negation / Involution | $\overline{\overline{A}}=A$                 |                                           |
| Kommutativgesetze              | $A+B=B+A$                                   | $AB=BA$                                   |
| Assoziativgesetze              | $A+(B+C)=(A+B)+C$                           | $A(BC)=(AB)C$                             |
| Distributivgesetz              | $A(B+C)=AB+AC$                              |                                           |
| DeMorgansche Regeln            | $\overline{AB} = \overline{A}+\overline{B}$ | $\overline{A}+\overline{B}=\overline{AB}$ |
| Vereinfachungen                | $A+AB=A$                                    |                                           |
| Vereinfachungen                | $A+\overline{A}B=A + B$                                    |                                           |
| Vereinfachungen                | $(A+B)(A+C)=A+BC$                                    |                                           |
