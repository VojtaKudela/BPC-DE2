# Tropical plants :palm_tree::potted_plant::cactus:
Členové týmu

1. Vít Janoš (zodpovědný za PWM)
2. Vojtěch Kudela (zodpovědný za správu GitHub a knihoven)
3. Jakub Kupčík (zodpovědný za získání dat)
4. Antonín Putala (zodpovědný za GUI a UART)

## Teoretický popis a vysvětlení


## Hardwarový popis


### Náhled na zařízení
![Pohled na zařízení](https://github.com/VojtaKudela/BPC-DE1-topic_4/blob/main/Picture/1713725654572.jpg).


## Sofwarový popis


## Simulace komponentů 


## Instrukční návod


### Popis částí


### Popis ovládacích prvků


### Nastavení 

### Video ukázka
Pro ukázku obsluhy zařízení a jeho činnosti za chodu ve formě videa klikněte [zde](https://youtu.be/y9z3xt5LS8A).

## Bloky
### ZÍSKÁNÍ DAT
- [x] 1. adc-zajistit získání hodnoty z _fotorezistoru_ a _soil čidla_ (knihovna)
- [x] 2. převést na _**SMYSLUPLNOU HODNOTU**_
- [x] 3. zajistit získání dat z _teplotního čidla_
- [x] 4. zajisti _získání dat z RTC_
- [x] 5. časování odečtu
   
### REGULACE VELIČIN
- [x] 1. PWM-rozjet (např. na 1 LED)
- [x] 2. knihovny pro relátka - každá **samostatná** knihovna bude obsahovat _**komparaci parametrů**_
- [x] 3. knihovna pro cumsum - musí zjišťovat, zda se hodnoty rovnají -> v opačném případě se provede úkon 
- [x] 4. implementace regulace osvětlení

### GUI ROZHRANÍ + UART
- [x] 1. zajištění komunikace přes UART
- [x] 2. vytahat data + zobrazit budíky
- [x] 3. databáze
- [x] 4. regulace

### KOMPLEMENTACE
- [x] 1. komplementace zařízení
- [x] 2. video
- [x] 3. schéma zapojení
- [ ] 4. dokumentace - popis algoritmů pomocí vývojových diagramů

## Dokumentace
1. [PC rozhraní](https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/Python/html/index.html)
2. [AVR - firmware](https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/AVR-C/html/index.html)
3. Podrobnější informace k projektu naleznete v [dokumentaci](https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/AVR-C/html/index.html)

## Video

## Použité nástroje
1. [VS Code](https://code.visualstudio.com/)
1. [ChatGPT](https://chatgpt.com/)
2. [Microsoft Copilot](https://copilot.microsoft.com/)
3. [SimulIDE](https://simulide.com/p/)
4. [Saleae Logic 2](https://www.saleae.com/pages/downloads)
5. [Online C compiler](https://www.online-cpp.com/online_c_compiler)
6. [Bandicam](https://www.bandicam.com/cz/)
7. [draw.io](https://app.diagrams.net/)
8. [Doxygen](https://doxygen.nl/index.html)
9. [Matlab](https://www.mathworks.com/products/matlab.html)
10. [ProfiCAD - Elektro CAD Software - ProfiCAD](https://www.proficad.cz/)

## Reference
1. [Climate Chamber System](https://projecthub.arduino.cc/ms_peach/climate-chamber-system-c545de).
2. [Learning AVR-C Episode 7: PWM](https://www.youtube.com/watch?v=ZhIRRyhfhLM&list=PLA6BB228B08B03EDD&index=7).
3. [Learning AVR-C Episode 8: Analog Input](https://www.youtube.com/watch?v=51QJ_WHN7u0&list=PLA6BB228B08B03EDD&index=8&fbclid=IwY2xjawGghWBleHRuA2FlbQIxMAABHVy7dx15Emsi53adUYbmtC7HX_bKwPgDDZE106S3zNYXwdnrUu0nhW8zyA_aem_Rj_25ybcyhsOJBNBMxLZ1Q).
4. [Custom Tkinter - Official Documentation](https://customtkinter.tomschimansky.com/)
5. [pySerial's documentation](https://pyserial.readthedocs.io/en/latest/)
6. [ASCII table](https://www.ascii-code.com/)
7. [ATMEGA328P- datasheet](https://www.microchip.com/en-us/product/ATmega328p)
8. [Soil moisure](https://www.makerguides.com/capacitive-soil-moisture-sensor-with-arduino/)
9. [Arduino map()](https://reference.arduino.cc/reference/en/language/functions/math/map/)
10. [Co potřebují rostliny k životu - Jaké jsou podmínky pro jejich život | Zjišťujeme.cz](https://www.zjistujeme.cz/co-potrebuji-rostliny-k-zivotu-jake-jsou-podminky-pro-jejich-zivot/#:~:text=Co%20pot%C5%99ebuj%C3%AD%20rostliny%20k%20%C5%BEivotu%20%E2%80%93%20Jak%C3%A9%20jsou,slune%C4%8Dn%C3%ADho%20sv%C4%9Btla.%20...%204%20Prostor%20a%20%C4%8Das%20)
11. [Podnebné (klimatické) pásy - Počasí](http://aaapocasi.cz/podnebne-klimaticke-pasy/)
12. [Your Gateway to Embedded Software Development Excellence · PlatformIO](https://platformio.org/?utm_source=platformio&utm_medium=piohome)
13. [DS3213 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/DS3231.pdf)
14. [Soil Moisture Sensor - Comple Guide | Arduino Project Hub](https://projecthub.arduino.cc/lucasfernando/soil-moisture-sensor-comple-guide-b9c82b)
15. [DHT12 temperature sensor and Arduino example - Arduino Learning](https://www.arduinolearning.com/code/dht12-temperature-sensor-arduino-example.php)
16. [Arduino - Home](https://www.arduino.cc/)
17. [CP2102 datasheet(1/18 Pages) SILABS | SINGLE-CHIP USB TO UART BRIDGE](https://www.alldatasheet.com/html-pdf/201067/SILABS/CP2102/215/1/CP2102.html)
18. [18.	CP210x USB to UART Bridge VCP Drivers - Silicon Labs](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)
19. [Peter Fleury Online: AVR Software](http://www.peterfleury.epizy.com/avr-software.html?i=1)
20. [AVR course – UART · tomas-fryza/avr-course](https://github.com/tomas-fryza/avr-course/tree/master/lab5-uart)
21. [AVR course – I2C    · tomas-fryza/avr-course](https://github.com/tomas-fryza/avr-course/tree/master/lab6-i2c)


