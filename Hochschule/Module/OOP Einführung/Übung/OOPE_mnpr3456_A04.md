![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_04.excalidraw.md#^area=rQA32enKfvrYFFxaab0zK|100%]]

```java
import utilities.TastaturEingabe;

public class Main {
    public static void main(String[] args) {
        int x, sum = 0, count = 0;
        double avg;

        do {
            x = TastaturEingabe.readInt("Bitte eine Zahl eingeben: ");
            sum += x;
            count++;
            avg = (double) sum / (count);
            System.out.println("Summe: " + sum + " Avg: " + avg);
        } while (x >= 0);
    }
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_04.excalidraw.md#^area=bmaDmi10BDg-g75e_Do4x|100%]]

<div style='page-break-after: always;'></div>

`Main.java`

```java
public class Main {
    public static void main(String[] args) {
        Pi pi = new Pi();

        System.out.println("Pi = " + pi.main());
    }
}
```

<div style='page-break-after: always;'></div>

`Pi.java`

```java
import utilities.TastaturEingabe;

public class Pi {
    Pi() {
    }

    double main() {
        int count = TastaturEingabe.readInt("Anzahl der Iterationen: ");
        int pointsIn = 0, pointsOut = 0;

        for (int i = 0; i < count; i++) {
            double x = Math.random();
            double y = Math.random();

            if (x * x + y * y <= 1) {
                pointsIn++;
            } else {
                pointsOut++;
            }
        }
        return 4d * (double) pointsIn / (double) (pointsOut + pointsIn);
    }
}
```
