![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_07.excalidraw.md#^area=LDavKsHSMGmTh0dLZwMzJ|100%]]

Schlüsselfolge: $9,23,10,19,17,16$
$h(k)= k \text{ mod }m$
$m=7, b=1$

(a)
$h_{i}(k)=(h(k)+i) \text{ mod } m$

| 0    | 1   | 2   | 3    | 4    | 5    | 6    |
| ---- | --- | --- | ---- | ---- | ---- | ---- |
| $16$ |     | $9$ | $23$ | $10$ | $19$ | $17$ |

Kollisionen:
$23,10,17,17,17,16,16,16,16,16$
$\to 10$ Kollisionen

(b)
$h_{i}(k)=(h(k)+i^{2}) \text{ mod } m$

| 0    | 1   | 2   | 3    | 4    | 5    | 6    |
| ---- | --- | --- | ---- | ---- | ---- | ---- |
| $17$ |     | $9$ | $23$ | $10$ | $19$ | $16$ |

Kollisionen:
$23,10,17,17,16,16$
$\to 6$ Kollisionen

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_07.excalidraw.md#^area=sMXaW18ln6zXjnLXDBSXo|100%]]

$h(k)= k \text{ mod }m$
$m=9, b=1$

$h_{i}(k)=(h(k)+i^{2}) \text{ mod } m$

$insert(3): 3$
$insert(21): 3,4$
$delete(3): 3$
$member(21): 3,4$
$insert(28): 1$
$member(10): 1,2$
$delete(3): 3,4,7$ (3, wurde gelöscht, also weiter schauen, 4 ist nicht 3, 7 ist leer also bricht ab)
$insert(12): 3$

| 0   | 1    | 2   | 3                                  | 4    | 5   | 6   | 7   | 8   |
| --- | ---- | --- | ---------------------------------- | ---- | --- | --- | --- | --- |
|     | $28$ |     | $\cancel{ 3 }\to \cancel{ D }\to3$ | $21$ |     |     |     |     |

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_07.excalidraw.md#^area=cKXEc-5qHcWNgVl26zyqG|100%]]

```python
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
        self.deleted = object()

    def insert(self, value):
        visited = []
        for i in range(self.size * 10000):
            index = self._get_next_index(value, i)
            if index not in visited:
                visited.append(index)
            elif len(visited) == self.size:
                break
            if self.buckets[index] is None or self.buckets[index] == self.deleted:
                self.buckets[index] = value
                return index
        raise Exception('Hashtabelle ist voll')

    def find(self, value):
        for i in range(self.size * 10000):
            index = self._get_next_index(value, i)
            if self.buckets[index] == value:
                return index
        return None

    def delete(self, value):
        if self.find(value) is not None:
            self.buckets[self.find(value)] = self.deleted
        else:
            raise Exception('Wert nicht gefunden')

    def _get_next_index(self, h, i):
        offset = i * i
        return (h + (-offset if i % 2 == 0 else offset)) % self.size

    def __str__(self):
        return str(self.buckets)
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_07.excalidraw.md#^area=ULY01J1ObCQ6wKZnSJkOG|100%]]

```python
def char_value(char):
    return ord(char.upper()) - ord('A') + 1


def my_hash(code, a, b, c):
    return (char_value(code[0]) * a + char_value(code[1]) * b + char_value(code[2]) * c) % 10


codes = ['MUC', 'STR', 'PMI', 'LUX', 'HAM', 'FDH', 'VLC', 'CGN', 'AGP', 'FAO']
for a in range(10):
    for b in range(10):
        for c in range(10):
            found_hashes = set()
            for code in codes:
                h = my_hash(code, a, b, c)
                found_hashes.add(h)
            if len(found_hashes) == 10:
                print(a, b, c)

print()
for code in codes:
    print(my_hash(code, 5, 1, 6))
```
