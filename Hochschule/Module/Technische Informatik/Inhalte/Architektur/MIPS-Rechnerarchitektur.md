[[Technische Informatik]]

---

> [!check]  Definition
> Die **MIPS-Architektur** (Microprocessor without Interlocked Pipeline Stages) ist eine **[[RISC]] (Reduced Instruction Set Computing)**-Prozessorarchitektur mit einfacher und effizienter Befehlssatzstruktur.

> [!info] Eigenschaften
> - **[[Load-Store-Architektur]]**: Nur Lade- und Speicherbefehle greifen direkt auf den Speicher zu.
> - **Registerbasiert**: 32 allgemeine Register ($0–$31).
> - **Feste Befehlslänge**: Alle Instruktionen sind **32 Bit lang**.
> - **[[3 Befehlsformate]]**: R-Typ (Register-Operationen), I-Typ (Immediate-Werte), J-Typ (Sprungbefehle).
> - **5-stufige Pipeline**: IF (Fetch), ID (Decode), EX (Execute), MEM (Memory), WB (Write Back).
> - **Big- oder Little-Endian** konfigurierbar.

> [!error] Aufbau
> ![[MIPS Architektur Bild.png]]
>> [!example] Komponenten
>> 
>> ### **1. Program Counter (PC)**
>> 
>> - Enthält die Adresse des aktuellen Befehls.
>> - Wird nach jeder Instruktion um **4** erhöht (da MIPS-Befehle 4 Byte groß sind).
>> 
>> ### **2. Instruction Memory**
>> 
>> - Speichert das Programm (Befehle).
>> - Gibt den aktuellen Befehl anhand der PC-Adresse aus.
>> 
>> ### **3. Steuerwerk (Control)**
>> 
>> - Dekodiert das Befehlsformat (Opcode aus **Instruction[31-26]**).
>> - Steuert Signale wie **RegDst, Jump, Branch, MemRead, MemWrite, ALUOp**.
>> 
>> ### **4. Registersatz**
>> 
>> - 32 Register ($0–$31) für schnelle Datenverarbeitung.
>> - Liest zwei Registerwerte für ALU-Operationen.
>> - Schreibt Ergebnisse zurück.
>> 
>> ### **5. ALU (Arithmetic Logic Unit)**
>> 
>> - Führt arithmetische & logische Operationen aus (Addition, Subtraktion, AND, OR etc.).
>> - ALU-Steuerung bestimmt die genaue Operation anhand des Funktionsfeldes (**Instruction[5-0]**).
>> 
>> ### **6. Daten-Speicher (Data Memory)**
>> 
>> - Für **Load (LW)** und **Store (SW)** Befehle.
>> - MemRead & MemWrite steuern Lese- und Schreibvorgänge.
>> 
>> ### **7. Multiplexer (MUX)**
>> 
>> Entscheiden zwischen verschiedenen Eingängen, z. B.:
>> - **RegDst MUX**: Wählt das Zielregister (R-Typ oder I-Typ).
>> - **ALUSrc MUX**: Wählt ALU-Operand (Register oder Immediate).
>> - **MemtoReg MUX**: Entscheidet, ob ein Register aus dem Speicher oder ALU-Ergebnis geschrieben wird.
>> 
>> ### **8. Sign-Extend**
>> 
>> - Erweitert **16-Bit Immediate-Werte** auf **32 Bit**, um mit der ALU kompatibel zu sein.
>> 
>> ### **9. Branching & Jump-Logik**
>> 
>> - **Shift Left 2**: Schiebt Adressen um 2 Bit nach links (Wortadressierung).
>> - **Branch-Adder** berechnet Zieladressen für Sprünge.
>> - **Zero-Flag** der ALU steuert bedingte Sprünge (Branch on Equal).

> [!question] Anwendungsbereiche
> - Eingebettete Systeme
> - Netzwerkrouter
> - Navigationssysteme
> - Spielekonsolen (z. B. PlayStation 1/2).
