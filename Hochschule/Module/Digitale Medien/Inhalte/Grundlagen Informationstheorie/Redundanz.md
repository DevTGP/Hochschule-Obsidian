[[Grundlagen Informationstheorie]]

---

> [!check] Definition  
> Redundanz misst den „überflüssigen“ Teil einer Nachricht, der entfernt werden kann, ohne den Informationsgehalt zu verlieren.

> [!info] Funktionsweise  
> Eine Kodierung ist redundant, wenn die durchschnittliche [[Wortlänge]] $L$ größer ist als die [[Entropie]] $H$:  
> $R = L - H$  
> Je kleiner $R$, desto effizienter ist die Kodierung. Bei optimaler Kodierung ist $R = 0$.

> [!list] Varianten und Aspekte
>
> -   Redundanz $= 0 \to$ optimale Kodierung
> -   Redundanz $> 0 \to$ Platzverschwendung, aber mögliche Fehlerkorrektur
> -   Fehlerkorrigierende Codes (Paritätsbit, CRC) erhöhen bewusst RR

> [!example] Beispielrechnung
>
> -   Wenn $H=1,75, L=2$, dann $R=0,25$.
> -   Wenn $H=1,75, L=1,75$, dann $R = 0 \to$ optimal.
