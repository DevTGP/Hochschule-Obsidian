[[2-er Komplement]]

---

> [!info] Subtraktion im 2er Komplement
>> [!error]- Regeln
>> Subtrahiere die Zahlen wie binäre Zahlen ([[Binärsystem Subtraktion]]). Ignoriere den Übertrag und behalte das Vorzeichen im MSB bei.
>> 1. Konvertiere den Subtrahenden ins 2er-Komplement (Invertieren der Bits und 1 addieren).
>> 2. Addiere den Minuenden und das 2er-Komplement des Subtrahenden.
>> 3. Ignoriere den Übertrag (Carry-Out), falls vorhanden.
>
>> [!example]- Beispiele
>>> [!note]- **Beispiel**: 7 - 3 im 4-Bit-System:
>>> 1. **Darstellung von 7: 0111.**
>>> 2. **Darstellung von 3: 0011.**
>>> 3. **Bildung des 2er-Komplements von 3:**
>>>     - Invertiere Bits: 1100.
>>>     - Addiere 1: 1100 + 1 = 1101.
>>> 4. **Addition von 7 und -3:**
>>>     0111 + 1101 = 10100.
>>> 5. **Ignoriere Übertrag (5 Bit auf 4 Bit):**
>>>     0100.
>>>     
>>> **Ergebnis:** 7 - 3 = 4 (0100).
^main
