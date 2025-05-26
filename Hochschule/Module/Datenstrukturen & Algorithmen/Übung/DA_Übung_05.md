![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_05.excalidraw.md#^area=SMBYgpkj5v4Lp6kWzS7Nw|100%]]

```python
class DoppeltListenelement:
    def __init__(self, inhalt=None, vorher=None, nachher=None):
        self.inhalt = inhalt
        self.vorher = vorher  # Zeiger auf vorheriges Element
        self.nachher = nachher  # Zeiger auf nächstes Element

    def __repr__(self):
        return f"Listenelement({self.inhalt})"


class DoppeltVerketteteListe:
    def __init__(self):
        self.kopf = DoppeltListenelement("HEAD")  # Nulltes Element
        self.ende = self.kopf  # Anfangs gleich Kopf

    def isempty(self):
        return self.kopf.nachher is None

    def append(self, wert):
        """Fügt ein Element am Ende der Liste hinzu."""
        neues_element = DoppeltListenelement(wert, vorher=self.ende)
        self.ende.nachher = neues_element
        self.ende = neues_element

    def first(self):
        """Gibt das erste tatsächliche Listenelement zurück."""
        if self.isempty():
            raise IndexError("Liste ist leer")
        return self.kopf.nachher.inhalt

    def last(self):
        """Gibt das letzte tatsächliche Listenelement zurück."""
        if self.isempty():
            raise IndexError("Liste ist leer")
        return self.ende.inhalt

    def rest(self):
        """Gibt eine neue Liste zurück, die alle Elemente außer dem ersten enthält."""
        if self.isempty():
            return DoppeltVerketteteListe()
        rest_liste = DoppeltVerketteteListe()
        current = self.kopf.nachher.nachher
        while current:
            rest_liste.append(current.inhalt)
            current = current.nachher
        return rest_liste

    def concat(self, andere_liste):
        """Hängt eine andere Liste hinten an."""
        if not andere_liste.isempty():
            andere_liste.kopf.nachher.vorher = self.ende
            self.ende.nachher = andere_liste.kopf.nachher
            self.ende = andere_liste.ende

    def contains(self, wert):
        """Prüft, ob ein Element enthalten ist."""
        return self.find(wert) is not None

    def find(self, wert):
        """Gibt das erste Listenelement mit dem Wert zurück (oder None)."""
        current = self.kopf.nachher
        while current:
            if current.inhalt == wert:
                return current
            current = current.nachher
        return None

    def previous(self, wert):
        """Gibt das vorherige Listenelement zu einem gegebenen Wert"""
        gefunden = self.find(wert)
        if gefunden is None or gefunden.vorher == self.kopf:
            return None
        return gefunden.vorher

    def delete(self, wert):
        """Löscht das erste Vorkommen eines Elements mit dem gegebenen Wert."""
        zu_loeschen = self.find(wert)
        if zu_loeschen:
            zu_loeschen.vorher.nachher = zu_loeschen.nachher
            if zu_loeschen == self.ende:
                self.ende = zu_loeschen.vorher
            if zu_loeschen.nachher:
                zu_loeschen.nachher.vorher = zu_loeschen.vorher
        return None

    def __len__(self):
        count = 0
        current = self.kopf.nachher
        while current:
            count += 1
            current = current.nachher
        return count

    def __repr__(self):
        werte = []
        current = self.kopf.nachher
        while current:
            werte.append(repr(current.inhalt))
            current = current.nachher
        return "Liste([" + ", ".join(werte) + "])"
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_05.excalidraw.md#^area=EvLTAbWczy9NfgQsdbYu5|100%]]

```python
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def postOrder(self, l):
        if self.getLeftChild():
            self.getLeftChild().postOrder(l)
        if self.getRightChild():
            self.getRightChild().postOrder(l)
        l.append(self.getRootVal())
        return l

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getLeftChild().insertLeft('g')
r.getLeftChild().insertRight('d')
r.getRightChild().insertRight('e')
r.getRightChild().getRightChild().insertLeft('f')
print(r.postOrder([]))
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_05.excalidraw.md#^area=FGeaQA3anhqGAnziK542t|100%]]

```python
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def postOrder(self, l):
        if self.getLeftChild():
            self.getLeftChild().postOrder(l)
        if self.getRightChild():
            self.getRightChild().postOrder(l)
        l.append(self.getRootVal())
        return l

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('+')
r.insertLeft('*')
r.insertRight('/')
r.getLeftChild().insertLeft('5')
r.getLeftChild().insertRight('3')
r.getRightChild().insertLeft('24')
r.getRightChild().insertRight('8')
print(r.postOrder([]))
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_05.excalidraw.md#^area=IHv4h1vpNIXvB413f0F-K|100%]]

```python
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def postOrder(self, l):
        if self.getLeftChild():
            self.getLeftChild().postOrder(l)
        if self.getRightChild():
            self.getRightChild().postOrder(l)
        l.append(self.getRootVal())
        return l

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


class Stack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def evaluate_upn(self, token):
        if token.isdigit():
            s.push(int(token))
        else:
            b = self.pop()
            a = self.pop()
            if token == '+':
                s.push(a + b)
            elif token == '-':
                s.push(a - b)
            elif token == '*':
                s.push(a * b)
            elif token == '/':
                s.push(int(a / b))
        return s.peek()

    def __str__(self):
        return self._data.__str__()


s = Stack()

r = BinaryTree('+')
r.insertLeft('*')
r.insertRight('/')
r.getLeftChild().insertLeft('5')
r.getLeftChild().insertRight('3')
r.getRightChild().insertLeft('24')
r.getRightChild().insertRight('8')

for i in r.postOrder([]):
    print(f'--> {s.evaluate_upn(i)}')
```
