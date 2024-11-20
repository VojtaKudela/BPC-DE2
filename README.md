# Tropical plants :palm_tree::potted_plant::cactus:
Členové týmu

1. Vít Janoš (zodpovědný za PWM)
2. Vojtěch Kudela (zodpovědný za správu GitHub a knihoven)
3. Jakub Kupčík (zodpovědný za získání dat)
4. Antonín Putala (zodpovědný za HMI a UART)

## ÚKOLY
> [!WARNING]
> 1. adc-zvládnot číst data z obou portů
> 2. PWM řízení intenzity osvětlení
> 3. PYTHON-zvládnout přijímat a vysílat data z UARTu
> 4. úprava knihoven
>    - teplota, vlhkost, _**cumsum**_ 
>    - získat veškerá data z RTC
> 6. regulátor teploty
> 7. regulátor vlhkosti
> 8. činnost větráku

## Poznámky
> [!TIP]
> - nastavení aktuálního času
> - teplota + hystereze
> - vlhkost + hystereze
>    -  při překročení obou se spustí větrák
> - soil measure - pro informaci -> _**nepůjde regulovat**_
> - osvětlení - není třeba hystereze

> [!IMPORTANT]
> ZPRACOVÁNÍ A ZOBRAZENÍ GRAFŮ
> - teploty
> - vlhkosti
> - slanosti
> - osvětlení

## Bloky
### ZÍSKÁNÍ DAT
- [ ] 1. adc-zajistit získání hodnoty z _fotorezistoru_ a _soil čidla_ (knihovna)
- [ ] 2. převést na _**SMYSLUPLNOU HODNOTU**_
- [ ] 3. zajistit získání dat z _teplotního čidla_
- [ ] 4. zajisti _získání dat z RTC_
- [ ] 5. časování odečtu
   
### REGULACE VELIČIN
- [ ] 1. PWM-rozjet (např. na 1 LED)
- [ ] 2. knihovny pro relátka - každá **samostatná** knihovna bude obsahovat _**komparaci parametrů**_
- [ ] 3. knihovna pro cumsum - musí zjišťovat, zda se hodnoty rovnají -> v opačném případě se vrovede úkon 
- [ ] 4. implementace regulace osvětlení

### HMI ROZHRANÍ + UART
- [ ] 1. zajištění komunikace přes UART
- [ ] 2. vytahat data + zobrazit budíky
- [ ] 3. databáze
- [ ] 4. regulace

## Reference
1. [Climate Chamber System](https://projecthub.arduino.cc/ms_peach/climate-chamber-system-c545de).
2. [Learning AVR-C Episode 7: PWM](https://www.youtube.com/watch?v=ZhIRRyhfhLM&list=PLA6BB228B08B03EDD&index=7).
3. [Learning AVR-C Episode 8: Analog Input](https://www.youtube.com/watch?v=51QJ_WHN7u0&list=PLA6BB228B08B03EDD&index=8&fbclid=IwY2xjawGghWBleHRuA2FlbQIxMAABHVy7dx15Emsi53adUYbmtC7HX_bKwPgDDZE106S3zNYXwdnrUu0nhW8zyA_aem_Rj_25ybcyhsOJBNBMxLZ1Q).
