[[Systemadministration]]

---

![[Standardeingabe und -ausgabe Bild.png]]
![[Umleitung Standardausgabe Bild.png]]
![[Piping Bild.png]]


# Polling
- Abfrage basiertes Kommunikationsprinzip 
- Daten werden regelmäßig (z.B. in festen Abtastintervallen) aus dem normalen Programmablauf heraus abgefragt. 
- Das Einlesen erfolgt also immer synchron zum Kontrollfluss der abfragenden Software. 
- Es ist keine besondere Hardwareunterstützung notwendig. 
- Zustandsänderungen die sich vollständig zwischen zwei Abfragezeitpunkten abspielen gehen verloren. 
- Polling kostet auch dann Rechenzeit, wenn sich nichts geändert hat.

# Interrupt-driven
-  Ausgewählte Zustandsänderungen an Eingangskanälen oder internen Komponenten des Systems werden durch eine Unterbrechung des normalen Programmflusses und Aufruf einer zugeordneten Interrupt Service Routine – ohne auf eine Abfrage zu warten – signalisiert. 
- Eine spezielle Hardwareunterstützung ist hierzu erforderlich. 
- Auch hier können unter Umständen Zustandsänderungen verloren gehen, etwa wenn die Interrupt Service Routine nicht schnell genug abgearbeitet werden kann. Allerdings ist dies bei vernünftigem Systemdesign in aller Regel vermeidbar. 
- Interrupts beeinflussen das zeitliche Verhalten i.d.R. weniger regelmäßig als Polling 
	- Vorteil: Geringerer Rechenleistungsbedarf 
	- Nachteil: Das Zeitverhalten anderer Systemteile wird gestört und ist schlechter vorhersagbar.

Steps in starting an I/O device and getting interrupt
![[Interrupt getriebene Kommunikation Bild 1.png]]
How the CPU is interrupted
![[Interrupt getriebene Kommunikation Bild 2.png]]
