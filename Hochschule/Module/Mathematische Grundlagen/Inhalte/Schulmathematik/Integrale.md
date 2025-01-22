[[Schulmathematik]]

---

# Beispiel
Berechnen Sie den Flächeninhalt, der zwischen dem Graph der Funktion $g(x) = x^2-4$ und der X-Achse im Intervall $[-2, 2]$ eingeschlossen wird.
Bilden Sie dazu das bestimmte Integral der Funktion.

1. Bestimmung der Nullstellen
$$
\begin{align*}
&x^2-4=0 & |+4\\
&x^2=4 & |\sqrt{  }\\
&x=\pm2 & |\implies x_{1}=2, x_{2}=-2\\
\end{align*}
$$
2. Zerlegung des Integrals:
$\int_{-2}^0(|g(x)|*dx)+\int_{0}^2(|g(x)|*dx)$

3. Stammfunktion bilden
$\implies \frac{x^3}{3}-4x$

4. Berechnen der Integrale
$$
\begin{align*}
&\int_{-2}^0(|g(x)|*dx)\\
=&\left[ \frac{x^3}{3}-4x \right]^0_{-2}\\
=&\left[ \left( \frac{0^3}{3}-4*0 \right) - \left( \frac{(-2)^3}{3}-4*(-2) \right) \right]\\
=&\left[ \left( \frac{0}{3}-0 \right) - \left( \frac{-8}{3}+8 \right) \right]\\
=&\left[ 0 - \left( \frac{-16}{3} \right) \right]\\
=&\left[\frac{16}{3}\right]\\
\end{align*}
$$
$$
\begin{align*}
&\int_{-2}^0(|g(x)|*dx)\\
=&\left[ \frac{x^3}{3}-4x \right]^2_{0}\\
=&\left[\left( \frac{2^3}{3}-4*2 \right) - \left( \frac{0^3}{3}-4*0 \right)\right]\\
=&\left[ \left( \frac{8}{3}-8 \right) -\left( \frac{0}{3}-0 \right)\right]\\
=&\left[\left( \frac{-16}{3} - 0  \right) \right]\\
=&\left[-\frac{16}{3}\right]\\
\end{align*}
$$
Da wir die Beträge entnehmen haben wir

$\frac{16}{3}+\frac{16}{3}=\frac{32}{3}$

Die eingeschlossene Fläche beträgt $\frac{32}{3}$Einheiten
