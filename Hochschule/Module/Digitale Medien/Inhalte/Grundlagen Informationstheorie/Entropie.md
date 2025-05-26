[[Grundlagen Informationstheorie]]

---

> [!check] Definition  
> Entropie ist der durchschnittliche Informationsgehalt (Entscheidungsgehalt) eines Zeichens einer Nachrichtenquelle – ein Maß für Unordnung oder Unsicherheit.

> [!info] Funktionsweise  
> Sie berechnet sich basierend auf den Wahrscheinlichkeiten $p_{a}$ der Zeichen einer Quelle:
>
> 1.  Entscheidungsgehalt $x_{a}$:
>     $x_{a}=\log_{2} \left( \frac{1}{p_{a}} \right)$
>
> 2.  Entropie $H$:
>     $H = \sum_{a \in A} p_{a} \cdot x_{a} =\sum_{a \in A} p_{a} \cdot \log_{2} \left( \frac{1}{p_{a}} \right)$
>
> Je gleichmäßiger die Wahrscheinlichkeiten, desto höher die Entropie. Maximale Entropie bedeutet maximale Unvorhersehbarkeit.

> [!example] Eigenschaften
>
> -   Einheit: $Bit$
> -   Wertebereich: $0 \leq H \leq \log_2(n)$ bei $n$ Zeichen
> -   $H = 0$ bei absoluter Vorhersagbarkeit (ein Zeichen mit $p=1$)
> -   $H$ ist maximal, wenn alle Zeichen gleich wahrscheinlich sind

> [!warning] Hinweis  
> Entropie ist Grundlage für effiziente Codierung: je höher die Entropie, desto weniger lässt sich komprimieren.
