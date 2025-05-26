![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02.excalidraw.md#^area=dNsJDMwLiVX5JsMPqNbcb|100%]]

a)
Eine Hypothese ist ein vom Lernalgorithmus erzeugtes Modell oder eine Annahme, die eine Beziehung zwischen Eingabedaten und Ausgaben beschreibt.

b)
Der Hypothesenraum ist die Menge aller möglichen Hypothesen (Modelle), die ein Lernalgorithmus im Rahmen seines gewählten Modells in Betracht ziehen kann.

c)
Klassifikation ist ein maschinelles Lernverfahren, bei dem Eingabedaten in diskrete Kategorien oder Klassen eingeteilt werden.

d)
Regression ist ein Lernverfahren, bei dem ein kontinuierlicher numerischer Wert vorhergesagt wird, z. B. Temperatur oder Preis.

e)
Ockhams Razor ist ein Prinzip, das besagt: _Die einfachste Erklärung, die alle Beobachtungen erklärt, ist vorzuziehen._ Im maschinellen Lernen bedeutet das, dass man einfachere Modelle bevorzugen sollte, um Überanpassung zu vermeiden.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02.excalidraw.md#^area=HL3E_JbN80l11Bg5NZB5k|100%]]

1. Google Search

    1. Suchergebnis-Ranking (Reihenfolge der Ergebnisse)

        - **Lernansatz:** _Überwachtes Lernen_
        - **Begründung:** Google analysiert historische Nutzerdaten (z. B. worauf geklickt wurde, wie lange man auf Seiten bleibt) und trainiert Modelle, die lernen, welche Seiten für welche Anfragen „gut“ sind. Die Relevanz-Bewertungen dienen als Labels.

    2. Suchvorschläge („Meinten Sie ...?“ / Autovervollständigung)

        - **Lernansatz:** _Unüberwachtes Lernen_
        - **Begründung:** Diese Systeme analysieren riesige Mengen an Suchanfragen, um Muster und Zusammenhänge zu erkennen – z. B. häufige Kombinationen oder Korrekturen – _ohne explizite Zielwerte_.

    3. Sprachverarbeitung & BERT-Modelle (natürliche Sprache verstehen)

        - **Lernansatz:** _Vortrainiertes überwachtes und unüberwachtes Lernen (hybrid)_
        - **Begründung:** Modelle wie BERT werden zunächst unüberwacht auf großen Textmengen vortrainiert (z. B. Lückentexte), später aber überwacht feinjustiert für Aufgaben wie „Frage verstehen“ oder „richtige Antwort finden“.

    4. Personalisierung der Suche

        - **Lernansatz:** _Verstärkendes Lernen (teilweise)_
        - **Begründung:** Google kann Nutzerverhalten auswerten (z. B. Klicks, Absprungraten) und daraus lernen, welche Art von Ergebnissen langfristig bessere „Belohnung“ bringt – ähnlich wie bei verstärkendem Lernen.

2. Fingerabdruck am Smartphone
   **Lernansatz:** _Überwachtes Lernen_
   **Begründung:** Beim Einrichten gibst du mehrere Fingerabdruck-Scans ein. Diese dienen als Trainingsdaten (mit dem Label „gehört zu Nutzer“). Das Modell lernt typische Muster deines Fingerabdrucks. Beim späteren Entsperren erkennt es auch leicht abweichende, aber ähnliche Muster.

3. Musik-Empfehlungen auf Spotify
   **Lernansatz:** _Unüberwachtes Lernen_
   **Begründung:** Das System analysiert Nutzerdaten (z. B. welche Songs gehört werden) und erkennt darin Muster oder Ähnlichkeiten zwischen Nutzern oder Songs. Da es keine expliziten „richtigen“ Ausgaben gibt, sondern Cluster oder Ähnlichkeitsanalysen entstehen, handelt es sich um unüberwachtes Lernen.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02.excalidraw.md#^area=DNZwmHJ4xLeA7TcixhUfh|100%]]

a)
Nein, die Einteilung ist nicht sinnvoll, da in den Testdaten, nur "Spam" klassifizierte Mails sind, und somit nicht geprüft werden kann, ob der Filter auch Mails als "Kein Spam" klassifiziert.

b)
Nein, da 4 und 13 sich überschneiden, können diese Ergebnisse auswendig gelernt sein. Die 2 Daten sind dann zu wenig, um das Modell ordentlich testen zu können.

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02.excalidraw.md#^area=raXFHHw8J7Bs8-4-nTtP2|100%]]

![[KI_Übung_02_Entscheidungsbaum.png]]

a)

| Alt | Bar | Fri | Hun | Pat  | Price  | Rain | Res | Type    | Est   | WillWait |
| --- | --- | --- | --- | ---- | ------ | ---- | --- | ------- | ----- | -------- |
| Yes | No  | No  | Yes | Full | \$\$   | Yes  | No  | Thai    | 30-60 | No       |
| No  | Yes | Yes | Yes | Full | \$\$\$ | No   | No  | Italian | 10-30 | Yes      |
| Yes | No  | No  | Yes | Full | \$     | Yes  | Yes | Thai    | 0-10  | Yes      |

b)

| Alt | Bar | Fri | Hun | Pat  | Price  | Rain | Res | Type     | Est  | WillWait |
| --- | --- | --- | --- | ---- | ------ | ---- | --- | -------- | ---- | -------- |
| Yes | Yes | Yes | Yes | None | \$\$\$ | Yes  | Yes | FastFood | 0-10 | No       |

c)

| Alt | Bar | Fri | Hun | Pat  | Price  | Rain | Res | Type     | Est   | WillWait |
| --- | --- | --- | --- | ---- | ------ | ---- | --- | -------- | ----- | -------- |
| Yes | Yes | Yes | Yes | Full | \$\$\$ | Yes  | Yes | FastFood | 10-30 | Yes      |

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02.excalidraw.md#^area=DQ12dFAxbKpVPdI7PlL_h|100%]]

a)

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02_A5.excalidraw.md#^area=EsRS4N70F6j2dPy5zVZwm|100%]]

b)

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02_A5.excalidraw.md#^area=nQ9IVl74m-uLACU8iA9EC|100%]]

c)

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02_A5.excalidraw.md#^area=jiYxc92nk7_WjJGCrHxoG|100%]]

<div style='page-break-after: always;'></div>

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02.excalidraw.md#^area=K74edKaP0Ol1otWii3ba3|100%]]

![[KI_Übung_02_Moral_Machine.png]]

| Straße Frei | Mitfahrer | Einhalten d. Gesetz | Geschlecht | Spezies | Alter     | Sportlichkeit | Sozialer Wert | Klasse |
| ----------- | --------- | ------------------- | ---------- | ------- | --------- | ------------- | ------------- | ------ |
| Nein        | Ja        | Ja                  | F          | Mensch  | Jung      | Nein          | Hoch          | Nein   |
| Nein        | Nein      | Ja                  | M          | Mensch  | Erwachsen | Ja            | Hoch          | Ja     |

![[Hochschule/Module/Einführung in die KI/Übung/KI_Übung_02_A5.excalidraw.md#^area=4MZ0TIgGporDhJwRREjhw|100%]]
