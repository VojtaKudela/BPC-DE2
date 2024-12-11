# Tropical plants :palm_tree::potted_plant::cactus:
Členové týmu

1. Vít Janoš (zodpovědný za PWM)
2. Vojtěch Kudela (zodpovědný za obsluhu a správu GitHub)
3. Jakub Kupčík (zodpovědný za získání dat)
4. Antonín Putala (zodpovědný za GUI a UART)

## Teoretický popis a vysvětlení
V době prudkého nárůstu světové populace jsou hledány způsoby, jak zvýšit světovou produkci potravin. Jednou z možností, která se nabízí je pěstování ve **sklenících**. Velkou výhodou skleníků je, že potravinová produkce v nich není vázána na vegetační cyklus ani na klimatické podmínky. Podmínky uvnitř skleníku je možné udržovat systémem senzorů a akčních členů, které zajistí **optimální klima** pro zde pěstované rostliny.

Jak známo rostliny ke svému životu potřebují:
1.	vodu a živiny
2.	vzduch a půdu
3.	světlo a teplo
4.	prostor a čas

Půdu a živiny je nutné zajistit při setí nebo sadbě. Vzduch bude zajištěn přístupem čerstvého vzduchu. Požadavek na prostor je omezující, co se týče rostlin, které jsme schopni na ploše vysadit a čas bohužel regulovat nelze, je tedy nezbytné nechat rostlinu růst do doby, než ponese plody.

Naopak je možné regulovat **teplotu** okolí, **světlo** a vodu, která se projeví jako **půdní vlhkost**. Tento projekt se zaměřuje na pěstování **tropických rostlin**. Je potřeba myslet na to, že tropické rostliny rostou ve velmi vlhkém prostředí, proto je nutné regulovat také **vlhkost vzduchu**.

Pro otestování možností bylo realizováno zařízení schopné, jak **měřit**, tak i **regulovat** zvolené veličiny v skleníku. Tyto veličiny je pochopitelně nutné v čase měnit, aby pokud možno odrážely, denní cykly a co nejlépe odrážely klima, ve kterém rostlina přirozeně roste. Protože jako pěstitel nemáme možnost neustále sledovat vývoj veličin, naměřené **hodnoty veličin** je vhodné **ukládat** pro další zpracování. Aby byla obsluha zařízení uživatelsky přívětivá, bylo zvoleno **ovládání prostřednictvím osobního počítače**, kčemuž slouží grafické uživatelské rozhraní (GUI). 


## Hardwarový popis

Zařízení představuje prototyp měřicího a řídicího členu pro tropický skleník. Umožňuje měření teploty, osvětlení, půdní vlhkosti a vlhkosti vzduchu. Tyto hodnoty jsou odečítány v reálném čase. Odečítání hodnot veličin zajišťují tyto senzory:

