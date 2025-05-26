![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_06.excalidraw.md#^area=IMEzLXOyUdBkSev5AhG3m|100%]]

<div style='page-break-after: always;'></div>

![[OOPE_mnpr3456_A06_Anhang_1.excalidraw|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_06.excalidraw.md#^area=0-gos0kemJ6Zx9VZMcd0_|100%]]

<div style='page-break-after: always;'></div>

```java
public class Auto {
    private int kmStand;
    private double verbrauch, tankVolumen, kraftstoffVorrat;

    public Auto(int kmStand, double verbrauch, double tankVolumen, double kraftstoffVorrat) {
        this.kmStand = kmStand;
        this.verbrauch = verbrauch;
        this.tankVolumen = tankVolumen;
        this.kraftstoffVorrat = Math.min(kraftstoffVorrat, tankVolumen);
    }

    public Auto() {
        this(0, 10d, 50d, 30d);
    }

    public static void main(String[] args) {
        Auto goggoMobil = new Auto(0, 5d, 50d, 30d);
        goggoMobil.fahren(300);
        goggoMobil.tanken(45d);
    }

    public void info() {
        System.out.println("Kilometerstand: " + kmStand + "km, Kraftstoff Vorrat: " + kraftstoffVorrat + "l");
    }

    public String toString() {
        return "Kilometerstand: " + kmStand + "km, Kraftstoff Vorrat: " + kraftstoffVorrat + "l, Verbrauch: " + verbrauch + "l/100km, Tank Volumen: " + tankVolumen + "l";
    }

    public void fahren(int km) {
        if (km < kraftstoffVorrat * verbrauch / 100) {
            kmStand += km;
            kraftstoffVorrat -= km * verbrauch / 100;
        } else {
            kmStand += (int) (kraftstoffVorrat * verbrauch / 100);
            kraftstoffVorrat = 0;
        }
    }

    public void tanken(double liter) {
        kraftstoffVorrat = Math.min(kraftstoffVorrat + liter, tankVolumen);
    }
}


class Omnibus extends Auto {
    private int anzahlSitze;

    public Omnibus(int kmStand, double verbrauch, double tankVolumen, double kraftstoffVorrat, int anzahlSitze) {
        super(kmStand, verbrauch, tankVolumen, kraftstoffVorrat);
        this.anzahlSitze = anzahlSitze;
    }

    public Omnibus() {
        this(0, 10d, 50d, 30d, 4);
    }

    public static void main(String[] args) {
        Omnibus bogdoMobil = new Omnibus(0, 5d, 50d, 30d, 4);
        bogdoMobil.fahren(300);
        bogdoMobil.tanken(45d);
    }

    public String toString() {
        return super.toString() + ", Anzahl Sitze: " + anzahlSitze;
    }
}
```
