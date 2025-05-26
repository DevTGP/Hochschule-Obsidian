![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_06.excalidraw.md#^area=DO_1UiTYCX9Fl570pz_Qm|100%]]

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

    def preOrder(self, l):
        l.append(self.getRootVal())
        if self.getLeftChild():
            self.getLeftChild().preOrder(l)
        if self.getRightChild():
            self.getRightChild().preOrder(l)
        return l

    def inOrder(self, l):
        if self.getLeftChild():
            self.getLeftChild().inOrder(l)
        l.append(self.getRootVal())
        if self.getRightChild():
            self.getRightChild().inOrder(l)
        return l

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('10')
r.insertLeft('3')
r.getLeftChild().insertRight('1')
r.getLeftChild().getRightChild().insertLeft('4')
r.insertRight('2')
r.getRightChild().insertLeft('9')
r.getRightChild().getLeftChild().insertRight('7')
r.getRightChild().insertRight('5')
r.getRightChild().getRightChild().insertLeft('8')

print(r.preOrder([]))
print(r.inOrder([]))
```

Baum kann nicht beide Orders gleichzeitig erfüllen

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_06.excalidraw.md#^area=k6NBjDHv6aycaNgQ2An5n|100%]]

```python
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
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

    def preOrder(self, l):
        l.append(self.getRootVal())
        if self.getLeftChild():
            self.getLeftChild().preOrder(l)
        if self.getRightChild():
            self.getRightChild().preOrder(l)
        return l

    def inOrder(self, l):
        if self.getLeftChild():
            self.getLeftChild().inOrder(l)
        l.append(self.getRootVal())
        if self.getRightChild():
            self.getRightChild().inOrder(l)
        return l

    def delete(self, val):
        if self.getLeftChild() and self.getLeftChild().getRootVal() == val and self.getLeftChild().getLeftChild() is None and self.getLeftChild().getRightChild() is None:
            self.leftChild = None
        elif self.getRightChild() and self.getRightChild().getRootVal() == val and self.getRightChild().getLeftChild() is None and self.getRightChild().getRightChild() is None:
            self.rightChild = None
        elif self.getLeftChild() and self.getLeftChild().getRootVal() == val and self.getLeftChild().getLeftChild() and self.getLeftChild().getRightChild() is None:
            self.leftChild = self.leftChild.leftChild
        elif self.getLeftChild() and self.getLeftChild().getRootVal() == val and self.getLeftChild().getRightChild() and self.getLeftChild().getLeftChild() is None:
            self.leftChild = self.leftChild.rightChild
        elif self.getRightChild() and self.getRightChild().getRootVal() == val and self.getRightChild().getLeftChild() and self.getRightChild().getRightChild() is None:
            self.rightChild = self.rightChild.leftChild
        elif self.getRightChild() and self.getRightChild().getRootVal() == val and self.getRightChild().getRightChild() and self.getRightChild().getLeftChild() is None:
            self.rightChild = self.rightChild.rightChild
        else:
            1

        if self.getLeftChild():
            self.getLeftChild().delete(val)
        if self.getRightChild():
            self.getRightChild().delete(val)

    def insert(self, val):
        if self.getRootVal() == val:
            return
        if val < self.getRootVal():
            if self.getLeftChild() is None:
                self.insertLeft(val)
            else:
                self.getLeftChild().insert(val)
        elif val > self.getRootVal():
            if self.getRightChild() is None:
                self.insertRight(val)
            else:
                self.getRightChild().insert(val)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def member(self, key):
        return self._search_node(self.root, key)

    def _search_node(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_node(node.left, key)
        else:
            return self._search_node(node.right, key)


# r = BinaryTree(6)
# r.insert(3)
# r.insert(8)
# r.insert(0)
# r.insert(5)
# r.insert(1)
# r.insert(4)
# r.insert(11)
# r.insert(9)
# print(r.preOrder([]))
# r.delete(1)
# print(r.preOrder([]))
# r.delete(5)
# print(r.preOrder([]))

r = BinaryTree(7)
r.insert(3)
r.insert(9)
r.insert(0)
r.insert(5)
r.insert(8)
r.insert(11)
r.insert(1)
r.insert(4)
r.insert(6)
r.insert(10)
print(r.preOrder([]))
r.delete(7)
print(r.preOrder([]))
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_06.excalidraw.md#^area=qUQQamrCAKi4WeAiGdbiN|100%]]

```python
class BinaryTree(object):
    def __init__(self, root_obj):
        self._val = root_obj
        self._lnode = None
        self._rnode = None
        self._height = 1
        self._node_count = 1

    def rnode(self):
        return self._rnode

    def lnode(self):
        return self._lnode

    def insert_lnode(self, new_node):
        if self._lnode is None:
            self._lnode = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._lnode = self._lnode
            self._lnode = t

    def insert_rnode(self, new_node):
        if self._rnode is None:
            self._rnode = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._rnode = self._rnode
            self._rnode = t

    def insert(self, val):
        if self.val() == val:
            return
        if val < self.val():
            if self._lnode is None:
                self.insert_lnode(val)
            else:
                self._lnode.insert(val)
        elif val > self.val():
            if self.rnode() is None:
                self.insert_rnode(val)
            else:
                self.rnode().insert(val)

    def val(self, obj=None):
        if obj:
            self._val = obj
            return True
        return self._val

    def search(self, key):
        return self._search_rec(self._val, key)

    def _search_rec(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.rnode()), self.height(node.lnode()))

    def post_order(self, l):
        if self._lnode:
            self._lnode.post_order(l)
        if self._rnode:
            self._rnode.post_order(l)
        l.append(self._val)
        return l

    def pre_order(self, l):
        l.append(self._val)
        if self._lnode:
            self._lnode.pre_order(l)
        if self._rnode:
            self._rnode.pre_order(l)
        return l

    def in_order(self, l):
        if self._lnode:
            self._lnode.in_order(l)
        l.append(self._val)
        if self._rnode:
            self._rnode.in_order(l)
        return l

    def delete(self, key):
        self._val = self._delete_rec(self, key).val()

    def _delete_rec(self, node, key):
        if node is None:
            return None
        elif key > node.val():
            node._rnode = self._delete_rec(node.rnode(), key)
        elif key < node.val():
            node._lnode = self._delete_rec(node.lnode(), key)
        else:
            if node.lnode() is None and node.rnode() is None:
                return None
            if node.lnode() is None:
                return node.rnode()
            if node.rnode() is None:
                return node.lnode()

            min_larger_node = self.min_node(node.rnode())
            node._val = min_larger_node.val()
            node.rnode = self._delete_rec(node.rnode(), min_larger_node.val())
        return node

    def min_node(self, node):
        if node and node.lnode() is None:
            return node
        return self.min_node(node.lnode())

    def __str__(self):
        return str(f'BinaryTree: {self.val()}')


r = BinaryTree(6)
for i in [3, 8, 0, 5, 1, 4, 11, 9]:
    r.insert(i)
print(r.pre_order([]))
r.delete(1)
print(r.pre_order([]))
r.delete(5)
print(r.pre_order([]))

r = BinaryTree(7)
for i in [3, 9, 0, 5, 8, 11, 1, 4, 6, 10]:
    r.insert(i)
print(r.pre_order([]))
r.delete(7)
print(r.pre_order([]))
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Datenstrukturen & Algorithmen/Übung/DA_Übung_06.excalidraw.md#^area=4dDkpUZ99zN3taR5tuhx0|100%]]

![[DA_Übung_06_Anhang_1.excalidraw]]