1.	[DHT12](https://www.arduinolearning.com/code/dht12-temperature-sensor-arduino-example.php) – kombinované teplotní a vlhkostní čidlo
2.	[Kapacitní senzor půdní vlhkosti v1.2](https://projecthub.arduino.cc/lucasfernando/soil-moisture-sensor-comple-guide-b9c82b) – Arduino
3.	fotorezistor
   
Aby odečítané hodnoty byly v reálném čase, byly použity hodiny reálného času RTC [DS3213](https://www.analog.com/media/en/technical-documentation/data-sheets/DS3231.pdf). 
Další funkcí je regulace těchto veličin. K tomu slouží výstupní periférie. V tom to případě byl uvažován **topný člen**, **ventilátor**, **nebulizér**, **ventil** pro ovládání hadice, která bude zajišťovat závlahu a LED pásek, který bude představovat **osvětlení**. Regulaci teploty zajišťuje topný člen a ventilátor a regulaci vlhkosti vzduchu zajišťuje nebulizér a ventilátor.Pro otestování funkce byly tyto periferie nahrazeny různobarevný **LED** diodami.


### Schéma + foto testovacího zařízení
![Pohled na zařízení](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Picture/IMG_20241204_180939.jpg)


### Schéma zapojení
![Schéma zapojení](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Picture/Schema.png)


## Periferie
V rámci projektu bylo uvažováno a použito kombinované teplotní a vlhkostní čidlo, hodiny reálného času, čidlo osvětlení, čidlo půdní vlhkosti, 
tepelný člen, ventilátor, nebulizér, ventil a LED pásek. Podrobnější popis jednotlivých periferií naleznete v [dokumentaci](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Documentation-final.pdf).

## Sofwarový popis
Pro funkci zařízení bylo nezbytné vytvořit jak program pro mikrokontroler, tak pro osobní počítač. Zatímco program pro mikrokontroler byl napsán v jazyce C, program pro osobní počítač byl napsán v Pythonu.


### Python
Úkolem programu pro osobní počítač je sbírat data vysílaná zařízením a vysílat instrukce k regulaci měřených veličin. Aplikace též umožňuje změnit čas zařízení a graficky zobrazit změřené hodnoty. Samotnou aplikaci spustí soubor [Tropical_plants](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/Tropical_plants.py). Tento program vytvoří aplikaci [GUI_main](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/GUI_main.py) a spustí ji. Podrobný popis všech použitých tříd a funkcí se nachází v této [dokumentaci] pro Python (https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/Python/html/index.html) nebo v [dokumentaci](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Documentation-final.pdf) k projektu.


### Náhled na zařízení s řídícím osobním počítačem v pozadí
![Pohled na zařízení s uživatelským rozhraním](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Picture/IMG_20241204_181146_1.jpg)


## Sériová komunikace
Veškerá sériová komunikace probíhá na rychlost **9600 Bd**. Je využíván sériový port počítače **COM3**. Aby se ušetřil datový tok, jsou zasílány přímo číselné hodnoty, nikoli jejich zápis v ASCII kódu. Osobní počítač vysílá dva různé datové balíčky; první nese informaci o **nastavení času**, druhý o **nastavení** regulovaných b. Mikrokontroler vysílá pouze jeden balíček.


### Zpracování přijatých dat z mikrokontroleru
Přijatá data ze sériového portu je nutné uložit, zpracovat a uložit do rozhraní, a poté jejich aplikovat aktualizaci, aby se změny projevily v hlavním okně. 
Třída [raw_data](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/raw_data.py) složí jako úložný prostor pro přijatá data. Jednotlivé byty jsou uloženy v listu. Tato třída je následně zpracována třídou [data_file](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/data_file.py). Zde dochází k převodu dat na smysluplnou zobrazitelnou hodnotu. Tato data jsou ukládána do textového souboru database.txt, který slouží jako úložiště naměřených hodnot pro pozdější zpracování. Pro grafické zpracování je nutné data z textového souboru načíst. To zajišťuje třída [database](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/database.py). 
Při zpracovávání dat je nutné převádět názvy dnů v týdnu na číselné hodnoty a zpětně, stejně jako názvy měsíců na číselné hodnoty. Převod názvů dnů zajišťuje knihovna [num_and_days](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/num_and_days.py), převod názvů měsíců na číslo funkce [month2num](https://github.com/VojtaKudela/BPC-DE2/blob/main/Python_GUI/month2num.py).
Podrobnější informace naleznete v [dokumentaci](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Documentation-final.pdf).


## Knihovny
Firmware mikrokontroleru využívá několik knihoven. Knihovna [uart](https://github.com/VojtaKudela/BPC-DE2/tree/main/Project-02-03/lib/uart) byla převzata z [19](http://www.peterfleury.epizy.com/avr-software.html?i=2). Použitá verze byla převzata z [20](https://github.com/tomas-fryza/avr-course/tree/master/lab5-uart). Knihovna [twi](https://github.com/VojtaKudela/BPC-DE2/tree/main/Project-02-03/lib/twi) byla převzata z [21](https://github.com/tomas-fryza/avr-course/tree/master/lab6-i2c). Ani jedna z nich nebyla upravována. Ostatní knihovny byly vytvořeny spolu s projektem. Ty naleznete v [dokumentaci](https://github.com/VojtaKudela/BPC-DE2/blob/main/Documentation/Documentation-final.pdf).


## Instrukční list

### Zobrazení aktuálně naměřené hodnoty
Naměřené hodnoty jsou přímo zobrazeny v hlavním panelu. Hlavní panel zobrazuje naměřenou hodnotu teploty, vlhkosti vzduch, půdní vlhkosti a osvětlenosti. U všech veličin je jednak zobrazena číselná hodnota a jednak její hodnota na analogové stupnici.
Analogové stupnice mají následující rozsah:
-	Teplota - 15 až 60 °C
-	Vlhkost vzduchu – 0 až 100 %
-	Půdní vlhkost – 0 až 100 %
-	Osvětlení – 1 až 1000 lx

Stupnice osvětlení je logaritmická, ostatní jsou lineární.



### Video ukázka
Pro ukázku obsluhy zařízení a jeho činnosti za chodu ve formě videa klikněte [zde](https://l.facebook.com/l.php?u=https%3A%2F%2Fvutbr-my.sharepoint.com%2F%3Av%3A%2Fg%2Fpersonal%2F246858_vutbr_cz%2FEXO8N39nYi9CjGoCtYOYt_YBu9UJ9zcuZxR2HDn7m6k5Xw%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR0kTXEcqZt7Lsbg1UoCl0ykdBTkBOt3FukuswAQO3Te59IQwOYOxVHeaSI_aem_F0M8OA4p4Sr2LX9bdFgvGQ&h=AT1zTisApxY7p2FXc7chAo3kfdsrvQq1c_8bjErb-S-DH0EZpSUpumy_P4UQ7MJ7msPugB_uP-vv12Eb6qwxfn0DG8LiicpJ44ga-bMsWyaQF_o4rvcu8xNuwXYGrkICevLfGg).


## Dokumentace
- [PC rozhraní](https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/Python/html/index.html)
- [AVR - firmware](https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/AVR-C/html/index.html)
- [Dokumentace k projektu](https://raw.githack.com/VojtaKudela/BPC-DE2/refs/heads/main/Documentation/AVR-C/html/index.html)


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


