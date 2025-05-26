![[DA_Übung_02.excalidraw#^area=Pdwjhl2yvrOxnHnN82olQ|100%]]

Reihenfolge:

1. $2^{100000} \in O(1)$ // Konstant
2. $3^3*\log_{2}n \in O(\log n)$ // Logarithmisch
3. $1020 n+1 \in O(n)$ // Linear
4. $\frac{n^{20}}{n^{18}}+1 = n^2+1 \in n^2$ // Quadratisch
5. $10^n +1 \in O(10^n)$ // Exponentiell

![[DA_Übung_02.excalidraw#^area=L6dDo_c7F58LzSKnfUalv|100%]]

| n                          | 11             | 12             | 13             |
| -------------------------- | -------------- | -------------- | -------------- |
| $A_{2} = 100n \log_{2}(n)$ | $\approx 3805$ | $\approx 4301$ | $\approx 4810$ |
| $A_{3} = 2^n$              | 2048           | 4086           | 8192           |

$A_{1} = 1000n$

$A_{1} <= A_{2} \Leftrightarrow 1000n <= 100n \log_{2}(n) | :100n$
$\Leftrightarrow 10 <=\log_{2}(n) \2^{()}$
$\Leftrightarrow 2^{10} <= n$
$\Leftrightarrow 1024 <= n$

$n<13: A_{3}$
$13<=n<=1024: A_{2}$
$n>1024: A_{1}$

![[DA_Übung_02.excalidraw#^area=if84J56Pr0O7MF9keAzOa|100%]]

| n       | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| zaehler | 1   | 2   | 4   | 6   | 9   | 12  | 16  | 20  |

n ungerade: $T(n) = \left( \left\lceil  \frac{n}{2}  \right\rceil \right)^{2} = \left( \frac{n+1}{2} \right)^2$
n gerade: $T(n) =T(n-1)+\frac{n}{2} = \left( \frac{n}{2} \right)^{2}+\frac{n}{2} = \frac{n^2+2n}{4}$

# Weiteres Beispiel

| n / i                         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Iterationen (innere Schleife) | 1   | 1   | 2   | 2   | 3   | 3   | 4   | 4   |
| zaehler                       | 1   | 2   | 4   | 6   | 9   | 12  | 16  | 20  |

$\left\lceil  \frac{i}{2}  \right\rceil$ Iterationen innere Schleife

n gerade: $T(n) = 2* \sum^{\frac{n}{2}}_{i=0}i = 2*\frac{\frac{n}{2}*\left( \frac{n}{2}+1 \right)}{2}=\frac{n^2+2n}{4}$
n ungerade: $T(n) = T(n+1)-\lceil \frac{n}{2} \rceil$
