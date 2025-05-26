![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_02.excalidraw.md#^area=hbw21DtWNi0DqLNCGO3hX|100%]]

a)

$1920 \cdot 1080 \cdot 24 \text{Bit}$
$=2073600 \cdot 3\text{Byte}$
$=6220800\text{Byte}$
$=6.2208\text{MByte}$
$\approx6.22\text{MByte}$

b)
$640 \cdot 480 \cdot 16 \cdot 8 \frac{\text{Bit}}{\text{s}}$
$=307200 \cdot 16 \cdot 8 \frac{\text{Bit}}{\text{s}}$
$=39321600 \frac{\text{Bit}}{\text{s}}$
$=39.3216 \frac{\text{MBit}}{\text{s}}$
$\approx39.32 \frac{\text{MBit}}{\text{s}}$

c)
$\left( 1280 \cdot 720 \cdot 30 \frac{1}{\text{s}} \cdot 3 \cdot8\text{Bit}  + 2 \cdot 22.05\text{kHz} \cdot 16\text{Bit} \right)\cdot 3 \cdot 60\text{s}$
$=\left( 82944000 \frac{\text{ Byte }}{\text{ s }} + 88200 \frac{Byte}{\text{ s }}\right)\cdot 3 \cdot 60\text{s}$
$=83032200 \frac{\text{ Byte }}{\text{ s }}\cdot 3 \cdot 60\text{s}$
$=14945796000 \text{ Byte }$
$=14.945796 \text{ GByte }$
$\approx14.95 \text{ GByte }$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_02.excalidraw.md#^area=WOEwU4LfHioNJSneZVR-D|100%]]

a)
$\text{ GGGA 0000 AAAB B444 4445 55AA AA12 BBBB CCCE 1111 1111  - (44 Byte)}$
$\to\text{   }<G,3><A,1><4,3><A,3><B,2><4,6><5,3><A,4><1,1><2,1><B,4><C,3><E,1><1,8> \text{ - 28 Byte }$

Bei $\text{ 2 Byte }$ pro gebildeter Block
$\frac{44-28}{44} = .3636 = 36.36\% \text{ Ersparnis }$

b)
$\text{ ADDB BB00 00CC CCCC B141 1124 22GG GGGC - (32 Byte)}$
$\to\text{   }<A,1><D,2><B,3><0,4><C,6><B,1><1,1><4,1><1,3><2,1><4,1><2,2><G,5><C,1> \text{ - 28 Byte }$

Bei $\text{ 2 Byte }$ pro gebildeter Block
$\frac{32-28}{32} = 0.125 = 12.5\% \text{ Ersparnis }$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_02.excalidraw.md#^area=JCot5Su-4XjfnpBxpb7Wz|100%]]

| a   | $p_{a}$ |
| --- | ------- |
| R   | $0.09$  |
| E   | $0.35$  |
| H   | $0.1$   |
| K   | $0.16$  |
| P   | $0.05$  |
| A   | $0.12$  |
| S   | $0.13$  |

a)

$H = \sum_{a \in A}p_{a \cdot x_{a}} = \sum_{a \in A} p_{a} \cdot \log_{2}\left( \frac{1}{p_{a}} \right)$
$= 0.09 \cdot \log_{2}\left( \frac{1}{0.09}\right) + 0.35 \cdot \log_{2}\left( \frac{1}{0.35}\right) + 0.1 \cdot \log_{2}\left( \frac{1}{0.1}\right) + 0.16 \cdot \log_{2}\left( \frac{1}{0.16}\right) + 0.05 \cdot \log_{2}\left( \frac{1}{0.05}\right) + 0.12 \cdot \log_{2}\left( \frac{1}{0.12}\right) + 0.13 \cdot \log_{2}\left( \frac{1}{0.13}\right)$
$=2.56377$

