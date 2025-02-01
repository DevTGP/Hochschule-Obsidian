[[Systemkomponenten]]

---

> [!check] Definition
> Das **Adresswerk** ist eine Komponente der CPU, die für die Berechnung und Verwaltung von Speicheradressen verantwortlich ist.

> [!error] Aufgaben
> 1. **Adressberechnung**: Erzeugt Speicheradressen für Befehle und Daten.
> 2. **Adressierung**: Bestimmt den Speicherbereich für Lese- und Schreiboperationen.
> 3. **Verwaltung von Adressregistern**: Nutzt spezielle Register (z. B. Stack Pointer, Basis- und Indexregister).
> 4. **Speicherzugriffskontrolle**: Steuert den Datenfluss zwischen CPU und Speicher.

> [!info] Merkmale
> - berechnet nach Vorgabe des Steuerwerks aus Register- oder Speicherinhalten die Adressen von Operanden
> 
>> [!question] Warum macht das nicht das Rechenwerk?
>> - Zur Adressberechnung sind nur wenige Operationen erforderlich (i.A. Addition und Subtraktion)
>> - Adressen haben ggf. eine andere Wortbreite als die Daten
>> - Adresswerk und Rechenwerk können parallel arbeiten
>> - früher / einfachen Prozessoren gibt es tatsächlich kein eigenständiges Adresswerk

> [!tip] Aufbau
> ![[Adresswerk Bild.png]]
