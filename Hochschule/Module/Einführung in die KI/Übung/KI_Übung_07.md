![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_07.excalidraw.md#^area=qFjoPTyGbNBU13NlE4JkV|100%]]

$X = \{x_{0},x_{1},x_{2},x_{3},x_{4},x_{5}\}$
$x_{0}=(1,1),x_{1}=(2,1),x_{2}=(2,3),x_{3}=(2,4),x_{4}=(1.5,2),x_{5}=(2.5,2.5)$

$k=2$

$C=\{c_{0},c_{1}\}$
$c_{0}=x_{2},c_{1}=x_{3}$

---

# Iteration 1

| $x_{i}$ | $\vert\vert x_{i} -c_{0}\vert\vert^{2}$ | $\vert\vert x_{i}-c_{1}\vert\vert^{2}$ | $z_{i}$ |
| ------- | --------------------------------------- | -------------------------------------- | ------- |
| $x_{0}$ | $(-1,-2)\to 5$                          | $(-1,-3)\to 10$                        | 0       |
| $x_{1}$ | $(0,-2)\to 4$                           | $(0,-3)\to 9$                          | 0       |
| $x_{2}$ | $(0,0)\to 0$                            | $(0,-1)\to 1$                          | 0       |
| $x_{3}$ | $(0,1)\to 1$                            | $(0,0)\to 0$                           | 1       |
| $x_{4}$ | $(-0.5,-1)\to 1.25$                     | $(-0.5,-2)\to 4.25$                    | 0       |
| $x_{5}$ | $(0.5,-0.5)\to 0.5$                     | $(0.5,-1.5)\to 2.5$                    | 0       |

![[KI_Übung_07_Anhang_1.excalidraw|100%]]

## Neue Clusterzentren

$c_{0} = \frac{1}{\vert S_{j}\vert} \cdot \sum_{x_{i} \in S_{j}} x_{i} = \frac{1}{5} \cdot ((1,1)+(2,1)+(2,3)+(1.5,2)+(2.5,2.5))=\frac{1}{5} \cdot (9,9.5)=\left( \frac{18}{10}, \frac{19}{10} \right)$
$c_{1} = \frac{1}{\vert S_{j}\vert} \cdot \sum_{x_{i} \in S_{j}} x_{i} = \frac{1}{1} \cdot ((2,4)) = (2,4)$

---

# Iteration 2

| $x_{i}$ | $\vert\vert x_{i} -c_{0}\vert\vert^{2}$              | $\vert\vert x_{i}-c_{1}\vert\vert^{2}$ | $z_{i}$ |
| ------- | ---------------------------------------------------- | -------------------------------------- | ------- |
| $x_{0}$ | $\left( -\frac{8}{10},-\frac{9}{10} \right)\to 1.55$ | $(-1,-3)\to 10$                        | 0       |
| $x_{1}$ | $\left( \frac{2}{10},-\frac{9}{10} \right)\to 0.85$  | $(0,-3)\to 9$                          | 0       |
| $x_{2}$ | $\left( \frac{2}{10},\frac{11}{10} \right)\to 1.25$  | $(0,-1)\to 1$                          | 1       |
| $x_{3}$ | $\left( \frac{2}{10},\frac{21}{10} \right)\to 4.45$  | $(0,0)\to 0$                           | 1       |
| $x_{4}$ | $\left( -\frac{3}{10},\frac{1}{10} \right)\to 0.1$   | $(-0.5,-2)\to 4.25$                    | 0       |
| $x_{5}$ | $\left( \frac{7}{10},\frac{6}{10} \right)\to 0.85$   | $(0.5,-1.5)\to 2.5$                    | 0       |

![[KI_Übung_07_Anhang_2.excalidraw|100%]]

## Neue Clusterzentren

$c_{0} = \frac{1}{4} \cdot ((1,1)+(2,1)+(1.5,2)+(2.5,2.5))=\frac{1}{4} \cdot (7,6.5)=\left( \frac{14}{8}, \frac{13}{8} \right)$
$c_{1} = \frac{1}{2} \cdot ((2,3)+(2,4)) =\frac{1}{2} \cdot (4,7) = \left( \frac{4}{2}, \frac{7}{2} \right)$

---

# Iteration 3

| $x_{i}$ | $\vert\vert x_{i} -c_{0}\vert\vert^{2}$                     | $\vert\vert x_{i}-c_{1}\vert\vert^{2}$                     | $z_{i}$ |
| ------- | ----------------------------------------------------------- | ---------------------------------------------------------- | ------- |
| $x_{0}$ | $\left( -\frac{6}{8},-\frac{5}{8} \right) == \frac{81}{64}$ | $\left( -\frac{2}{2},-\frac{5}{2} \right) == \frac{29}{4}$ | 0       |
| $x_{1}$ | $\left( \frac{2}{8},-\frac{5}{8} \right) == \frac{29}{64}$  | $\left( \frac{0}{2},-\frac{5}{2} \right) == \frac{25}{4}$  | 0       |
| $x_{2}$ | $\left( \frac{2}{8},\frac{11}{8} \right) == \frac{125}{64}$ | $\left( \frac{0}{2},-\frac{1}{2} \right) == \frac{1}{4}$   | 1       |
| $x_{3}$ | $\left( \frac{2}{8},\frac{19}{8} \right) == \frac{365}{64}$ | $\left( \frac{0}{2},\frac{1}{2} \right) == \frac{1}{4}$    | 1       |
| $x_{4}$ | $\left( -\frac{2}{8},\frac{3}{8} \right) == \frac{13}{64}$  | $\left( -\frac{1}{2},-\frac{3}{2} \right) == \frac{10}{4}$ | 0       |
| $x_{5}$ | $\left( \frac{6}{8},\frac{7}{8} \right) == \frac{85}{64}$   | $\left( \frac{1}{2},-\frac{2}{2} \right) == \frac{5}{4}$   | 1       |

![[KI_Übung_07_Anhang_3.excalidraw|100%]]

## Neue Clusterzentren

$c_{0} = \frac{1}{3} \cdot ((1,1)+(2,1)+(1.5,2))=\frac{1}{3} \cdot (4.5,4)=\left( \frac{9}{6}, \frac{8}{6} \right)$
$c_{1} = \frac{1}{3} \cdot ((2,3)+(2,4)+(2.5,2.5)) =\frac{1}{3} \cdot (6.5,9.5) = \left( \frac{13}{6}, \frac{19}{6} \right)$

---

# Iteration 4

| $x_{i}$ | $\vert\vert x_{i} -c_{0}\vert\vert^{2}$                     | $\vert\vert x_{i}-c_{1}\vert\vert^{2}$                        | $z_{i}$ |
| ------- | ----------------------------------------------------------- | ------------------------------------------------------------- | ------- |
| $x_{0}$ | $\left( -\frac{3}{6},-\frac{2}{6} \right) == \frac{13}{36}$ | $\left( -\frac{7}{6},-\frac{13}{6} \right) == \frac{218}{36}$ | 0       |
| $x_{1}$ | $\left( \frac{3}{6},-\frac{2}{6} \right) == \frac{13}{36}$  | $\left( -\frac{1}{6},-\frac{13}{6} \right) == \frac{170}{36}$ | 0       |
| $x_{2}$ | $\left( \frac{3}{6},\frac{10}{6} \right) == \frac{109}{36}$ | $\left( -\frac{1}{6},-\frac{1}{6} \right) == \frac{2}{36}$    | 1       |
| $x_{3}$ | $\left( \frac{3}{6},\frac{16}{6} \right) == \frac{265}{36}$ | $\left( -\frac{1}{6},\frac{5}{6} \right) == \frac{26}{36}$    | 1       |
| $x_{4}$ | $\left( \frac{0}{6},\frac{4}{6} \right) == \frac{16}{36}$   | $\left( -\frac{4}{6},-\frac{7}{6} \right) == \frac{65}{36}$   | 0       |
| $x_{5}$ | $\left( \frac{6}{6},\frac{7}{6} \right) == \frac{85}{36}$   | $\left( \frac{2}{6},-\frac{4}{6} \right) == \frac{20}{36}$    | 1       |

![[KI_Übung_07_Anhang_4.excalidraw|100%]]

## Neue Clusterzentren

$c_{0} = \frac{1}{3} \cdot ((1,1)+(2,1)+(1.5,2))=\frac{1}{3} \cdot (4.5,4)=\left( \frac{9}{6}, \frac{8}{6} \right)$
$c_{1} = \frac{1}{3} \cdot ((2,3)+(2,4)+(2.5,2.5)) =\frac{1}{3} \cdot (6.5,9.5) = \left( \frac{13}{6}, \frac{19}{6} \right)$

Keine Änderungen an den Zentren mehr vorhanden

$SSE = \sum_{i=1}^{n} \vert\vert x_{i}-c_{z_{i}}\vert\vert^{2} = \frac{90}{36} = 2.5$

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_07.excalidraw.md#^area=9fRkTLlV2l5nFIhP_5GTl|100%]]

```python
import random

import numpy as np


def berechneNeueClusterzentren(X, z, C):
    """
        Berechnet neue Clusterzentren basierend auf den aktuellen Zuweisungen.
        Parameter:            X (list of np.array): Liste der Datenpunkte            z (list of int): Clusterzuweisungen pro Datenpunkt            C: (list of np.array): Liste der Clusterzentren
        Rückgabe:            neue_clusterzentren (list of np.array): neue Clusterzentren        """    neue_clusterzentren = []

    for j in range(len(C)):
        c = 1 / len([n for i, n in enumerate(z) if j == n]) * np.sum([X[i] for i, n in enumerate(z) if j == n], axis=0)
        neue_clusterzentren.append(c)

    return neue_clusterzentren


def berechneClusterzuweisungen(X, C, verbose=True):
    """
    Weist jedem Punkt in X das nächstgelegene Clusterzentrum aus C zu.
    Parameter:        X (list of np.array): Datenpunkte        C (list of np.array): Aktuelle Clusterzentren        verbose (bool): Ob Ausgaben zu den Distanzen und Zuweisungen erfolgen sollen
    Rückgabe:        z (list of int): Liste mit der Clusterzuweisung für jeden Punkt in X    """    z = []

    for i, x in enumerate(X):
        z.append(np.argmin([np.linalg.norm(x - c) ** 2 for c in C]))

        if verbose:
            print(f'{X[i]} wird Cluster {z[i]} zugeordnet')

    return z


def lists_equal_allclose(list1, list2, rtol=1e-5, atol=1e-8):
    """
        Vergleicht zwei Listen von NumPy-Arrays elementweise.
        Gibt True zurück, wenn beide Listen die gleiche Länge haben und        alle Arrays an denselben Positionen fast gleich sind (numerisch),        basierend auf relativer (rtol) und absoluter (atol) Toleranz.
        Parameter:            list1 (List[np.ndarray]): Erste Liste von Arrays.            list2 (List[np.ndarray]): Zweite Liste von Arrays.            rtol (float): Relative Toleranz (default 1e-5).            atol (float): Absolute Toleranz (default 1e-8).
        Returns:            bool: True, wenn alle entsprechenden Arrays fast gleich sind.        """    if len(list1) != len(list2):
        return False
    return all(np.allclose(a, b, rtol=rtol, atol=atol) for a, b in zip(list1, list2))


def kmeans(X, k, max_iter=100, verbose=False, seed=0):
    if k > len(X):
        raise ValueError(f"k = {k} ist größer als die Anzahl der Datenpunkte ({len(X)}).")

    # Initialisierung mit zufälligen, eindeutigen Datenpunkten
    random.seed(seed)
    indices = random.sample(range(len(X)), k)
    C = [X[i] for i in indices]
    print("initiale Cluster: ", indices)

    iteration = 0
    # Bei uns soll die Schleife nach einer angegebenen Anzahl an Durchläufen abbrechen
    # oder wenn sich die Clusterzentren nicht mehr verändern (für den Test kann die Funktion lists_equal_allclose verwendet werden)    z = []
    prev_C = []
    while iteration < max_iter:
        z = berechneClusterzuweisungen(X, C)
        prev_C, C = C, berechneNeueClusterzentren(X, z, C)
        if lists_equal_allclose(C, prev_C):
            break
        iteration += 1
        print()

    if iteration >= max_iter:
        print("Maximale Iterationen erreicht.")

    return C, z, iteration


def main():
    x0 = np.array([1, 1])
    x1 = np.array([2, 1])
    x2 = np.array([2, 3])
    x3 = np.array([2, 4])
    x4 = np.array([1.5, 2])
    x5 = np.array([2.5, 2.5])

    X = [x0, x1, x2, x3, x4, x5]

    k = 2
    seed = 42

    try:
        C, z, it = kmeans(X, k, max_iter=100, verbose=True, seed=seed)
        print(f"\nK-Means konvergiert nach {it} Iterationen.")
        for idx in range(len(C)):
            print(f"Clusterzentrum {idx}: {C[idx]}")

        print(
            f'SSE: {round(sum([np.linalg.norm(x - c) ** 2 for i, x in enumerate(X) for j, c in enumerate(C) if z[i] == j]), 2)}')

    except ValueError as e:
        print("Fehler:", e)


if __name__ == "__main__":
    main()
```

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_07.excalidraw.md#^area=DdASYS1lmRFDwoDeDCb5S|100%]]

```python
import random

import numpy as np


def berechneNeueClusterzentren(X, z, C):
    """
        Berechnet neue Clusterzentren basierend auf den aktuellen Zuweisungen.
        Parameter:            X (list of np.array): Liste der Datenpunkte            z (list of int): Clusterzuweisungen pro Datenpunkt            C: (list of np.array): Liste der Clusterzentren
        Rückgabe:            neue_clusterzentren (list of np.array): neue Clusterzentren        """    neue_clusterzentren = []

    for j in range(len(C)):
        c = 1 / len([n for i, n in enumerate(z) if j == n]) * np.sum([X[i] for i, n in enumerate(z) if j == n], axis=0)
        neue_clusterzentren.append(c)

    return neue_clusterzentren


def berechneClusterzuweisungen(X, C, verbose=True):
    """
    Weist jedem Punkt in X das nächstgelegene Clusterzentrum aus C zu.
    Parameter:        X (list of np.array): Datenpunkte        C (list of np.array): Aktuelle Clusterzentren        verbose (bool): Ob Ausgaben zu den Distanzen und Zuweisungen erfolgen sollen
    Rückgabe:        z (list of int): Liste mit der Clusterzuweisung für jeden Punkt in X    """    z = []

    for i, x in enumerate(X):
        z.append(np.argmin([np.linalg.norm(x - c) ** 2 for c in C]))

        if verbose:
            print(f'{X[i]} wird Cluster {z[i]} zugeordnet')

    return z


def lists_equal_allclose(list1, list2, rtol=1e-5, atol=1e-8):
    """
        Vergleicht zwei Listen von NumPy-Arrays elementweise.
        Gibt True zurück, wenn beide Listen die gleiche Länge haben und        alle Arrays an denselben Positionen fast gleich sind (numerisch),        basierend auf relativer (rtol) und absoluter (atol) Toleranz.
        Parameter:            list1 (List[np.ndarray]): Erste Liste von Arrays.            list2 (List[np.ndarray]): Zweite Liste von Arrays.            rtol (float): Relative Toleranz (default 1e-5).            atol (float): Absolute Toleranz (default 1e-8).
        Returns:            bool: True, wenn alle entsprechenden Arrays fast gleich sind.        """    if len(list1) != len(list2):
        return False
    return all(np.allclose(a, b, rtol=rtol, atol=atol) for a, b in zip(list1, list2))


def kmeans(X, k, max_iter=100, verbose=False, seed=0, C=None):
    if k > len(X):
        raise ValueError(f"k = {k} ist größer als die Anzahl der Datenpunkte ({len(X)}).")

    indices = random.sample(range(len(X)), k)
    if C is None:
        C = [X[i] for i in indices]

    # Initialisierung mit zufälligen, eindeutigen Datenpunkten
    random.seed(seed)
    print("initiale Cluster: ", indices)

    iteration = 0
    # Bei uns soll die Schleife nach einer angegebenen Anzahl an Durchläufen abbrechen
    # oder wenn sich die Clusterzentren nicht mehr verändern (für den Test kann die Funktion lists_equal_allclose verwendet werden)    z = []
    prev_C = []
    while iteration < max_iter:
        z = berechneClusterzuweisungen(X, C)
        prev_C, C = C, berechneNeueClusterzentren(X, z, C)
        if lists_equal_allclose(C, prev_C):
            break
        iteration += 1
        print()

    if iteration >= max_iter:
        print("Maximale Iterationen erreicht.")

    return C, z, iteration


def main():
    x0 = np.array([1, 1])
    x1 = np.array([2, 1])
    x2 = np.array([2, 3])
    x3 = np.array([2, 4])
    x4 = np.array([1.5, 2])
    x5 = np.array([2.5, 2.5])
    x6 = np.array([4.5, 4.5])

    X = [x0, x1, x2, x3, x4, x5, x6]

    k = 2
    seed = 42

    try:
        C = [x1, x6]
        # C = [x2, x5]

        C, z, it = kmeans(X, k, max_iter=100, verbose=True, seed=seed, C=C)
        print(f"\nK-Means konvergiert nach {it} Iterationen.")
        for idx in range(len(C)):
            print(f"Clusterzentrum {idx}: {C[idx]}")

        print(
            f'SSE: {round(sum([np.linalg.norm(x - c) ** 2 for i, x in enumerate(X) for j, c in enumerate(C) if z[i] == j]), 2)}')

    except ValueError as e:
        print("Fehler:", e)


if __name__ == "__main__":
    main()
```

```python
import csv
import random
from itertools import product

import numpy as np


def berechneNeueClusterzentren(X, z, C):
    """
        Berechnet neue Clusterzentren basierend auf den aktuellen Zuweisungen.
        Parameter:            X (list of np.array): Liste der Datenpunkte            z (list of int): Clusterzuweisungen pro Datenpunkt            C: (list of np.array): Liste der Clusterzentren
        Rückgabe:            neue_clusterzentren (list of np.array): neue Clusterzentren        """    neue_clusterzentren = []

    for j in range(len(C)):
        if len([n for i, n in enumerate(z) if j == n]) == 0:
            c = C[j]
        else:
            c = 1 / len([n for i, n in enumerate(z) if j == n]) * np.sum([X[i] for i, n in enumerate(z) if j == n],
                                                                         axis=0)
        neue_clusterzentren.append(c)

    return neue_clusterzentren


def berechneClusterzuweisungen(X, C, verbose=False):
    """
    Weist jedem Punkt in X das nächstgelegene Clusterzentrum aus C zu.
    Parameter:        X (list of np.array): Datenpunkte        C (list of np.array): Aktuelle Clusterzentren        verbose (bool): Ob Ausgaben zu den Distanzen und Zuweisungen erfolgen sollen
    Rückgabe:        z (list of int): Liste mit der Clusterzuweisung für jeden Punkt in X    """    z = []

    for i, x in enumerate(X):
        z.append(np.argmin([np.linalg.norm(x - c) ** 2 for c in C]))

        if verbose:
            print(f'{X[i]} wird Cluster {z[i]} zugeordnet')

    return z


def lists_equal_allclose(list1, list2, rtol=1e-5, atol=1e-8):
    """
        Vergleicht zwei Listen von NumPy-Arrays elementweise.
        Gibt True zurück, wenn beide Listen die gleiche Länge haben und        alle Arrays an denselben Positionen fast gleich sind (numerisch),        basierend auf relativer (rtol) und absoluter (atol) Toleranz.
        Parameter:            list1 (List[np.ndarray]): Erste Liste von Arrays.            list2 (List[np.ndarray]): Zweite Liste von Arrays.            rtol (float): Relative Toleranz (default 1e-5).            atol (float): Absolute Toleranz (default 1e-8).
        Returns:            bool: True, wenn alle entsprechenden Arrays fast gleich sind.        """    if len(list1) != len(list2):
        return False
    return all(np.allclose(a, b, rtol=rtol, atol=atol) for a, b in zip(list1, list2))


def kmeans(X, k, max_iter=100, verbose=False, seed=0, C=None):
    if k > len(X):
        raise ValueError(f"k = {k} ist größer als die Anzahl der Datenpunkte ({len(X)}).")

    indices = random.sample(range(len(X)), k)
    if C is None:
        C = [X[i] for i in indices]
    Start = C

    # Initialisierung mit zufälligen, eindeutigen Datenpunkten
    random.seed(seed)
    # print("initiale Cluster: ", indices)

    iteration = 0
    # Bei uns soll die Schleife nach einer angegebenen Anzahl an Durchläufen abbrechen
    # oder wenn sich die Clusterzentren nicht mehr verändern (für den Test kann die Funktion lists_equal_allclose verwendet werden)    z = []
    prev_C = []
    while iteration < max_iter:
        z = berechneClusterzuweisungen(X, C)
        prev_C, C = C, berechneNeueClusterzentren(X, z, C)
        if lists_equal_allclose(C, prev_C):
            break
        iteration += 1
        # print()

    if iteration >= max_iter:
        print("Maximale Iterationen erreicht.")

    sse = round(sum([np.linalg.norm(x - c) ** 2 for i, x in enumerate(X) for j, c in enumerate(C) if z[i] == j]), 2)

    return {
        'Start': Start,
        'Center': C,
        'Zuordnung': z,
        'Iterationen': iteration,
        'SSE': sse
    }


def main():
    x0 = np.array([1, 1])
    x1 = np.array([2, 1])
    x2 = np.array([2, 3])
    x3 = np.array([2, 4])
    x4 = np.array([1.5, 2])
    x5 = np.array([2.5, 2.5])
    x6 = np.array([4.5, 4.5])

    X = (x0, x1, x2, x3, x4, x5, x6)

    k = 2
    seed = 42

    try:
        data = [kmeans(list(X), k, max_iter=100, verbose=False, seed=seed, C=C) for C in product(X, repeat=2)]
        with open('data.csv', mode='w') as file:
            fieldnames = ['Start 1', 'Start 2', 'Center 1', 'Center 2', 'Zuordnung', 'Iterationen', 'SSE']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            for d in data:
                writer.writerow({
                    'Start 1': d['Start'][0],
                    'Start 2': d['Start'][1],
                    'Center 1': d['Center'][0],
                    'Center 2': d['Center'][1],
                    'Zuordnung': d['Zuordnung'],
                    'Iterationen': d['Iterationen'],
                    'SSE': str(d['SSE']).replace('.', ','),
                })


    except ValueError as e:
        print("Fehler:", e)


if __name__ == "__main__":
    main()
```

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_07.excalidraw.md#^area=yDIESXoe4tvReFdsWcl_Q|100%]]

```python
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def berechneNeueClusterzentren(X, z, C):
    """
        Berechnet neue Clusterzentren basierend auf den aktuellen Zuweisungen.
        Parameter:            X (list of np.array): Liste der Datenpunkte            z (list of int): Clusterzuweisungen pro Datenpunkt            C: (list of np.array): Liste der Clusterzentren
        Rückgabe:            neue_clusterzentren (list of np.array): neue Clusterzentren        """    neue_clusterzentren = []

    for j in range(len(C)):
        if len([n for i, n in enumerate(z) if j == n]) == 0:
            c = C[j]
        else:
            c = 1 / len([n for i, n in enumerate(z) if j == n]) * np.sum([X[i] for i, n in enumerate(z) if j == n],
                                                                         axis=0)
        neue_clusterzentren.append(c)

    return neue_clusterzentren


def berechneClusterzuweisungen(X, C, verbose=False):
    """
    Weist jedem Punkt in X das nächstgelegene Clusterzentrum aus C zu.
    Parameter:        X (list of np.array): Datenpunkte        C (list of np.array): Aktuelle Clusterzentren        verbose (bool): Ob Ausgaben zu den Distanzen und Zuweisungen erfolgen sollen
    Rückgabe:        z (list of int): Liste mit der Clusterzuweisung für jeden Punkt in X    """    z = []

    for i, x in enumerate(X):
        z.append(np.argmin([np.linalg.norm(x - c) ** 2 for c in C]))

        if verbose:
            print(f'{X[i]} wird Cluster {z[i]} zugeordnet')

    return z


def lists_equal_allclose(list1, list2, rtol=1e-5, atol=1e-8):
    """
        Vergleicht zwei Listen von NumPy-Arrays elementweise.
        Gibt True zurück, wenn beide Listen die gleiche Länge haben und        alle Arrays an denselben Positionen fast gleich sind (numerisch),        basierend auf relativer (rtol) und absoluter (atol) Toleranz.
        Parameter:            list1 (List[np.ndarray]): Erste Liste von Arrays.            list2 (List[np.ndarray]): Zweite Liste von Arrays.            rtol (float): Relative Toleranz (default 1e-5).            atol (float): Absolute Toleranz (default 1e-8).
        Returns:            bool: True, wenn alle entsprechenden Arrays fast gleich sind.        """    if len(list1) != len(list2):
        return False
    return all(np.allclose(a, b, rtol=rtol, atol=atol) for a, b in zip(list1, list2))


def kmeans(X, k, max_iter=100, verbose=False, seed=0, C=None):
    if k > len(X):
        raise ValueError(f"k = {k} ist größer als die Anzahl der Datenpunkte ({len(X)}).")

    indices = random.sample(range(len(X)), k)
    if C is None:
        C = [X[i] for i in indices]
    Start = C

    # Initialisierung mit zufälligen, eindeutigen Datenpunkten
    random.seed(seed)
    # print("initiale Cluster: ", indices)

    iteration = 0
    # Bei uns soll die Schleife nach einer angegebenen Anzahl an Durchläufen abbrechen
    # oder wenn sich die Clusterzentren nicht mehr verändern (für den Test kann die Funktion lists_equal_allclose verwendet werden)    z = []
    prev_C = []
    while iteration < max_iter:
        z = berechneClusterzuweisungen(X, C)
        prev_C, C = C, berechneNeueClusterzentren(X, z, C)
        if lists_equal_allclose(C, prev_C):
            break
        iteration += 1
        # print()

    if iteration >= max_iter:
        print("Maximale Iterationen erreicht.")

    sse = round(sum([np.linalg.norm(x - c) ** 2 for i, x in enumerate(X) for j, c in enumerate(C) if z[i] == j]), 2)

    return {
        'Start': Start,
        'Center': C,
        'Zuordnung': z,
        'Iterationen': iteration,
        'SSE': sse
    }


def plot_clusters(X, z):
    X = np.array(X)
    z = np.array(z)
    plt.figure(figsize=(6, 6))
    for cluster_id in np.unique(z):
        cluster_points = X[z == cluster_id]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=40, label=f"Cluster {cluster_id}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Clustervisualisierung")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    seed = 42

    try:
        df = pd.read_csv("kmeans_blobs.csv")
        X = [np.array([row.x, row.y]) for row in df.itertuples(index=False)]
        for k in range(2, 8):
            data = kmeans(list(X), k, max_iter=100, verbose=False, seed=seed)
            print(data['SSE'])
            plot_clusters(X, data['Zuordnung'])

    except ValueError as e:
        print("Fehler:", e)


if __name__ == "__main__":
    main()
```
