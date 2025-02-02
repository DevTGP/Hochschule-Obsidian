[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Multiplexer (MUX)** ist eine digitale Schaltung, die **einen von mehreren Eingängen** auswählt und an den Ausgang weiterleitet.

> [!info] Funktion
> **Funktionsweise:**
> - Die **Steuerleitungen** bestimmen, welcher Eingang zum Ausgang durchgeschaltet wird.
> - Bei **n Steuerleitungen** können **$2^n$ Eingänge** adressiert werden.
>
> **Beispiel: 4:1-Multiplexer**
> - **Eingänge**: $D_{0}, D_{1}, D_{2}, D_{3}$
> - **Steuerleitungen**: $S_{0}, S_{1}$
> - **Ausgang**: $Y = DS_{1}S_{0}$

> [!tip] Aufbau
> - **Daten-Eingänge**: Mehrere (z. B. 2, 4, 8, 16).
> - **Steuerleitungen**: Wählen den aktiven Eingang aus.
> - **Ausgang**: Gibt das Signal des gewählten Eingangs aus.
>
> ![[Multiplexer Bild.png]]
