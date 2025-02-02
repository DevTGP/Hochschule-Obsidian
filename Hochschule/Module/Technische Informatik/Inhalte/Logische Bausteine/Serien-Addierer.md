[[Logische Bausteine]]

---

> [!check] Definition
> Ein **Serien-Addierer** ist eine digitale Schaltung, die **mehrstellige Binärzahlen bitweise** addiert, indem sie nur **einen [[Volladdierer]] und ein Register** für den Übertrag verwendet.

> [!info] Funktion
> 1. **Bits werden nacheinander (LSB → MSB) addiert.**
> 2. **Ein [[Volladdierer]]** berechnet die Summe eines Bit-Paars pro Taktzyklus.
> 3. **Der Übertrag wird in einem Flip-Flop zwischengespeichert** und im nächsten Schritt als Carry-In verwendet.
> 4. Nach **n Takten** ist das Endergebnis verfügbar.
> 
> **Eigenschaften:**
> - **Langsam**, aber **hardwareeffizient** (nur ein [[Volladdierer]] nötig).
> - Wird in **Speicher- und Mikrocontroller-Systemen** verwendet, wenn geringe **Hardwarekosten** entscheidend sind.

> [!tip] Aufbau
> Ein **Serien-Addierer** besteht aus folgenden Hauptkomponenten:
> 1. **Register für Operanden (A und B)** – Speichern die beiden zu addierenden Binärzahlen.
> 2. **Schieberegister** – Schiebt die Bits nacheinander in den Addierer.
> 3. **Volladdierer (FA)** – Addiert die Bits von A und B sowie den Übertrag.
> 4. **Flip-Flop für Carry (C)** – Speichert den Übertrag für den nächsten Rechenschritt.
> 5. **Ergebnisregister (Summe S)** – Speichert die berechnete Summe.
> 6. **Taktgeber (Clock)** – Steuert die Addition **bitweise** über mehrere Taktzyklen.
>
> ![[Serien-Addierer Bild.png]]

> [!example] Beispiele Rechnung
>> [!note]- 01001011 + 00111111
>> ```
>>   01001011 (1. Zahl)
>> + 00111111 (2. Zahl)
>>   1111111  (Carry In/Out)
>> = 10001010
