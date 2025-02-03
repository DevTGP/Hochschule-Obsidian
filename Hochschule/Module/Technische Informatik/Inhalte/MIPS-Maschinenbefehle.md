[[Technische Informatik]]

---

> [!check] Definition
> **MIPS-Maschinenbefehle** sind **binäre Instruktionen**, die direkt von der **MIPS-CPU** ausgeführt werden. Sie gehören zur **RISC-Architektur** und sind in R-Typ, I-Typ und J-Typ unterteilt.

> [!example] Instruktionstypen
>> [!info]-  **1. R-Typ (Register-zu-Register)**
>> - **Format:** `opcode | rs | rt | rd | shamt | funct`
>> - **Allgemein:** 
>> 	- `opcode immer 000000`
>> 	- `funct rd, rs, rt`
>> 	- `shamt nur bei shift operationen`
>> - **Beispiel:** `add $t0, $t1, $t2` $\to$ **$t0 = $t1 + $t2**
>>     - Binär: `000000 01001 01010 01000 00000 100000`
>
>> [!info]-  **2. I-Typ (Immediate-Werte & Speicherzugriff)**
>> - **Format:** `opcode | rs | rt | immediate`
>> - **Allgemein:** 
>> 	- `opcode not 000000`
>> 	- `funct rt, immediate(rs)`
>> - **Beispiel:** `addi $t0, $t1, 5` → **$t0 = $t1 + 5**
>> 	- Binär: `001000 01001 01000 0000 0000 0000 0101`
>
>> [!info]-  **3. J-Typ (Sprungbefehle)**
>> - **Format:** `opcode | address`
>> - **Beispiel:** `j 0x00400000` → **Springe zur Adresse 0x00400000**
>>     - Binär: `000010 00000000000000000000000000`

> [!info] Bedeutung der einzelnen Felder
> - _[6 Bits]_ **Opcode** $\to$ Operation Code (Basisoperation der Instruktion)
> - _[5 Bits]_  **RS** $\to$ Register Source (Operand 1)
> - _[5 Bits]_  **RT** $\to$ Register Target (Operand 2)
> - _[5 Bits]_  **RD** $\to$ Register Desitnation (Zielregister)
> - _[5 Bits]_  **SHAMT** $\to$ Shift-Amount (Anzahl der zu verschiebenden Bits)
> - _[6 Bits]_  **FUNCT** $\to$ Function Code (Variante der Basisoperation)
> - _[16 Bits]_  **Immediate** $\to$ Immediate (Konstante / Adresse)
> - _[26 Bits]_  **Address** $\to$  Jump Adresse (Adresse)

> [!quote]- Register in der MIPS-Architektur
> ![[MIPS-Rechnerarchitektur#^Register]]

> [!quote]- Core Instruction Set
| Typ   | Name                                   | Mnemonic     | Opcode/Funct     |
| ----- | -------------------------------------- | ------------ | ---------------- |
| R     | Add                                    | add          | 0 / 100000       |
| I     | Add Immediate                          | addi         | 001000           |
| I     | Add Immediate Unsigned                 | addiu        | 001001           |
| R     | Add Unsigned                           | addu         | 0 / 100001       |
| R     | Subtract                               | sub          | 0 / 100010       |
| R     | Subtract Unsigned                      | subu         | 0 / 100011       |
| ----- | -------------------------------------- | ------------ | ---------------- |
| R     | And                                    | and          | 0 / 100100       |
| I     | And Immediate                          | andi         | 001100           |
| R     | Nor                                    | nor          | 0 / 100111       |
| R     | Or                                     | or           | 0 / 100101       |
| I     | Or Immediate                           | ori          | 001101           |
| ----- | -------------------------------------- | ------------ | ---------------- |
| R     | Shift Left Logical                     | sll          | 0 / 0            |
| R     | Shift Right Logical                    | srl          | 0 / 000010       |
| ----- | -------------------------------------- | ------------ | ---------------- |
| R     | Set Less Than                          | slt          | 0 / 101010       |
| I     | Set Less Than Immediate                | slti         | 001010           |
| I     | Set Less Than Immediate Unsigned       | sltiu        | 001011           |
| R     | Set Less Than Unsigned                 | sltu         | 0 / 101011       |
| ----- | -------------------------------------- | ------------ | ---------------- |
| I     | Branch On Equal                        | beq          | 000100           |
| I     | Branch On Not Equal                    | bne          | 000101           |
| J     | Jump                                   | j            | 000010           |
| J     | Jump and Link                          | jal          | 000011           |
| J     | Jump Register                          | jr           | 0 / 0010000      |
| ----- | -------------------------------------- | ------------ | ---------------- |
| I     | Load Byte Unsigned                     | lbu          | 100100           |
| I     | Load Halfword Unsigned                 | lhu          | 100101           |
| I     | Load Upper Immediate                   | lui          | 001111           |
| I     | Load Word                              | lw           | 100011           |
| I     | Store Byte                             | sb           | 101000           |
| I     | Store Halfword                         | sh           | 101001           |
| I     | Store Word                             | sw           | 101011           |
