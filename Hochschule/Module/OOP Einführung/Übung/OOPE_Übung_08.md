![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_08.excalidraw.md#^area=kfoFqYYqInEMeuNc2k2Sy|100%]]

![[Hochschule/Module/OOP Einführung/Übung/OOPE_Übung_08.excalidraw.md#^area=avzMMzdbGfKGVDwP7xyuE|100%]]

```java
public abstract class Konto {
    private static double gebuehr = 0.02;
    public final double UMRECHNUNGSFAKTOR_EUR_USD = 1.08;
    protected double saldo;
    protected String waehrung;
    private long kontonr, blz;
    private String institut;
    private String inhaber;

    public Konto(long kontonr, long blz, String institut, String inhaber, String waehrung) {
        this.kontonr = kontonr;
        this.blz = blz;
        this.institut = institut;
        this.inhaber = inhaber;
        this.waehrung = waehrung;
    }

    public double getGebuehr() {
        return gebuehr;
    }

    public void setGebuehr(double gebuehr) {
        Konto.gebuehr = gebuehr;
    }

    public abstract double verfuegbar();

    public void buchen(double bewegung) {
        saldo += bewegung;
    }

    public void dollarUmstellung() {
        if (waehrung.equals("EUR")) {
            waehrung = "USD";
            saldo *= UMRECHNUNGSFAKTOR_EUR_USD;
        }
    }

    public void euroUmstellung() {
        if (waehrung.equals("USD")) {
            waehrung = "EUR";
            saldo /= UMRECHNUNGSFAKTOR_EUR_USD;
        }
    }

    public void druckeKontoBlatt() {
        System.out.println("Konto-Nr.: " + kontonr + "BLZ: " + blz + "Institut: " + institut + "Inhaber: " + inhaber + "Waehrung: " + waehrung + "Saldo: " + saldo);
    }
}

class Girokonto extends Konto {
    private double kreditrahmen;

    public Girokonto(long kontonr, long blz, String institut, String inhaber, String waehrung, double kreditrahmen) {
        super(kontonr, blz, institut, inhaber, waehrung);
        this.kreditrahmen = kreditrahmen;
    }

    public double getKreditrahmen() {
        return kreditrahmen;
    }

    public void setKreditrahmen(double kreditrahmen) {
        this.kreditrahmen = kreditrahmen;
    }

    public double verfuegbar() {
        return saldo + kreditrahmen;
    }

    @Override
    public void buchen(double bewegung) {
        super.buchen(bewegung);
        if (saldo + bewegung > -kreditrahmen) {
            saldo += bewegung - getGebuehr();
        }
    }

    @Override
    public void dollarUmstellung() {
        super.dollarUmstellung();
        if (waehrung.equals("EUR")) {
            kreditrahmen *= UMRECHNUNGSFAKTOR_EUR_USD;
        }
    }

    public void euroUmstellung() {
        super.euroUmstellung();
        if (waehrung.equals("USD")) {
            kreditrahmen /= UMRECHNUNGSFAKTOR_EUR_USD;
        }
    }
}
```
