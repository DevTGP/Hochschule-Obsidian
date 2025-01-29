[[Minimierungstechniken]]

---

> [!check] Definition
> Ein **Karnaugh-Diagramm (K-Map)** ist eine tabellarische Darstellung einer booleschen Funktion zur visuellen Minimierung logischer Ausdrücke.
> - Es ordnet Wahrheitswerte in einer **2D-Tabelle** an, wobei benachbarte Felder sich nur in **einem Bit** unterscheiden.
> - Einsen werden gruppiert in **Potenzen von 2** (1, 2, 4, 8 …), um Terme zu reduzieren.
> - Ziel: Eine **minimale disjunktive Normalform (DNF)** oder **konjunktive Normalform (KNF)** zu finden.

> [!example]
>> [!note]- 2 Variablen
>> Ausdruck im [[Sum of Products]]: $AB + \overline{A}B + \overline{AB}$
>> 
| /              | $A$ | $\overline{A}$ |
| -------------- | --- | -------------- |
| $B$            | 1   | 1              |
| $\overline{B}$ | 0   | 1               |
>>  Ausdruck nach Karnaugh: $\overline{A} + B$
>
>> [!note]- 3 Variablen
>> Ausdruck im [[Sum of Products]]: $A\overline{B}C + A\overline{BC} + \overline{AB}C + \overline{A}BC$
>> 
| /              | $A$ | $A$            | $\overline{A}$ | $\overline{A}$ |
| -------------- | --- | -------------- | -------------- | -------------- |
| /              | $B$ | $\overline{B}$ | $\overline{B}$ | $B$            |
| $C$            | 0   | 1              | 1              | 1              |
| $\overline{C}$ | 0   | 1              | 0              | 0              | 
>>  Ausdruck nach Karnaugh: $A\overline{B} + \overline{A}C$
>
>> [!note]- 4 Variablen
>> Ausdruck im [[Sum of Products]]: $A\overline{B}CD + A\overline{B}C\overline{D} + A\overline{BCD} + A\overline{BC}D + \overline{AB}CD + \overline{AB}C\overline{D} + \overline{A}BCD + \overline{A}BC\overline{D}$
>> 
| /              | /              | $A$ | $A$            | $\overline{A}$ | $\overline{A}$ |
| -------------- | -------------- | --- | -------------- | -------------- | -------------- |
| /              | /              | $B$ | $\overline{B}$ | $\overline{B}$ | $B$            |
| $C$            | $D$            | 0   | 1              | 1              | 1              |
| $C$            | $\overline{D}$ | 0   | 1              | 1              | 1              |
| $\overline{C}$ | $\overline{D}$ | 0   | 1              | 0              | 0              |
| $\overline{C}$ | $D$            | 0   | 1              | 0              | 0              |
>>  Ausdruck nach Karnaugh: $A\overline{B} + \overline{A}C$
