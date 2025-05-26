![[OOPE_Übung_02.excalidraw#^area=5HVWzFZyBJDq6PylBwe5G|100%]]

# a)

$a = 14$

# b)

```java
int a = (2 + 3) * 4;
```

![[OOPE_Übung_02.excalidraw#^area=MM4zFyWdUDgzAm2PijEVX|100%]]

# a)

Ausgabe:

```txt
Inkompatible Typen: Möglicher Verlust bei Konvertierung von double in long
```

# b)

Man kann den double zu einem long casten:

```java
double d = 7.99;
long l = (long) d;
```

![[OOPE_Übung_02.excalidraw#^area=W3QLf6dY9vKR16Q5Cd9hD|100%]]

# a)

$b$ ist vom Typ $double$.

# b)

$a$ wird implizit zu einem $double$ konvertiert, da $2.5$ bereits ein $double$ ist.

![[OOPE_Übung_02.excalidraw#^area=yOc_PAbyOOvH2-O1nGNPo|100%]]

```java
int x = 7 / 2; // 3 (int)
float y = 7 / 2; // 3.0 (float)
float z = 7 / 2.0f; // 3.5 (float)
```

![[OOPE_Übung_02.excalidraw#^area=W1knoeUiM7wn3QhX4Hel9|100%]]
$x = -2147483648$
Da das Maximum eines $int$ $2147483647$ beträgt entsteht beim inkrementieren um $1$, ein $IntegerOverflow$, wodurch $x$ vom maximalen $int$ Wert zum minimalen $int$ Wert wird.

![[OOPE_Übung_02.excalidraw#^area=0GthErqzqDvbsqYBlsbpW|100%]]

```java
int a = 10, b = 15;
int max = a >= b ? a : b;
System.out.println("Größerer Wert: " + max);
```

![[OOPE_Übung_02.excalidraw#^area=6EX7Jn5IU7l1EjB_9OFsJ|100%]]

# a)

Ausgabe:

```txt
Bedingung erfüllt
x = 6
```

# b)

Ausgabe:

```txt
Bedingung erfüllt
x = 6
```

**The & operator always evaluates both expressions.** **The && operator evaluates the second expression only if the first expression is true**

![[OOPE_Übung_02.excalidraw#^area=9301jtqSrLZif1mc_yAda|100%]]

# a)

$c = 1$

# b)

$c = 7$

![[OOPE_Übung_02.excalidraw#^area=0G6a7JtWD03hYs5FRnWd0|100%]]

# a)

$i = 9$

# b)

Beim Cast geht jegliche Information über den Dezimalbereich eines $double$ verloren, dass heißt es wird im Prinzip beim Cast zu einem $int$ abgerundet.

![[OOPE_Übung_02.excalidraw#^area=ZDaJvXyRoRMJJ47EkNWJH|100%]]

Ausgabe:

```txt
x = 12, y = 12, z = 10
```
