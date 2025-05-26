[[Systemadministration]]

---

Adress- und Datenbus (Instruktionen werden i.d.R. ebenfalls über den Datenbus übertragen)
![[von Neumann Bus Bild.png]]


# Schnittstelle Prozessor <-> Speicher
![[Schnittstelle Prozessor Speicher Bild.png]]

A three-stage pipeline 
![[3-stage Pipeline Bild.png]]
SA superscalar CPU
![[Superscalar CPU Bild.png]]

# Pipelinestufen
- Fetch 
	- Laden der Instruktion aus Speicher (z.B. Cache) 
- Decode 
	- Dekodieren des Opcodes der Instruktion 
- Execute 
	- Ausführen arithmetisch/logischer Berechnungen gemäß Opcode 
- Write Back 
	- Schreiben des Ergebnisses ins Zielregister

# Ausführung in Pipeline (einfach)
Beispiel mit vierstufiger Pipeline (Fetch, Decode, Execute, Write Back)
![[Beispiel vierstufiger Pipeline Bild.png]]

# Hardware für Parallelität auf Taskebene 
## Multithreading (Hyperthreading)
- CPU hält Zustand mehrerer Threads (ausgeführte Programme) gleichzeitig 
- Sehr schnelle Umschaltung zwischen Threads in der Hardware 
- Tatsächlich wird immer nur ein Thread auf dem Prozessorkern ausgeführt (Pseudo-Parallelität)

## Multicore
