![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_07.excalidraw.md#^area=gFBH6vBfR-x1qPtBo0l8J|100%]]

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Soll: reverseInt(1234) == 4321\nIst: " + reverseInt(1234) + "\n");
        System.out.println("Soll: reverseInt(1234) == 4321\nIst: " + reverseInt(1234) + "\n");
        System.out.println("Soll: reverseInt(17) == 71\nIst: " + reverseInt(17) + "\n");
        System.out.println("Soll: reverseInt(454) == 454\nIst: " + reverseInt(454) + "\n");
    }

    public static long reverseInt(int n) {
        long reversed = 0;
        while (n != 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return reversed;
    }
}
```

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_07.excalidraw.md#^area=8nvXCD2voT_ShvfFmboO9|100%]]

![[OOPE_mnpr3456_A07_Anhang_1.excalidraw|100%]]

```java
public class DemoKlasse {
    private int wert;

    public DemoKlasse(int wert) {
        this.wert = wert;
    }

    public int getWert() {
        return this.wert;
    }

    public void setWert(int wert) {
        this.wert = wert;
    }

    public DemoKlasse add(DemoKlasse other) {
        return new DemoKlasse(this.getWert() + other.getWert());
    }
}
```

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_07.excalidraw.md#^area=AyaC31KI5VcyHpdG8ILzj|100%]]

```java
public abstract class GeomObjekt {
    protected double x, y;

    public GeomObjekt(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public abstract void print();
}


class Kreis extends GeomObjekt {
    private double d;

    public Kreis(double x, double y, double d) {
        super(x, y);
        this.d = d;
    }

    public void print() {
        System.out.println("Kreis");
    }
}


class Rechteck extends GeomObjekt {
    private double l, b;

    public Rechteck(double x, double y, double l, double b) {
        super(x, y);
        this.l = l;
        this.b = b;
    }

    public void print() {
        System.out.println("Rechteck");
    }
}
```

(d)
Das 4. UML-Diagramm gibt di Beziehung korrekt wieder.
