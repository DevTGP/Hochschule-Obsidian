[[Kompression & Kodierungen]]

---

> [!check] Definition  
> Eine Kodierung ist **präfixfrei**, wenn kein Codewort der Anfang eines anderen ist.

> [!info] Funktionsweise
>
> Gewährleistet **eindeutige Dekodierung** bei variabler Wortlänge
>
> Beispiel:
>
> -   gültig: `0`, `10`, `110` (keines beginnt mit einem anderen)
> -   ungültig: `0`, `01` → nicht eindeutig
>
> ![[Fano-Bedingung_Anhang_1.png]]

> [!example] Eigenschaften
>
> -   Notwendig für **verlustfreie** Kodierung
> -   Wird z. B. bei **[[Huffmann-Kodierung]]** eingehalten
> -   Alternativ wären explizite Trennzeichen nötig (wie bei Morse-Code)

> [!abstract] Beispiel
>
> | Zeichen $a$       | A   | B   | C   | D   |
> | ----------------- | --- | --- | --- | --- |
> | Codierung $c_{1}$ | 00  | 01  | 10  | 11  |
> | Codierung $c_{2}$ | 0   | 10  | 110 | 111 |
>
> $\to$ Kodierung $c_{2}$ erfüllt die Fano-Bedingung
