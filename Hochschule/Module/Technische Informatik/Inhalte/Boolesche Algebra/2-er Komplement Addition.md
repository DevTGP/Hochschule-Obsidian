[[2-er Komplement]]

---

> [!info] Addition im 2er Komplement
>> [!error]- Regeln
>> Addiere die Zahlen wie binäre Zahlen ([[Binärsystem Addition]]). Ignoriere den Übertrag und behalte das Vorzeichen im MSB bei.
>> 1. **Binär addieren**: Addiere die beiden Zahlen bitweise, einschließlich Vorzeichenbit.
>> 2. **Übertrag ignorieren**: Falls ein Übertrag aus dem höchstwertigen Bit entsteht, wird er verworfen.
>> 3. **Vorzeichen beachten**: Das Ergebnis ist im Zweierkomplement, und das Vorzeichen wird durch das MSB (höchstwertiges Bit) bestimmt:
>>     - 0: positiv
>>     - 1: negativ.
>
>> [!example]- Beispiele
>>> [!note]- **Beispiel**: 5 + (-3) im 4-Bit-System:
>>> 5 = 0101, -3 = 1101 ([[2-er Komplement]]).
>>> - Addiere: 0101 + 1101 = 10010
>>> - Ignoriere den Übertrag (1): Ergebnis 0010.
>>> - 0010 = 2.
>>> 
>>> Das Ergebnis ist korrekt: 5+(−3)=25 + (-3) = 2.
^main
