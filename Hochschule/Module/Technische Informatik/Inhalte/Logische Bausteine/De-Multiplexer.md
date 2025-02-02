[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Demultiplexer (DEMUX)** ist eine digitale Schaltung, die **ein Eingangssignal auf einen von mehreren Ausgängen verteilt**.

> [!info] Funktion
> **Funktionsweise:**
> - **Eingangssignal (D)**: Ein einzelnes Datenbit oder Signal.
> - **Steuerleitungen (n Bit)**: Bestimmen, welcher Ausgang aktiv ist.
> - **Ausgänge ($2^n$ Stück)**: Genau einer erhält das Eingangssignal, alle anderen sind **0**.
>
> **Beispiel: 1-zu-4-Demultiplexer**
> - **Eingang**: D
> - **Steuerleitungen**: $S_{0},S_{1}$
> - **Ausgänge**: $D_{0}, D_{1}, D_{2}, D_{3}$
> - **Funktion**:
>     - $S_{1} S_{0} = 00 \to D$ auf $D_{0}$
>     - $S_{1} S_{0} = 01 \to D$ auf $D_{1}$
>     - $S_{1} S_{0} = 10 \to D$ auf $D_{2}$
>     - $S_{1} S_{0} = 11 \to D$ auf $D_{3}$

> [!tip] Aufbau
> - **Eingang (Datenleitung)**: Ein einzelnes Signal.
> - **Steuerleitungen**: Wählen den aktiven Ausgang.
> - **Ausgänge**: Mehrere (z. B. 2, 4, 8, 16).
>
> ![[De-Multiplexer Bild.png]]
