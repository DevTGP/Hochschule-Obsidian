[[Systemkomponenten]]

---

> [!check] Definition
> Das **Steuerwerk (Control Unit, CU)** ist eine zentrale Komponente der CPU, die den Ablauf der Befehlsverarbeitung steuert.

> [!error] Aufgaben
> 1. **Befehlsholung (Fetch)**: Holt den nächsten Befehl aus dem Speicher.
> 2. **Befehlsdekodierung (Decode)**: Interpretiert den Befehl und bestimmt die auszuführende Operation.
> 3. **Steuerung der Ausführung (Execute)**: Koordiniert die Ausführung durch Aktivierung der notwendigen Komponenten (ALU, Register, Speicherzugriffe).
> 4. **Takt- und Signalsteuerung**: Synchronisiert Abläufe mit dem Systemtakt.

> [!info] Merkmale
> - beinhaltet den aktuellen abzuarbeitenden Befehl im Befehlsregister.
> - ist mit allen Komponenten der CPU über einen gemultiplexten Steuerbus oder über seperate Steuerleitungen verbunden.
> - es werden sowohl die CPU-internen als auch (über den Systembus) CPU-externe Komponenten gesteuert.

> [!tip] Aufbau
> Besteht aus:
> - Befehlsregister
> - Steuerregister
> - Befehlsdecoder
>
> ![[Steuerwerk Bild.png]]
