![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_06.excalidraw.md#^area=MM8WbQAlU8S8d8pQtIv9V|100%]]

```java
public class Main {
	public static void main(String[] args) {
		System.out.println(reku(1, 2, 3));
	}

    static double reku(double a, double b, int n) {
        if (n == 1) return a + b;
        else if (n == 0) return 1;
        return (a + b) * reku(a, b, n - 1);
    }
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_06.excalidraw.md#^area=82FXGgkQAHRWBpZ1lJmu5|100%]]

a)

1. `Mitarbeiter` (Basisklasse)

    - Attribute:
        - `name: str` – (private)
        - `rvNr: str` – (private)
    - Methode:
        - `mitarbeiterInfo(): void` – (protected)
        - `tarifErhoehung(): void` – (protected, abstract)

2. `Angestellter` (abgeleitet)

    - Attribute:
        - `gehalt: double` – (private)
    - Methode:
        - `mitarbeiterInfo(): void` – (public)
        - `tarifErhoehung(): void` – (public)

3. `Arbeiter` (abgeleitet)
    - Attribute:
        - `stundenlohn: double` – (private)
        - `stunden: double` – (private)
    - Methode:
        - `mitarbeiterInfo(): void` – (public)
        - `tarifErhoehung(): void` – (public)

b)
![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_06_Anhang_1.excalidraw.md#^area=S2J9CnurNftjYrq-SfcTk|100%]]
![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_06_Anhang_1.excalidraw.md#^area=amYXIFgL50Wb-zYBhxPNK|100%]]
![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_06_Anhang_1.excalidraw.md#^area=3Ggg65i22K07SCxzeBJdS|100%]]

c)

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_06.excalidraw.md#^area=f1xxfRXN59gVF4rwOpfsj|100%]]

Die Methode sollte $\text{ abstract }$ sein, damit sichergestellt wird, dass diese implementiert wird.

```java
public abstract class Mitarbeiter {
    protected String name;
    protected String rvNr;

    public Mitarbeiter(String name, String rvNr) {
        this.name = name;
        this.rvNr = rvNr;
    }

    void mitarbeiterInfo() {
        System.out.println("Name: " + name);
        System.out.println("RV-Nr.: " + rvNr);
    }

    abstract void tarifErhoehung(double prozent);
}


class Angestellter extends Mitarbeiter {
    double gehalt;

    public Angestellter(String name, String rvNr, int gehalt) {
        super(name, rvNr);
        this.gehalt = gehalt;
    }

    void mitarbeiterInfo() {
        super.mitarbeiterInfo();
        System.out.println("Status: Angestellter");
        System.out.println("Gehalt: " + gehalt);
        System.out.println();
    }

    void tarifErhoehung(double prozent) {
        gehalt *= (1 + prozent / 100);
    }
}

class Arbeiter extends Mitarbeiter {
    double stundenlohn, anzahlStunden;

    public Arbeiter(String name, String rvNr, double stundenlohn, double anzahlStunden) {
        super(name, rvNr);
        this.stundenlohn = stundenlohn;
        this.anzahlStunden = anzahlStunden;
    }

    void mitarbeiterInfo() {
        super.mitarbeiterInfo();
        System.out.println("Status: Arbeiter");
        System.out.println("Stundenlohn: " + stundenlohn);
        System.out.println("Anzahl Stunden: " + anzahlStunden);
        System.out.println("Arbeitslohn: " + (stundenlohn * anzahlStunden));
        System.out.println();
    }

    void tarifErhoehung(double prozent) {
        stundenlohn *= (1 + prozent / 100);
    }

}

class MitarbeiterTest {
    public static void main(String[] args) {
        // zwei Angestellte und einen Arbeiter deklarieren
        Angestellter boss, dilbert;
        Arbeiter dogbert;

        // ... und erzeugen
        boss = new Angestellter("The Pointy Haired Boss", "221-45-7632", 15000);
        dilbert = new Angestellter("Dilbert", "234-67-8901", 7500);
        dogbert = new Arbeiter("Dogbert", "896-54-3217", 250.00, 160);

        // alle Informationen ueber Dilbert ausgeben
        dilbert.mitarbeiterInfo();

        // das Gleiche fuer den Chef
        boss.mitarbeiterInfo();

        // Dogbert erhaelt einen hoeheren Stundenlohn
        dogbert.tarifErhoehung(20d);

        // alle Informationen ueber Dogbert ausgeben
        dogbert.mitarbeiterInfo();
    }
}

/* Ausgabe des Programms:
Name: Dilbert
RV-Nr.: 234-67-8901
Status: Angestellter
Gehalt: 7500.0

Name: The Pointy Haired Boss
RV-Nr.: 221-45-7632
Status: Angestellter
Gehalt: 15000.0

Name: Dogbert
RV-Nr.: 896-54-3217
Status: Arbeiter
Stundenlohn: 300.0
Anzahl Stunden: 160.0
Arbeitslohn: 48000.0
*/
```
