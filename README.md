# rail_lib
Simulátor návěstidla pro české železnice / Railway signal simulator for Czech railways. <br>
Tento soubor obsahuje kompletní dokumentaci knihovny. Tato knihovna umožňuje ovládat LED svítilny přes GPIO rozhraní Raspberry Pi podle návěstních předpisů SŽDC D1. Balík se skládá z několika Python souborů:
<br>Soubor rail_lib.py je samotná knihovna, která sama o sobě nic nedělá, pouze definuje funkce, které lze použít v jiných programech. Dokumentace a seznam těchto funkcí je níže. Nyní jsou v balíku přítomny další dva programy, manual.py umožňuje ruční ovládání LED svítilen pomocí funkcí definovaných v knihovně rail_lib.py, test.py po zadání názvů portů vyzkouší rozsvícením na 5s všechny diody.
<br><br>
Pro přidání knihovny do vlastního projektu importujte soubor rail_lib.py do Python programu:

```python
from rail_lib import *
```

## Instalace a závislosti

Knihovna rail_library používá gpiozero. Pokud není předinstalováno, lze nainstalovat pomocí pip:

```bash
sudo pip install gpiozero
```

Připojte LED diody k GPIO rozhraní a poznamenejte si názvy GPIO portů (ne čísla portů 1-40), ale názvy (tj. GPIOxx). Naklonujte si tento balík:

```bash
git clone https://github.com/ddaqua6/rail_lib
```

Přejděte do složky rail_lib:

```bash
cd rail_lib
```

Knihovna je nainstalovaná.

## Funkce definované v knihovně a jejich popis

on(led,speed) - ruční zapnutí svítilny led (ve formátu gpiozero), speed - rychlost blikání: 0 - nebliká, 1 - pomalé blikání, 2 - rychlé blikání (rychlost odpovídá návěstnímu  předpisu)<br><br>
off(led) - ruční vypnutí svítilny led<br><br>
konfigurovat() - spustí manuální konfiguraci svítilen (GPIO pinů), vepisujte názvy pinů, na kterém je daná svítilna připojena<br><br>
konfigurovat_auto(y1,g,r,w,y2,b) - konfigurace svítilen a pinů pomocí argumentů funkce (pro automatizované použití), uvádějte názvy pinů: např. konfigurovat_auto(21, 17, 8, 27, 22, 5). Pořadí svítilen: žlutá horní, zelená, červená, bílá, žlutá spodní, modrá (pro posun). Pokud má návěstidlo jen jedno žluté světlo, uvádějte ho vždy jako žluté horní. Pokud danou LED svítilnou návěstidlo nedisponujte, uveďte místo čísla "null"<br><br>
zmena() - zhasne všechny nakonfigurované svítilny<br><br>
zhasnout_vse() - zhasne všechny nakonfigurované svítilny<br><br>
nejedu() - systémová funkce, pokud se program pokusí zobrazit návěst, kterou nelze zobrazit (např. návěsti pro posun na návěstidle autobloku), program vypíše chybu a barvu, která mu chybí, aby návěst mohl zobrazit a pokusí se zobrazit návěst Stůj<br><br>
help() - zobrazí zkrácený přehled funkcí<br><br>
spodni() - spustí spodní žluté světlo; funkce pro účely systému<br><br>

### Funkce zobrazující návěsti

volno() - Volno<br>
stuj() - Stůj!<br>
vystraha() - Výstraha<br>
posun_dovolen() - Posun dovolen<br>
posun_zakazan() - Posun zakázán<br>
ocekavej(rychlost) - Očekávej 40/60/80/100 km/h. Příklad použití: ocekavej(40)<br>
rychlost40(rychlost) - Rychlost 40 km/h a výstraha/volno nebo očekávej 40/60/80/100 km/h. Příklady použití: rychlost40(volno), rychlost40(60)<br>
jizda_vlaku_dovolena() - Jízda vlaku dovolena<br>
privolavaci() - Přivolávací návěst<br>
privolavaci_jen_bile() - PN jen s bílým světlem (bez Stůj)<br>
jizda_dle_rozhl_pomeru() - Jízda podle rozhledových poměrů
