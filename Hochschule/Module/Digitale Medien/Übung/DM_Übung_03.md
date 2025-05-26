![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_03.excalidraw.md#^area=DKexExjrRUn_mgN5VsIOp|100%]]

a)
$\frac{8'888'888}{16}=555555 \text{ R }=8$
$\frac{555555}{16}=34722 \text{ R }=3$
$\frac{34722}{16}=2170 \text{ R }=2$
$\frac{2170}{16}=135 \text{ R }=10=A$
$\frac{135}{16}=8 \text{ R }=7$
$\frac{8}{16}=0 \text{ R }=8$

$\to 8888888_{10} = 0x87A238_{16}$

b)
$0xBC614E_{16}$
$=14 \cdot 16^{0} + 4 \cdot 16^{1} + 1 \cdot 16^{2} + 6 \cdot 16^{3} + 12 \cdot 16^{4} + 11 \cdot 16^{5}$
$=14 + 64 + 256 +24576 + 786432 + 11534336$
$=12'345'678_{10}$

c)
$\#A1882B$
$A1_{16}=161_{10}$
$88_{16}=136_{10}$
$2B_{16}=43_{10}$

$\to RGB(161, 136, 43)$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_03.excalidraw.md#^area=T6XrGaFiMT_645XaFnxx4|100%]]

$\#00E600$
$00_{16}=0_{10}$
$E6{16}=230_{10}$
$00_{16}=0_{10}$

$\to RGB(0, 230, 0)$
$f_{CMY} = weiß_{RGB}-f_{RGB} = (255, 255, 255) - (0, 230, 0) = (255, 25, 255)$
$\to CMY(255, 25, 255)$

Die Farbe grün wird im Print Bereich mit den Farben Cyan und gelb (und minimal magenta) gedruckt, da diese beide rotes, und blaues Licht absorbieren.
Durch das rot und blau absorbierte Licht erscheint das weiße Blatt Papier grün.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_03.excalidraw.md#^area=V912Ty6hf46V_CYly3pYf|100%]]

Speicherplatz:

- ohne Farbtabelle:
    $5 \cdot 5 \cdot 24 \text{ Bit }$
    $=75\text{ Byte }$
- mit Farbtabelle (mit Tabellengröße von bis zu $2^{4}=16$ Einträgen):
    $5 \cdot 5 \cdot 4 \text{ Bit } + 12 \cdot 24 \text{ Bit }$
    $=12.5\text{ Byte } + 36 \text{ Byte }$
    $=48.5 \text{ Byte }$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_03.excalidraw.md#^area=6r5O_O58eo4lgUE3_h-55|100%]]

$x \cdot 1 \text{ Byte } + 256 \cdot 3 \text{ Byte } = x \cdot 3 \text{ Byte }$ | $\div 3\text{ Byte }$
$\Leftrightarrow \frac{x}{3}  + 256 = x$ | $- \frac{x}{3}$
$\Leftrightarrow 256 = \frac{2x}{3}$ | $\cdot \frac{3}{2}$
$\Leftrightarrow 384 = x$

$x \cdot 1 \text{ Byte } + 256 \cdot 3 \text{ Byte } = x \cdot 3 \text{ Byte }$ | $x=384$
$384 \text{ Byte } + 768 \text{ Byte } = 1152 \text{ Byte }$

Die Rastergrafik muss mindestens 384 Pixel enthalten.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_03.excalidraw.md#^area=Xn2P74JFKbts_qWqb5_Ay|100%]]

a)
Die Nationalflagge hat nur 3 Farben, daher stellen indizierte Farben, diese vollständig und verlustfrei dar.

b)
Da die Marsoberfläche nur aus Rot-Tönen besteht, reichen indizierte Farben aus, um das Foto befriedigend darzustellen.

c)
Nein, da durch Kleidung Hintergrund, Farbverläufe vom Wasser oder Himmel und Sonstige Gegenstände am Strand können viele unterschiedliche Farben im Motiv liegen, wodurch die Auflösung (Farbtiefe) nicht mehr ausreicht, um alles ausreichend darzustellen.

Ja, Dithering könnte helfen um den Gradienten des Himmels und Wasser besser darzustellen, trotzdem werden einige Farben verloren gehen.

d)
Der Schwarz-Weiß-Film besteht nur aus einem $8\text{ Bit Farbkanal}$, daher würde man mit indizierten Farben (mit einer Größe von $8\text{ Bit }$ für die Farbtabelle), nur zusätzlich Daten erzeugen.