b)
![[DM_Übung_02_Codebaum.excalidraw#^area=EgqG-wKd80ULK3_thl0dT|100%]]

| Zeichen $a$                | E   | K   | S   | A   | H   | R    | P    |
| -------------------------- | --- | --- | --- | --- | --- | ---- | ---- |
| Codierung                  | 01  | 00  | 100 | 011 | 010 | 1010 | 1011 |
| Wahrscheinlichkeit $p_{a}$ | .35 | .16 | .13 | .12 | .1  | .09  | .05  |
| Wortlänge                  | 2   | 2   | 3   | 3   | 3   | 4    | 4    |

$\text{ HARKE } \to 11110 1110 111110 10 0$

$\text{ KEKSE } \to 10 0 10 110 0$

c)
Durchschnittliche Wortlänge $L = .35 \cdot 2 + .16 \cdot 2 +.13 \cdot 3 +.12\cdot3+.1\cdot3+.09\cdot4+.05\cdot4$
$=.7+.32+.39+.36+.3+.36+.2$
$=2.63$

$R = L-H = 2.63-2.56377= 0.06623$

Nein, die Codierung ist nicht optimal, da die Redundanz $R>0$ ist.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_02.excalidraw.md#^area=9yNeqfA9hzYyIVuASG1_9|100%]]

$\text{ bobobobowebewe }$

| $input$ | $\text{ dictionary.add() }$ | $\text{ print() }$ | $buffer$ |
| ------- | --------------------------- | ------------------ | -------- |
|         |                             |                    | $b$      |
| $o$     | $(128, \text{ "bo"})$       | $98$               | $o$      |
| $b$     | $(129, \text{ "ob"})$       | $111$              | $b$      |
| $o$     |                             |                    | $bo$     |
| $b$     | $(130, \text{ "bob"})$      | $128$              | $b$      |
| $o$     |                             |                    | $bo$     |
| $b$     |                             |                    | $bob$    |
| $o$     | $(131, \text{ "bobo"})$     | $130$              | $o$      |
| $w$     | $(132, \text{ "ow"})$       | $111$              | $w$      |
| $e$     | $(133, \text{ "we"})$       | $119$              | $e$      |
| $b$     | $(134, \text{ "eb"})$       | $101$              | $b$      |
| $e$     | $(135, \text{ "be"})$       | $98$               | $e$      |
| $w$     | $(136, \text{ "ew"})$       | $101$              | $w$      |
| $e$     |                             |                    | $we$     |
| $EOF$   |                             | $133$              |          |

$\text{ Kodierte Nachricht: }98,111,128,130,111,119,101,98,101,133$

$\text{ unkomprimiertes ASCII: }1100010 1101111 1100010 1101111 1100010 1101111 1100010 1101111 1110111 1100101 1100010 1100101 1110111 1100101 \text{ - (98Bit) }$
$\text{ LZW-Darstellung: }01100010 01101111 10000000 10000010 01101111 01110111 01100101 01100010 01100101 10000101 \text{ - (80Bit) }$

$\text{ Ersparnis: } \frac{98-80}{98} \approx .18367 \approx 18.37\%$

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_02.excalidraw.md#^area=FUv58YE1Th_qscpRG5NOK|100%]]

a)

| $input$ | $\text{ dictionary.add() }$ | $\text{ print() }$ | $buffer$ |
| ------- | --------------------------- | ------------------ | -------- |
|         |                             |                    | $0$      |
| $0$     | $(4, \text{ "00"})$         | $0$                | $0$      |
| $1$     | $(5, \text{ "01"})$         | $0$                | $1$      |
| $2$     | $(6, \text{ "12"})$         | $1$                | $2$      |
| $2$     | $(7, \text{ "22"})$         | $2$                | $2$      |
| $3$     | $(8, \text{ "23"})$         | $2$                | $3$      |
| $0$     | $(9, \text{ "30"})$         | $3$                | $0$      |
| $3$     | $(10, \text{ "03"})$        | $0$                | $3$      |
| $3$     | $(11, \text{ "33"})$        | $3$                | $3$      |
| $1$     | $(12, \text{ "31"})$        | $3$                | $1$      |
| $1$     | $(13, \text{ "11"})$        | $1$                | $1$      |
| $3$     | $(14, \text{ "13"})$        | $1$                | $3$      |
| $0$     |                             |                    | $30$     |
| $1$     | $(15, \text{ "301"})$       | $9$                | $1$      |
| $2$     |                             |                    | $2$      |
| $1$     | $(16, \text{ "121"})$       | $6$                | $1$      |
| $EOF$   |                             | $1$                |          |

$\text{ LZW-Kodierung: }0 0 1 2 2 3 0 3 3 1 1 9 6 1$

b)

| $a$        | Dezimal | Anzahl | $p_{a}$        | Codierung |
| ---------- | ------- | ------ | -------------- | --------- |
| Rot(ro)    | 0       | 4      | $\frac{4}{16}$ | 00        |
| Blau(bl)   | 1       | 5      | $\frac{5}{16}$ | 01        |
| Braun(br)  | 2       | 3      | $\frac{3}{16}$ | 10        |
| Orange(or) | 3       | 4      | $\frac{4}{16}$ | 11        |

![[Hochschule/Module/Digitale Medien/Übung/DM_Übung_02_Codebaum.excalidraw.md#^area=MX4ermJjZYyIqGHtoGjBr|100%]]

$\text{ Huffman Kodierung: }00 00 01 10 10 11 00 11 11 01 01 11 00 01 10 01 \text{ - 32Bit }$

c)
$\text{ LZW-Kodierung (in Bits): }0000 0000 0001 0010 0010 0011 0000 0011 0011 0001 0001 1001 0110 0001 \text{ - (56Bit) }$

In dem Fall ist die $\text{ Huffman-Kodierung }$ besser als die $\text{ LZW-Kodierung }$.
