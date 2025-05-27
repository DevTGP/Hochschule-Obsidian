[[Kompression & Kodierungen]]

---

> [!check] Definition  
> Ein universelles, verlustfreies Kompressionsverfahren, das häufige Zeichen kürzer codiert und seltene länger.

> [!info] Funktionsweise
>
> -   Ausgangspunkt: bekannte Zeichen & Wahrscheinlichkeiten
> -   Häufige Zeichen bekommen kurze Codes, seltene lange
> -   Bottom-up-Erstellung eines **Codebaums**:
>     1. Zwei Zeichen mit kleinster Wahrscheinlichkeit zu Knoten verbinden
>     2. Neue Wahrscheinlichkeit ist die Summe
>     3. Wiederholen, bis nur noch ein Baum
> -   Ergebnis: Präfixfreie, binäre Codierung → eindeutig dekodierbar

> [!example] Eigenschaften und Voraussetzungen
>
> -   **Verlustfrei**
> -   **Präfixfrei** ([[Fano-Bedingung]])
> -   **Optimal** für bekannte Häufigkeiten
> -   **Dekodierung** über Traversieren des Baums

> [!abstract] Beispiel
> ![[Huffmann-Kodierung_Anhang_1.png]]
>
> -   Eine Nachricht, die sich an die gegebene Häufigkeitsverteilung hält: `ABABACADAABACDBA` (Länge: $16$)
>
> | Zeichen $a$       | A   | B   | C   | D   |
> | ----------------- | --- | --- | --- | --- |
> | Codierung $c_{1}$ | 00  | 01  | 10  | 11  |
> | Codierung $c_{2}$ | 0   | 10  | 110 | 111 |
>
> -   Kodierung $c_{1}$: $16$ Zeichen á $2 Bit$ = $32 Bit$
> -   Huffman-Kodierung $c_{2}$: $0100100110011100100110111100$ $28 Bit$, d.h. $12.5\%$ Kompression
