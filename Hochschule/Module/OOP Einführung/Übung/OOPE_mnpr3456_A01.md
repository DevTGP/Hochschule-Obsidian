`Matrikelnummer: 982773`

![[OOPE_Abgabe_01.excalidraw#^area=-78si3DwJPR0PURt9xK2t|100%]]

# 1)

```java
c = b % a * 9; // a=76, b=37, c=18
a++; // a=77, b=37, c=18
b--; // a=77, b=36, c=18
c += a + b; // a=77, b=36, c=131
c %= 2 * 5; // a=77, b=36, c=1
c++; // a=77, b=36, c=2
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=lApwla6x-LLEnBU1vQ44o|100%]]

# 2)

a)
2 (int) wird zum float konvertiert
2\*z wird zum double konvertiert, da y ein double sein soll

b)
s (short) wird zum int konvertiert, da 3 ein int ist und i ein int sein soll

c)
s (short) wird zum float konvertiert
z/s wird zum double konvertiert, da x ein double sein soll

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=GO5kw8HgokB9lDTsrVTg8|100%]]

# 3)

```java
public class assignOps2 {
	public static void main(String args[]) {
		int a, b;
		a = 20;
		a -= 4; // a = 16

		a = 20;
		b = 4;
		a += b; // a = 24
		b *= a; // b = 96
		a %= b + 6; // a = 24

		a = 35;
		b = 88;
		a++; // a = 36
		b--; // b = 87
	}
}
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=xbkRi1_SISl1l-Y-YRa1d|100%]]

# 4)

'=' ist eine Zuweisung
'==' ist ein Vergleichsoperator

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=Z6Ofvqjch1PZNOzuZja56|100%]]

# 5)

```java
if (ch instanceof float) || (ch instanceof double) { /* Operation A hier */ }
else { /* Operation B hier */ }
```

```java
if (ch == 'y')) { /* Operation A hier */ }
else if (ch == 'Y') { /* Operation B hier */ }
```

```java
if ("aeiou".contains(ch)) { /* Operation A hier */ }
else { /* Operation B hier */ }
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=PCTcGe71SjfMo3QkL187T|100%]]

# 6)

```java
boolean p = true; q = false;
p ^ q // false
(p & !q) | (q & !p) // true
(p | !q) & (!p | q) // false
```

| $\text{(p \& !q) == false}$ | $q = true$ | $q = false$ |
| --------------------------- | ---------- | ----------- |
| $p = true$                  | $true$     | $false$     |
| $p = false$                 | $true$     | $true$      |

| $\text{(p │ (p != q)) == true}$ | $q = true$ | $q = false$ |
| ------------------------------- | ---------- | ----------- |
| $p = true$                      | $true$     | $false$     |
| $p = false$                     | $true$     | $true$      |

```java
(p != q) == (!(p & q)) // Nein, mit p=false und q=false ergibt sich false == true
(p != q) == ((p | q) & !(p & q)) // Ja
```

```java
bexp = false != true; // true
bexp = !false; //true
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=v1N6UyC6QA93AePFEweyM|100%]]

# 7)

```java
x != 5 // ist false und somit wird der zweite Teil der if abfrage gar nicht erst geprüft
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=89Egb8fifK-MDBiF1NaRN|100%]]

# 8)

a)

```java
if (value % 2 == 1) { return true; }
else { return false; }
```

b)

```java
if (x > y) { value = x; }
else { value = y; }
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=4C9gedQper48oLV_-EOBq|100%]]

# 9)

```java
c = a < 2 * b ? a : b;
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=7t7m0nzFThvBgG0PCAm33|100%]]

# 10)

```java
mietpreis = gefahreneKm*.35 + 10 > 45 ? gefahreneKm*.35 + 10 : 45;
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=oHrLKXF4tGhdSlIMsQQ9E|100%]]

# 11)

```java
if (x < y && y != 0) { val = 1; }
else { val = 0; }
```

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=IAyc61i1RG8Pu9ElvibXz|100%]]

# 12)

$32768L$ ist ein Long. Bei der Konvertierung werden nur die unteren 16 Bit übernommen.
-> Somit liegt 32768 außerhalb des Wertebereiches und es erfolgt ein Überlauf, wodurch $n=-32758$ interpretiert wird

<div style='page-break-after: always;'></div>

![[OOPE_Abgabe_01.excalidraw#^area=g8WtfMO_pFPsdAZnpe9PJ|100%]]

# 13)

- In der Nähe von `1.0` gibt es eine kleinste darstellbare Differenz.
- Wenn `d` kleiner als diese Differenz ist, hat `1.0 + d` denselben Binärwert wie `1.0`.
