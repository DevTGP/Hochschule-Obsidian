[[Einführung in die Programmierung]]

---

```python
def addiere(a, b): 
	"""Gibt die Summe von a und b zurück."""
	return a + b
	
print(help(addiere))  # Zeigt den Docstring an
```
^codeblock-docstrings-singleline

```python
def multipliziere(a, b):
	"""
	Berechnet das Produkt von a und b.
	
	Parameter:
	a (int, float): Erster Faktor
	b (int, float): Zweiter Faktor
	
	Rückgabewert:
	int, float: Das Produkt von a und b
	"""
	return a * b

print(help(multipliziere))  # Zeigt den Docstring an
```
^codeblock-docstrings-multiline
