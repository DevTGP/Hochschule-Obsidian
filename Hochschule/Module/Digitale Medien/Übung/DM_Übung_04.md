![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=iyjRLEwN7eECWxZf8yVtv|100%]]

a)
(1)
$740 \cdot 600 \cdot 3 \cdot 8 \text{ Bit } = 444'000  \cdot 3 \text{ Byte } = 1'332'000 \text{ Byte } = 1.332 \text{ MByte }$

(2)
$740 \cdot 600 \cdot 3 \cdot 4 \text{ Bit } = 444'000  \cdot 12 \text{ Bit } = 5'328'000 \text{ Bit } = 666'000 \text{ Byte } = 666 \text{ KByte }$

(3)
$740 \cdot 600 \cdot 3 \cdot 4 \text{ Bit } = 444'000  \cdot 6 \text{ Bit } = 2'664'000 \text{ Bit } = 333'000 \text{ Byte } = 33 \text{ KByte }$

(4)
$740 \cdot 600 \cdot 3 \cdot 4 \text{ Bit } = 444'000  \cdot 6 \text{ Bit } = 2'664'000 \text{ Bit } = 333'000 \text{ Byte } = 33 \text{ KByte }$

die Pixeldichte hat keine Auswirkungen auf die Rohdatenmenge

b)
$1cm = 2.54inch$
$\frac{\sqrt{ (740px)^{2} + (600px)^{2} }}{\sqrt{ (12.7cm)^{2}+(10.3cm)^{2} }} = \frac{\sqrt{ 907600px^{2} }}{\sqrt{ 267.38cm^{2} }} = \frac{952.68px}{16.35cm} = \frac{952.68px}{6.44inch} = 147.93ppi$

c)
$\frac{740px}{370ppi} = 2inch_{\text{ horizontal }}$
$\frac{600px}{370ppi} = 1.62inch_{\text{ vertikal }}$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=TeMccncyFR5JWxq9R2vC2|100%]]

Es kommt auf das Verfahren an:
Wenn nur abgetastet wird und der abgetastete Wert für die Zwischenräume verwendet wird (oder "Nächster Nachbar" verwendet wird), dann sind die Bilder identisch,
,ansonsten sind die Bilder nicht identisch, da die meisten Verfahren mit Mittelwerten arbeiten

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=ilhSo3ycVve9LFerlr9x1|100%]]

Ein Histogramm eines Bildes ist eine grafische Darstellung der Häufigkeit der Helligkeits- oder Farbwerte in einem Bild.

- Auf der x-Achse: mögliche Helligkeitswerte (z. B. 0–255 bei 8 Bit)
- Auf der y-Achse: Anzahl der Pixel mit dem jeweiligen Helligkeitswert

Es zeigt also, wie das Licht und die Dunkelheit im Bild verteilt sind.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=ISOUHtGTTFcdFffQQ8ioV|100%]]

$100 \cdot100 \cdot3 \cdot8\text{ Bit }=30000 \text{ Byte } =30\text{ KByte }$
Berechnete Datenmenge:
$30 \text{ KByte }$
Tatsächliche Größe:
$30.054 \text{ KByte }$

Verdoppelt:
$200 \cdot100 \cdot3 \cdot8\text{ Bit }=30000 \text{ Byte } =60\text{ KByte }$
Berechnete Datenmenge:
$60 \text{ KByte }$
Tatsächliche Größe:
$60.054 \text{ KByte }$

Es sind $50\text{ Bytes }$ als Header zur Größe zum Bild dazu gespeichert.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=KQjqwRabf9Zw_phCNm4TD|100%]]

a)
biWidth: $12_{16} \to 6$
biHeight: $16_{16} \to 9$

$\to 6px  \cdot 9px$

b)
"DM ROCKT"

Da die Länge der Zeile immer ein Vielfaches von $4 \text{ Bytes }$ müssen Platzhalter eingefügt werden. Dabei ist es egal, was in diesen Bytes beinhaltet ist.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=R2Zy55CIE6oSS6D0AFkHr|100%]]

a)

$30 \cdot 20 \cdot 24\text{ Bit } = 1800 \text{ Byte } = 1.8 \text{ KByte }$

b)

$<w,30><w,30><w,2><b,28><w,30><w,30><b,30><b,30><b,30><b,15><g,15><g,30><g,30><g,30><g,30><g,30><g,30><g,30><g,30><g,30><g,30><g,30>$

$\to 22 \cdot (1+1)\text{ Byte } = 44 \text{ Byte }$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=YPVW387ZXRlZ2jAK_KSMl|100%]]

a)
$4:1:1$

b)
![[DM_Übung_04_Anhang_1.excalidraw|100%]]

c)
JPEG-Farbunterabtastung: $4:2:0$
$\to 1-\left( \frac{1}{3}+\frac{1}{3}+\frac{1}{3} \frac{\cdot1}{4} \right)=1-\left( \frac{9}{12} \right)=\frac{1}{4}$
$\to$ Alleine durch die Farbunterabtastung wird $25\%$ eingespart.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_04.excalidraw.md#^area=Y_ePAA5yfja0sYQQXBEO3|100%]]

a)
Der komplette untere $\frac{3}{4}$ Bereich hat eine hoher Ortsfrequenz, da das Muster sehr fein ist.

b)
Der obere $\frac{1}{3}$ Bereich hat eine niedrige Ortsfrequenz, da dieser Bereich kein feines Muster sondern nur einen Gradienten besitzt.

c)
![[DM_Übung_04_Anhang_2.png|800]]
