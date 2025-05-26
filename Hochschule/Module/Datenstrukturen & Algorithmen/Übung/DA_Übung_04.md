![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_04.excalidraw.md#^area=vePLBDKmFbeuDIqcfP4GX|100%]]

a)
Exponentialfunktion

$f(n) = 2^n$

b)
Beispiel für $n=2$

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_04Notation.excalidraw.md#^area=uB6Al9yi8-Ocpna4sDObz|100%]]

$$
T(n) = \begin{cases}
1 & \text{, falls }n=0 \\
2 \cdot T(n-1)+1 & \text{, sonst}
\end{cases}
$$

$T(n) = 2^{n+1}-1$

c)

$T_{\geq}(n) = 2^{n+1}-1$
$T_{+}(n) = 2^{n+1}-1-2^{n}=2^{n}-1$

$T_{\geq+}(n) = 2^{n+1}-1+2^{n}-1=2^{n+1}+2^{n}-2$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_04.excalidraw.md#^area=oS5X66nrCXX262hcPt7f_|100%]]

i)
ii)

```python
def add(x, y):
	if x == 0:
		return y
	return 1 + add(x - 1, y)

print(add(3, 4))

def add2(x, y):
	if x == 0:
		return y
	return add(x - 1, y + 1)

print(add2(3, 4))

def mult(x, y):
	if x == 0:
		return 0
	return y + mult(x - 1, y)

print(mult(3, 4))

def mult2(x, y, acc = 0):
	if x == 0:
		return acc
	return mult2(x - 1, y, acc+y)

print(mult2(3, 4))
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_04.excalidraw.md#^area=d43O7466V2PCI70kq2Bqq|100%]]

a)
$\text{delete: list x elem } \to \text{ list}$

$\text{delete(emtpy, e) = empty}$
$\text{delete(append(empty, e), e) = empty}$
$\text{delete(append(l, e), e) = l}$
$\text{delete(append(l, x), e) = append(delete(l, e), x) | , falls }x\neq e$

b)
$\text{last: list } \to \text{ elem}$

$\text{last(append(empty, e)) = e}$
$\text{last(append(l, e)) = e}$

c)
$\text{find: list x elem} \to \text{ elem}$

$\text{previous(empty, e) = Fehler / n.d.}$
$\text{previous(append(l, e), e) = last(l)}$
$\text{previous(append(l, x), e) = previous(l, e) | , falls }x \neq e$
$\text{previous(append(empty, e), e) = Fehler}$

d)
$\text{previous: list x elem} \to \text{ elem}$

$\text{find(empty, e) = Fehler}$
$\text{find(append(empty, e), e) = e}$
$\text{find(append(l, e), e) = e}$
$\text{find(append(l, x), e) = find(l, e) | , falls}x \neq e$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_04.excalidraw.md#^area=t3ANEoYvF4hVqYWxMv-A1|100%]]

a)

b)
$\text{delete(insert(insert(insert(insert(create, a), b), c), d), s1) | wobei key(d), key(b) == s2 und key(c), key(a) = s1}$
$\text{insert(delete(insert(insert(insert(create, a), b), c), s1), d)}$
$\text{insert(delete(insert(insert(create, a), b), s1), d)}$
$\text{insert(insert(delete(insert(create, a), s1), b), d)}$
$\text{insert(insert(delete(create, s1), b), d)}$
$\text{insert(insert(create, s1), b), d)}$

c)
$\text{readp(insert(insert(insert(insert, a), b), c), d), 2}$
$\text{readp(insert(insert(insert, a), b), c), 2}$

d)
$\text{readp(delete(insert(insert(insert(insert(create, a), b), c), d), s1), 2)}$
$\text{readp(insert(insert(create, b), d), 2)}$
$\text{readp(insert(create, b) 2)}$

e)
$\text{readp(insert(create, a), 2)}$
$\text{readp(create, 1) = Fehler}$
