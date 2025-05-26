![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_05.excalidraw.md#^area=LqKksMQXvLjuMm3TDOtg0|100%]]

1 )

![[OOPE_Übung_05_Anhang_1]]

2 )

```java
public class Radio {
    String band;
    int lautstaerke;
    int kanal;

    Radio(String b, int l, int k) {
        if (b.equals("UKW") || b.equals("MW") || b.equals("LW")) {
            band = b;
        } else {
            band = "UKW";
        }

        if (l >= 0 && l <= 10) {
            lautstaerke = l;
        } else {
            lautstaerke = 1;
        }

        if (k >= 1 && k <= 5) {
            kanal = k;
        } else {
            kanal = 1;
        }
    }

    Radio() {
        this("UKW", 1, 1);
    }

    Radio(String b) {
        this(b, 1, 1);
    }

    Radio(int k) {
        this("UKW", 1, k);
    }

    void lautstaerkeErhoehen(int i) {
        if (i >= 0) {
            lautstaerke += i;
            lautstaerke %= 11;
        }
    }

    void lautstaerkeVermindern(int i) {
        if (i <= 0) {
            lautstaerke += i;
            lautstaerke %= 11;
            if (lautstaerke < 0) {
                lautstaerke += 10;
            }
        }
    }

    void kanalWechseln(int i) {
        kanal++;
        if (kanal == 6) {
            kanal = 1;
        }
    }

    void ausgabe() {
        System.out.println("Das Radio ist eingestellt auf Band: " + band);
        System.out.println("Lautstaerke: " + lautstaerke);
        System.out.println("Kanal: " + kanal);
        System.out.println();
    }
}


public class Main {
    public static void main(String[] args) {
        System.out.println((5 - 10) % 11 + 10);
        Radio kofferRadio = new Radio();
        kofferRadio.ausgabe();
        kofferRadio.lautstaerkeErhoehen(25);
        kofferRadio.ausgabe();
        Radio boomBox = new Radio("LKW");
        boomBox.lautstaerkeVermindern(12);
        boomBox.ausgabe();
        boomBox = new Radio("MW");
        boomBox.ausgabe();
        Radio ghettoBlaster = new Radio(4);
        Radio autoRadio = new Radio("UKW", 5, 5);
        ghettoBlaster.ausgabe();
        autoRadio.ausgabe();
    }
}
```

<div style='page-break-after: always;'></div>

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_05.excalidraw.md#^area=T2O4Oi5E9qnTuPUbXPD0e|100%]]

```java
public class BBQ {
    String grillGut;
    double kohle;
    String raeucherHolz = "Kirsche";
    String grillGeraet = "FarmerGrill";
    int zeit;

    BBQ(String grillGut, double kohle, int zeit) {
        this.grillGut = grillGut;
        this.kohle = kohle;
        if (kohle < 0) {
            this.kohle = 0;
        }
        this.zeit = zeit;
        if (zeit < 0) {
            this.zeit = 0;
        }
    }

    void aendereRaeucherHolz(String holz) {
        this.raeucherHolz = holz;
    }

    String getGrillGeraet() {
        return this.grillGeraet;
    }

    void setGrillGeraet(String grillGeraet) {
        this.grillGeraet = grillGeraet;
    }

    void kohleNachlegen(double kohle) {
        this.kohle += kohle;
    }

    boolean istFertig() {
        return this.zeit <= 0;
    }

    boolean grillen(double zeit) {
        if (zeit >= 0 && this.kohle * 60 >= this.zeit) {
            this.kohle -= zeit / 60d;
            this.zeit -= zeit; // implizit this.zeit = int(this.zeit - zeit)
            return true;
        }
        return false;
    }

    void ausgabe() {
        System.out.println(this.grillGut + " muss noch " + this.zeit + " Minuten auf dem Grill " + this.grillGeraet + " gegrillt werden.");
        System.out.println("Das Raeucherholz ist " + this.raeucherHolz + " und es sind noch " + this.kohle + " kg Kohle vorhanden.");
        if (this.istFertig()) {
            System.out.println("Das Essen ist fertig.");
        } else {
            System.out.println("Das Essen ist noch nicht fertig. Es dauert noch " + this.zeit + ".");
        }
    }
}
```
