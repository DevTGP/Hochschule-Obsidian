![[Hochschule/Module/OOP Einführung/Übung/OOPE_Abgabe_05.excalidraw.md#^area=TzlEdWyHApewbKpj07M4h|100%]]

<div style='page-break-after: always;'></div>

```java
import utilities.TastaturEingabe;

public class Time24 {
    private int hour, minute;

    public Time24(int hour, int minute) {
        this.hour = hour;
        this.minute = minute;
        normalizeTime();
    }

    public Time24() {
        this(0, 0);
    }

    public Time24(Time24 time) {
        this(time.hour, time.minute);
        normalizeTime();
    }

    public static void main(String[] args) {

        // Testst aus der Tabelle
        Time24 sanfrancisco = new Time24();
        sanfrancisco.setHour(14);
        sanfrancisco.setMinute(80);
        System.out.println("Soll-Wert : 15:20:");
        sanfrancisco.writeTime();

        Time24 frankfurt = new Time24();
        frankfurt.setHour(27);
        frankfurt.setMinute(15);
        System.out.println("Soll-Wert : 3:15:");
        frankfurt.writeTime();

        Time24 melbourne = new Time24();
        melbourne.setHour(22);
        melbourne.setMinute(150);
        System.out.println("Soll-Wert : 0:30:");
        melbourne.writeTime();

        // b)
        sanfrancisco.readTime();
        frankfurt = new Time24(sanfrancisco);
        melbourne = new Time24(sanfrancisco);
        frankfurt.addTime(9 * 60);
        melbourne.addTime(17 * 60);

        sanfrancisco.writeTime();
        frankfurt.writeTime();
        melbourne.writeTime();
    }

    public void readTime() {
        this.hour = TastaturEingabe.readInt("Stunde: ");
        this.minute = TastaturEingabe.readInt("Minute: ");
        normalizeTime();
    }

    public void writeTime() {
        System.out.println(this.hour + ":" + this.minute);
    }

    public void addTime(int minutes) {
        if (minutes >= 0)
            this.minute += minutes;
        normalizeTime();
    }

    public int getHour() {
        return this.hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
        normalizeTime();
    }

    public int getMinute() {
        return this.minute;
    }

    public void setMinute(int minute) {
        this.minute = minute;
        normalizeTime();
    }

    private void normalizeTime() {
        if (this.minute >= 59) {
            this.hour += this.minute / 60;
            this.minute %= 60;
        }

        if (this.hour >= 23) {
            this.hour %= 24;
        }
    }

    public String toString() {
        return this.hour + ":" + this.minute;
    }
}
```
