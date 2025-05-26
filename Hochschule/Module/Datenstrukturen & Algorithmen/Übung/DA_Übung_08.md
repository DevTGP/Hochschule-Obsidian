![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_08.excalidraw.md#^area=_87KKkPkqn0qpoub7j5oH|100%]]

```python
import random

unsorted = [random.randint(1, 1000) for i in range(10)]
unsorted = list(set(unsorted))


def selection_sort(l):
    for i in range(len(l)):
        lowest = max(l) + 1
        index = None
        for n in range(i, len(l)):
            if l[n] < lowest:
                lowest = l[n]
                index = n
        if index:
            l[index], l[i] = l[i], l[index]
    return l


def insertion_sort(l):
    sorted_list = []

    for i, x in enumerate(l):
        if i == 0:
            sorted_list.append(x)
            continue
        index = 0
        for n in range(i):
            if x > sorted_list[n]:
                index = n + 1
            else:
                break
        sorted_list = sorted_list[:index] + [x] + sorted_list[index:]
    return sorted_list


def bubble_sort(l):
    n = len(l) - 1
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print(unsorted)
print(selection_sort(unsorted))
print(insertion_sort(unsorted))
print(bubble_sort(unsorted))
```
