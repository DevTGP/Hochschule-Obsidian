[[Kompression & Kodierungen]]

---

> [!check] Definition  
> **Lauflängenkodierung (Run Length Encoding, RLE)** ist ein universelles, verlustfreies Kompressionsverfahren, das gleiche aufeinanderfolgende Zeichen (Läufe) durch ein einziges Zeichen-Zähler-Paar ersetzt. Besonders effektiv ist sie bei Daten mit vielen langen Wiederholungen – wie sie z. B. in einfachen Bilddaten oder Texten mit Leerstellen vorkommen.

> [!info]  
> RLE ist einfach zu implementieren, arbeitet unabhängig von Wahrscheinlichkeiten (nicht informationsbasiert) und kann bei ungeeigneten Daten die Datenmenge sogar vergrößern. Die praktische Effizienz hängt vom verwendeten Byte-Format und den Dateninhalten ab. Oft werden Begrenzungen wie max. 256 für Zählerwerte eingeführt, um Platz zu sparen.

> [!example] Varianten & Besonderheiten
>
> -   Wird in vielen Formaten (BMP, TIFF, Faxübertragung, teilweise JPEG) als Teilschritt eingesetzt
> -   Byte-orientiert: meist 1 Byte für Zeichen, 1 Byte für Zähler
> -   Effektiv bei langen, homogenen Zeichenfolgen
> -   Nicht geeignet bei hochgradig wechselnden Daten

> [!abstract] Beispiele
> Beim Faxen werden große weiße Flächen durch z. B. `<weiß,172>` kodiert, statt $172$-mal das gleiche Zeichen zu übertragen – das spart erheblich Bandbreite.
>
> Aus $ABABAB$ wird $<A,1><B,1><A,1><B,1><A,1><B,1>$
