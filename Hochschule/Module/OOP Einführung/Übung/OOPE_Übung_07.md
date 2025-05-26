![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_07.excalidraw.md#^area=zsnUuO4cmIDaot_yaWiV8|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_07.excalidraw.md#^area=iMZ0hyK_YLbbR0U6gGhio|100%]]

```java
public class Flugzeug {
    private double maxGewicht, reiseGeschw, flugStunden, verbrauch, tankKapazitaet, kerosinVorrat;

    public Flugzeug(double maxGewicht, double reiseGeschw, double flugStunden, double verbrauch, double tankKapazitaet, double kerosinVorrat) {
        this.maxGewicht = maxGewicht;
        this.reiseGeschw = reiseGeschw;
        this.flugStunden = flugStunden;
        this.verbrauch = verbrauch;
        this.tankKapazitaet = tankKapazitaet;
        if (kerosinVorrat > tankKapazitaet) {
            kerosinVorrat = tankKapazitaet;
        }
        this.kerosinVorrat = kerosinVorrat;
    }

    public static void main(String[] args) {
        Flugzeug albatros = new Flugzeug(68000, 800, 500, 2000, 20000, 16000);
        System.out.println(albatros.fliegen(3000));
        albatros.tanken(5000);

        albatros.info();
        System.out.println(albatros);
        System.out.println("Reichweite: " + albatros.reichweite());
        System.out.println("Flugstunden: " + albatros.flugStunden);
        System.out.println("Verbrauch: " + albatros.verbrauch);
        System.out.println("tankKapazitaet: " + albatros.tankKapazitaet);
        System.out.println("kerosinVorrat: " + albatros.kerosinVorrat);
    }

    public void info() {
        System.out.println("Geflogene Stunden: " + flugStunden + ", Tank Inhalt: " + kerosinVorrat);
    }

    public String toString() {
        return "Maximaler Gewicht: " + maxGewicht + ", Reisegeschwindigkeit: " + reiseGeschw + ", Flugstunden: " + flugStunden + "Verbrauch: " + verbrauch + "tankKapazitaet: " + tankKapazitaet + "kerosinVorrat: " + kerosinVorrat;
    }

    public double reichweite() {
        return reiseGeschw * kerosinVorrat / verbrauch;
    }

    public boolean fliegen(double km) {
        if (km < reichweite()) {
            kerosinVorrat *= km / reichweite();
            flugStunden += km / reiseGeschw;
            return true;        } else {
            return false;
        }
    }

    public void tanken(double liter) {
        kerosinVorrat += liter;
        if (kerosinVorrat > tankKapazitaet) {
            kerosinVorrat = tankKapazitaet;
        }
    }
}


class FrachtFlugzeug extends Flugzeug {
    private double maxZuladung;

    public FrachtFlugzeug(double maxGewicht, double reiseGeschw, double flugStunden, double verbrauch, double tankKapazitaet, double kerosinVorrat, double maxZuladung) {
        super(maxGewicht, reiseGeschw, flugStunden, verbrauch, tankKapazitaet, kerosinVorrat);
        this.maxZuladung = maxZuladung;
        if (maxZuladung > maxGewicht - tankKapazitaet) {
            maxZuladung = maxGewicht - tankKapazitaet;
        }
    }

    public static void main(String[] args) {
        FrachtFlugzeug f = new FrachtFlugzeug(68000, 800, 500, 2000, 20000, 16000, 10000);
        System.out.println(f.fliegen(3000));
        f.tanken(5000);

        f.info();
        System.out.println(f);
    }

    public String toString() {
        return super.toString() + ", Maximaler Zuladung: " + maxZuladung;
    }
}
```
