![[Hochschule/Module/Lineare Algebra/Übung/LA_Aufgabensammlung_02.excalidraw.md#^area=S-8Ag3bB1LkGaqfKmtOP9|100%]]

```python
from itertools import product

import matplotlib.pyplot as plt
import numpy as np

number_points = 500

v1 = (1, 1)
v2 = (-1, 2)
vectors = (v1, v2)

b1 = 1
b2 = 0
b3 = -.5
bs = (b1, b2, b3)

points = (np.random.rand(number_points, 2) - .5) * 4

fig, axs = plt.subplots(2, 3, layout='constrained', figsize=(6 * len(bs) - 1, 6 * len(vectors) - 1))

for n, (v, b) in enumerate(product(vectors, bs)):
    ax = axs[n // 3][n % 3]

    data = {
        'x': [],
        'y': [],
        'color': []
    }

    for dot in points:
        p = v @ dot
        data['x'].append(dot[0])
        data['y'].append(dot[1])

        if p < b:
            data['color'].append('green')
        elif p > b:
            data['color'].append('red')
        else:
            data['color'].append('blue')

    ax.quiver(0, 0, v[0], v[1], color='blue', scale=1, angles='xy', scale_units='xy')
    o = (v[1], -v[0])
    ax.quiver(0, 0, o[0], o[1], color='red', scale=1, angles='xy', scale_units='xy')

    if b == 0:
        ax.axline((0, 0), o, color='blue', linestyle='--')
    else:
        ax.axline((0, b / v[1]), (b / v[0], 0), color='blue', linestyle='--')

    ax.scatter(data['x'], data['y'], color=data['color'], alpha=.3)
    ax.set_title(f'v = {v}, b = {b}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.axhline(y=0, color='black')
    ax.axvline(x=0, color='black')
    ax.grid(True)

plt.savefig('la.png')
```

![[LA_A34_Anhang_1.png]]
