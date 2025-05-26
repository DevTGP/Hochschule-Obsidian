[[Digitalisierung]]

---

> [!check] Definition  
> Aliasing ist ein Störeffekt bei der Digitalisierung, bei dem hochfrequente Signalanteile fälschlich als niedrigere Frequenzen interpretiert werden.

> [!info] Ursache  
> Tritt auf, wenn ein Signal mit einer Abtastrate kleiner als das Doppelte seiner höchsten Frequenz (Nyquist-Grenze) digitalisiert wird. Das Signal wird dann falsch rekonstruiert.

> [!example] Typen von Fehlern
>
> -   **Audio**: hohe Töne werden zu tiefen Tönen
> -   **Bild**: Treppen- oder Moiré-Effekt
> -   **Video**: Räder drehen scheinbar

> [!warning] Vermeidung  
> Aliasing lässt sich vermeiden durch:
>
> -   Abtastrate > $2  \cdot f_{max}$ ([[Abtasttheorem]])
> -   Tiefpassfilter vor der Digitalisierung (Anti-Aliasing-Filter)
