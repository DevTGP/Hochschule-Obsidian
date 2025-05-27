[[Kompression & Kodierungen]]

---

> [!check] Definition  
> **Lempel-Ziv-Welch-Kodierung (LZW)** ist ein universelles, verlustfreies Kompressionsverfahren, das Zeichenfolgen durch Indizes in ein dynamisch wachsendes Wörterbuch ersetzt. Die Methode erkennt wiederkehrende Muster in der Eingabe und ersetzt sie zunehmend durch kürzere Referenzen auf zuvor gespeicherte Teilwörter, wodurch längere Daten effizient komprimiert werden können.

> [!info] Funktionsweise
> LZW arbeitet zeichenorientiert und ohne Kenntnis der Wahrscheinlichkeiten. Das Verfahren startet mit einem Wörterbuch der Einzelzeichen (z. B. ASCII) und erweitert es während der Kodierung durch neue Kombinationen. Die Dekodierung erfolgt synchron durch identischen Aufbau des Wörterbuchs.

> [!example] Eigenschaften und Varianten
>
> -   Entwickelt aus LZ78, verbessert von Welch (1984)
> -   Bildet Basis vieler Formate (GIF, TIFF, PDF, frühere UNIX-Kompression)
> -   Symmetrisch und effizient, aber patentgeschützt bis 2006
> -   Nicht geeignet bei sehr kurzlebigen oder nicht wiederholenden Datenmustern

> [!abstract] Pseudocode & Beispiel
> ![[LZW-Kodierung_Anhang_1.png]]
>
> -   Nachricht: `bananenanbau` $(98, 97, 110, 97, 110, 101, 110, 97, 110, 98, 97, 117)$
> -   Wörterbuch an den Indizes $0-127$ mit [[ASCII Tabelle]] vorbesetzt, Indizes $128-255$ ungenutzt
>     ![[LZW-Kodierung_Anhang_2.png]]
> -   Kodierte Nachricht: $98, 97, 110, 257, 101, 258, 110, 256, 117$
