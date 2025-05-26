![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_03.excalidraw.md#^area=J4H4MW3a8iNosuM5CxdVa|100%]]

i)
Richtig,
Konstanten sind per Definition in $O(1)$, da sie unabhängig von $n$ sind.

ii)
Richtig,
$n \cdot(n-1)=n^{2}-n \leq n^{2} \in O(n)$

iii)
Richtig,
$2^{n} \leq 3^{n}\in O(3^{n})$

iv)
Falsch,
$3^{n} \not\in O(2^{n})$
$3^{n}$ ist per Definition größer als $2^{n}$

v)
Falsch,
$2^{n} \not\in O(n^{7})$
$2^{n}$ ist per Definition größer als $n^{2}$ und somit $n^{7}$

vi)
Richtig,
$(n+1)! = (n+1) \cdot n! \in O(n!)$

vii)
Richtig,
$\sum_{i=0}^{n}(2i+1) = (n+1)\cdot(n+1) = (n+1)^{2}\in O(n^{2})$

viii)
,
$\sum_{i=0}^{n}i^{k} = (n+1) \cdot \frac{n}{2}^{k}\in O(n^{k+1})$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_03.excalidraw.md#^area=VjZx9i1KNBNe2kUa1f0Ne|100%]]

```python
def fakultaet(n, akku=1):
    if n == 0:
        return akku
    return fakultaet(n - 1, n * akku)

print(fakultaet(3))
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_03.excalidraw.md#^area=AcCrXEZIoJkIMy86xFWVh|100%]]

```python
def anagramme(wort):
    if len(wort) <= 1:
        return [wort]

    ergebnisse = []
    for i, buchstabe in enumerate(wort):
        rest = wort[:i] + wort[i+1:]
        for perm in anagramme(rest):
            ergebnisse.append(buchstabe + perm)

    return ergebnisse

print(anagramme("cat"))
```
