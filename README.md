# Tropical plants
Členové týmu

1. Vít Janoš (zodpovědný za )
2. Vojtěch Kudela (zodpovědný za správu GitHub)
3. Jakub Kupčík (zodpovědný za )
4. Antonín Putala (zodpovědný za )

## ÚKOLY
> [!WARNING]
> 1. adc-zvládnot číst data z obou portů
2. PWM řízení intenzity osvětlení
3. PYTHON-zvládnout přijímat a vysílat data z UARTu
4. úprva knihoven
   - teplota, vlhkost, CUMSUM
   - získat veškerá tada z RTC
6. regulátor teploty
7. regulátor vlhkosti
8. činnost větráku

## Bloky
### ZÍSKÁNÍ DAT
1. adc-zajistit získání hodnoty z _fotorezistoru_ a _soil čidla_ (knihovna)
2. převést na _**SMYSLUPLNOU HODNOTU**_
3. zajistit získání dat z _teplotního čidla_
4. zajisti _získání dat z RTC_
5. časování odečtu
   
### REGULACE VELIČIN
1. PWM-rozjet (např na 1 LED)
2. knihovny pro relátka - každá **samostatná** knihovna bude obsahovat _**komparaci parametrů**_
3. implementace regulace osvětlení

### HMI ROZHRANÍ + UART
1. zajištění komunikace přes UART
2. vytahat data + zobrazit budíky
3. databáze
4. regulace

## Reference
1. [Climate Chamber System](https://vhdl.lapinoo.net/testbench/).
