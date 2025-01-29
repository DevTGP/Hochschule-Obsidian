[[Fließkomma IEEE 754]]

---

> [!info] IEEE 754 Representation
| Funktion                      | Sign | Exponent  | Mantissa                     |
| ----------------------------- | ---- | --------- | ---------------------------- |
| Null                          | 0    | 0000 0000 | 000 0000 0000 0000 0000 0000 |
| Negativ Null                  | 1    | 0000 0000 | 000 0000 0000 0000 0000 0000 |
| Eins                          | 0    | 0111 1111 | 000 0000 0000 0000 0000 0000 |
| Minus Eins                    | 1    | 0111 1111 | 000 0000 0000 0000 0000 0000 |
| Kleinste denormalisierte Zahl | *    | 0000 0000 | 100 0000 0000 0000 0000 0000 |
| Größte denormalisierte Zahl   | *    | 0000 0000 | 111 1111 1111 1111 1111 1111 |
| Kleinste normalisierte Zahl   | *    | 0000 0001 | 000 0000 0000 0000 0000 0000 |
| Größte normalisierte Zahl     | *    | 1111 1110 | 111 1111 1111 1111 1111 1111 |
| Positiv Unendlich             | 0    | 1111 1111 | 000 0000 0000 0000 0000 0000 |
| Negativ Unendlich             | 1    | 1111 1111 | 000 0000 0000 0000 0000 0000 |
| NaN                           | *    | 1111 1111 | nicht Null                   |
^main