[[Digitalisierung]]

---

> [!check] Definition
> Das **Abtasttheorem** (auch **Nyquist-Shannon-Abtasttheorem**) ist ein zentrales Prinzip der digitalen Signalverarbeitung.
>
> Ein **analoger** Signalverlauf kann **verlustfrei** rekonstruiert werden, wenn er mit einer **Abtastfrequenz** $f_{A}$ abgetastet wird, die **mindestens doppelt so groß** ist wie die **höchste Frequenz** $f_{max}$ im Signal.
>
> **Formel:**
>
> > $f_A > 2 \cdot f_{max}$

> [!info]
> Das Abtasttheorem garantiert, dass man ein kontinuierliches Signal exakt digitalisieren kann, **ohne Informationsverlust**, solange die Abtastung schnell genug erfolgt.

> [!error] Folge bei Verletzung:
> Wenn $f_{A} \leq 2 \cdot f_{max}$, tritt [[Unterabtastung oder Aliasing]] auf → das rekonstruierte Signal enthält Verzerrungen oder falsche Frequenzen.
