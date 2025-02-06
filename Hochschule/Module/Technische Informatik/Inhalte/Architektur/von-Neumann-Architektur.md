[[Architektur]]

---

> [!check] Definition
> Die von-Neumann-Architektur ist ein Computermodell, bei dem ein einzelner Speicher sowohl für Daten als auch für Programme genutzt wird. Sie umfasst folgende Hauptkomponenten:
> 
> 1. **Zentraleinheit (CPU)**: Führt Berechnungen und Steuerung aus.
> 2. **Speicher**: Hält sowohl Programme als auch Daten.
> 3. **Ein- und Ausgabegeräte (I/O)**: Ermöglichen die Kommunikation mit der Außenwelt.
> 4. **[[Steuereinheit]]**: Lädt Befehle aus dem Speicher und steuert deren Ausführung.
> 5. **Recheneinheit ([[ALU]])**: Führt mathematische und logische Operationen aus.
> 
> Das Programm wird in sequenzieller Reihenfolge aus dem Speicher geladen und ausgeführt.

> [!tip] Aufbau
> ![[von Neumann-Architektur Bild.png]]

> [!error] von-Neumann-Flaschenhals
> Der **Von-Neumann-Flaschenhals** beschreibt die Leistungsbegrenzung von Computersystemen, die nach der **Von-Neumann-Architektur** arbeiten.
> 
> **Problem:**
> - In der Von-Neumann-Architektur teilen sich **Daten** und **Programme** denselben Speicher und denselben Bus.
> - Der **Speicherbus** hat eine begrenzte Bandbreite, wodurch die CPU oft warten muss, bis Daten oder Instruktionen geladen sind.
> - Dadurch entsteht eine **Datenflussbegrenzung**, die die gesamte Systemgeschwindigkeit reduziert.
>
> **Folgen:**
> 
> - Begrenzte **Datenübertragungsrate** zwischen Speicher und CPU.
> - **Leerlaufzeiten der CPU**, wenn der Speicherzugriff zu langsam ist.
> - Problem verstärkt sich mit steigender **Prozessorleistung** (CPU wird schneller als die Speicheranbindung).
