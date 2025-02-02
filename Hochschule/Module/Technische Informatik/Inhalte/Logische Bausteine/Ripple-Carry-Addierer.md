[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Ripple-Carry-Addierer (RCA)** ist eine digitale Schaltung, die **mehrere [[Volladdierer]] kaskadiert**, um **mehrstellige Binärzahlen** zu addieren.

> [!info] Funktion
> 1. Die niederwertigsten Bits (LSB) werden mit einem **Eingangsübertrag $C_{0}$ = 0** addiert.
> 2. Jeder Volladdierer berechnet eine **Summe** und gibt einen **Carry-Out** an den nächsten Addierer weiter.
> 3. Das höchste Carry-Out gibt den Übertrag für eine **n+1-Bit-Summe** an.

> [!tip] Aufbau
> - Besteht aus **n Volladdierern**, wobei der **Übertrag (Carry-Out) eines Addierers** als **Carry-In des nächsten Addierers** dient.
>
> ![[Ripple-Carry-Addierer Bild.png]]

> [!bug] **Problem:**
> - Die **Berechnungszeit steigt linear mit der Bit-Anzahl**, da jeder Addierer auf den Carry des vorherigen warten muss (**Ripple-Effekt**).
