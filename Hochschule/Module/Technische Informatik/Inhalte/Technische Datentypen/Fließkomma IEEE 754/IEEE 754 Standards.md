[[Fließkomma IEEE 754]]

---

> [!quote] IEEE 754 Standards
| Typ                      | Größe<br>(1+r+p) | Exponent <br>(r) | Mantisse <br>(p) | Werte des Exponenten <br>(e) | Biaswert<br>(B) |
|:------------------------ | ----------------:| ----------------:| ----------------:| ----------------------------:| ---------------:|
| single                   |           32 bit |            8 bit |           23 bit |       $-126 \leq e \leq 127$ |             127 |
| double                   |           64 bit |           11 bit |           52 bit |     $-1022 \leq e \leq 1023$ |            1023 |
| single extended          |    $\geq 43$ bit |    $\geq 11$ bit |    $\geq 31$ bit |                              |                 |
| double extended          |    $\geq 79$ bit |    $\geq 15$ bit |    $\geq 63$ bit |                              |                 |
| single extended, minimum |           43 bit |           11 bit |           31 bit |     $-1022 \leq e \leq 1023$ |            1023 |
| double extended, minimum |           79 bit |           15 bit |           63 bit |   $-16382 \leq e \leq 16383$ |           16383 |
