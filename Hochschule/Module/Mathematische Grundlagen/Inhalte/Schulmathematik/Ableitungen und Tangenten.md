[[Schulmathematik]]

---

# Ableitungen
>Ableitungen beschreiben, wie sich eine Funktion in Bezug auf eine Variable verändert. Mathematisch ist die Ableitung die Grenzwertbetrachtung des Änderungsquotienten einer Funktion. Sie gibt die Steigung der Tangente an einem Punkt der Funktion an.
>
>Zum Ableiten nutzt man Regeln, die auf der Struktur der Funktion basieren:
>
>1. **Konstante Regel**: $\frac{d}{dx} c = 0$
>2. **Potenzregel**: $\frac{d}{dx} x^n = n \cdot x^{n-1}$
>3. **Summe/Differenzregel**: $\frac{d}{dx} (f(x) \pm g(x)) = f'(x) \pm g'(x)$
>4. **Produktregel**: $\frac{d}{dx} (f(x) \cdot g(x)) = f'(x) \cdot g(x) + f(x) \cdot g'(x)$
>5. **Kettenregel**:$\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$
>
>Jede Funktion wird anhand dieser Regeln abgeleitet.

# Beispiele

## $x^2$
>$f(x) = x^{2} + 2x + 1$
>$f'(x) = 2x + 2$
 
## $x^3$
>$f(x) = x^{3} + 5x^2 - 3x + 1$
>$f'(x) = 3x^2 + 10x - 3$

## cos & sin
>$f(x) = \sin(x) + \cos(x)$
>$f'(x) = \cos(x) - \sin(x)$

## eulersche Zahl
>$f(x) = e^{x} - 5$
>$f'(x) = e^{x}$


# Tangente
>Eine Tangente ist eine Gerade, die eine Kurve an genau einem Punkt berührt und dort dieselbe Steigung wie die Kurve hat. Ihre Gleichung lautet:
>
> $y = f'(x_0)(x - x_0) + f(x_0)$
>
>Hier ist $x_0$ der Berührpunkt, $f'(x_0)$ die Steigung der Kurve an dieser Stelle.

## Berechnen
>1. **Funktion ableiten**: Bestimme $f'(x)$, die Ableitung der Funktion.
>2. **Berührpunkt einsetzen**: Setze $x_0$ in $f'(x)$ ein, um die Steigung $m = f'(x_0)$ zu berechnen.
>3. **Punkt berechnen**: Bestimme den Berührpunkt $(x_0, f(x_0))$.
>4. **Gleichung aufstellen**: Verwende die Tangentengleichung: $y = m(x - x_0) + f(x_0)$

# Beispiel

Gegeben sei die Funktion $f(x) = 3x^3-5x+1$. Berechnen Sie die Tangente die $f$ bei $x=1$ berührt. 
1. $f'(x) = 9x^2 -5$
2. $f'(1) = 9*1^2 -5 = 4$. Somit ist die Steigung $m=4$
3. $f(1) = 3*1^3 -5*1+1 =-1$. Somit ergibt sich der Berührpunkt $(1, -1)$
4. $y =4(x-1)+(-1)$ oder vereinfacht: $y =4x-5$
