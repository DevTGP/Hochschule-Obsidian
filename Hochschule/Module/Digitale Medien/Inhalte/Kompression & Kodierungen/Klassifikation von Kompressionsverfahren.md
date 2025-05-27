[[Kompression & Kodierungen]]

---

> [!check] Definition  
> Kompressionsverfahren werden nach Anwendbarkeit (spezifisch/universell) und Datenwiederherstellbarkeit (verlustfrei/verlustbehaftet) eingeteilt.

> [!info] Einteilung
>
> 1. **Speziell**: Nur für bestimmte Medientypen nutzbar, da sie medientypische Eigenschaften ausnutzen (z. B. MP3 → Audio).
> 2. **Universell**: Für beliebige Datenarten anwendbar (z. B. ZIP).
> 3. **Verlustfrei**: Originaldaten können exakt rekonstruiert werden.
> 4. **Verlustbehaftet**: Nicht alle Informationen werden gespeichert; Kompression ist effektiver, aber mit Qualitätsverlust.

> [!example] Beispiele
>
> -   **Speziell & verlustbehaftet**: MP3, JPEG
> -   **Speziell & verlustfrei**: FLAC, PNG, AIFF
> -   **Universell & verlustbehaftet**: kaum genutzt
> -   **Universell & verlustfrei**: ZIP, [RLE](Lauflängenkodierung.md), [[Huffmann-Kodierung]], [[LZW-Kodierung]]

> [!warning] Hinweis  
> Verlustbehaftete Verfahren eignen sich für Medien, bei denen kleine Unterschiede für den Menschen kaum wahrnehmbar sind (z. B. Audio, Bild).
