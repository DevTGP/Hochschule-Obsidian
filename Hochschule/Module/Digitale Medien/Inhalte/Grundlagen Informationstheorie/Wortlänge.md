[[Grundlagen Informationstheorie]]

---

> [!check] Definition  
> Die Wortlänge ist die Anzahl der Zeichen eines Wortes in einer formalen Sprache. In Codierungen: die Länge des zugewiesenen Codes für ein Zeichen.

> [!info] Funktionsweise  
> Ein Wort $w \in A^{*}$ besteht aus Zeichen eines Alphabets $A$, und seine Länge ist $\vert w\vert$. Wird bei einer Codierung $c$ einem Zeichen $a \in A$ ein Wort $c(a) \in B^{*}$ zugewiesen, so ist $\vert c(a)\vert$ dessen Wortlänge.
>
> -   Durchschnittliche Wortlänge $L$:
>     $L = \sum_{a \in A} p(a) \cdot \vert c(a)\vert$

> [!example] Wichtige Begriffe
>
> -   $A^{*}$: Menge aller endlichen Wörter über dem Alphabet $A$
> -   $\vert w\vert$: Anzahl der Zeichen im Wort
> -   $\vert c(a)\vert$: Länge des Codes für Zeichen $a$
> -   $L = \sum_{a \in A} p(a) \cdot \vert c(a)\vert$: Durchschnittliche Wortlänge bei Kodierung
