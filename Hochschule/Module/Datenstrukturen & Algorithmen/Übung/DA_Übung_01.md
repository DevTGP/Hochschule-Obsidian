![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_01.excalidraw.md#^area=SWsbcmUQUF7B5v566CUOr|100%]]

# Schleife 1

```python
for n in range(0, 11):
	count = 0
	for i in range(n):
		for j in range(n):
			count += 1
	print(count)
```

| n     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 0   | 1   | 4   | 9   | 16  | 25  | 36  | 49  | 64  | 81  | 100 |

$T(n) = n \cdot n = n^{2}$
$T(n) \in O(n^{2})$

# Schleife 2

```python
for n in range(0, 11):
	count = 0
	for i in range(n, 0, -1):
		for j in range(i, n):
			count += 1
	print(count)
```

| n     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 0   | 0   | 1   | 3   | 6   | 10  | 15  | 21  | 28  | 36  | 45  |

$$
T(n) =
\begin{cases}
0 & \text{, falls } n=0 \\
T(n-1) + n-1 & \text{, sonst}
\end{cases}
$$

$T(n) \in O(n)$

# Schleife 3

```python
for n in range(0, 11):
	count = 0
	for i in range(1, n // 2 + 1):
		for j in range(1, n*n):
			count += 1
	print(count)
```

| n     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 0   | 0   | 3   | 8   | 30  | 48  | 105 | 144 | 252 | 320 | 495 |

$T(n) = \left\lfloor  \frac{n}{2}  \right\rfloor  * (n^{2}-1)$

$T(n) \in O(n^{2})$

# Schleife 4

```python
for n in range(0, 11):
	i = n
	count = 0
	while True:
		count += 1
		i =  i // 3
		if i <= 0:
			break
	print(count)
```

| n     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 1   | 1   | 1   | 2   | 2   | 2   | 2   | 2   | 2   | 3   | 3   |

$count = \log_{2} n$
$T(n) \in O(\log n)$
