from gpiozero import *
from time import sleep
def on(led,speed):
	if speed == 0:
		led.on()
	if speed == 1:
		led.blink(0.55, 0.55)
	if speed == 2:
		led.blink(0.27, 0.27)
def off(led):
	led.off()
null = "null"
vystraha = "vystraha"
volno = "volno"
seznam = []
zluta_up = "null"
zelena = "null"
cervena = "null"
bila = "null"
zluta_dn = "null"
modra = "null"
def konfigurovat():
	global zluta_up
	global zelena
	global cervena
	global bila
	global zluta_dn
	global modra
	print("\nNastavte GPIO piny na kterych jsou pripojeny svitilny.")
	print("Pokud svitilna neni pripojena, napiste null nebo nepiste nic (odenterujte).\n")
	zluta_up = raw_input("Zluta horni: ")
	zelena = raw_input("Zelena: ")
	cervena = raw_input("Cervena: ")
	bila = raw_input("Bila: ")
	zluta_dn = raw_input("Zluta spodni: ")
	modra = raw_input("Modra (pro posun): ")
	print("Podpora indikatoru bude pridana pozdeji.")
	if zluta_up == "":
		zluta_up = null
	if zelena == "":
		zelena = null
	if cervena == "":
		cervena = null
	if bila == "":
		bila = null
	if zluta_dn == "":
		zluta_dn = null
	if modra == "":
		modra = null
	if zluta_up != "null":
		zluta_up = LED(int(zluta_up))
		seznam.append(zluta_up)
	if zelena != "null":
	        zelena = LED(int(zelena))
		seznam.append(zelena)
	if cervena != "null":
        	cervena = LED(int(cervena))
		seznam.append(cervena)
	if bila != "null":
	        bila = LED(int(bila))
		seznam.append(bila)
	if zluta_dn != "null":
	        zluta_dn = LED(int(zluta_dn))
		seznam.append(zluta_dn)
	if modra != "null":
	        modra = LED(int(modra))
		seznam.append(modra)
	print("")
	help()
def konfigurovat_auto(y1="null", g="null", r="null", w="null", y2="null", b="null"):
	global zluta_up
        global zelena
        global cervena
        global bila
        global zluta_dn
        global modra
	if y1 != "null":
                zluta_up = LED(int(y1))
                seznam.append(zluta_up)
        if g != "null":
                zelena = LED(int(g))
                seznam.append(zelena)
        if r != "null":
                cervena = LED(int(r))
                seznam.append(cervena)
        if w != "null":
                bila = LED(int(w))
                seznam.append(bila)
        if y2 != "null":
                zluta_dn = LED(int(y2))
                seznam.append(zluta_dn)
        if b != "null":
                modra = LED(int(b))
                seznam.append(modra)
def zmena():
	for i in seznam:
		i.off()
def zhasnout_vse():
	zmena()
def nejedu(nav=""):
	stuj("err")
	print("Neni nastavena svitilna potrebna pro tuto navest: " + nav)
def help():
	print("Podporovane prikazy:")
	print("help(), konfigurovat(), zhasnout_vse(); volno(), stuj(), vystraha(), posun_zakazan(), posun_dovolen(), ocekavej(40/60/80/100), rychlost40(volno/vystraha/40/60/80/100), jizda_vlaku_dovolena(), privolavaci(), privolavaci_jen_bile(), jizda_dle_rozhl_pomeru()")
	print("Do funkce ocekavej(rychlost) vepiste rychlost. Do funkce rychlost40(volno/vystraha/40/60/80/100) vepiste navest horni casti.\n")
def volno(change="ano"):
	if change != "null":
		zmena()
	if zelena != "null":
		zelena.on()
	else:
		nejedu("Zelena")
def stuj(error="null"):
		zmena()
		if cervena != "null":
			cervena.on()
		elif error == "null":
			nejedu("Cervena")
def posun_zakazan():
	zmena()
	if modra != "null":
		modra.on()
	else:
		nejedu("Modra")
def vystraha(change="ano"):
	if change != "null":
		zmena()
	if zluta_up != "null":
		zluta_up.on()
	else:
		nejedu("Zluta horni")
def posun_dovolen():
	zmena()
	if bila != "null":
		bila.on()
	else:
		nejedu("Bila")

def spodni():
	if zluta_dn != "null":
		zluta_dn.on()
	else:
		nejedu("Zluta spodni")
def ocekavej(rychlost):
	zmena()
	if rychlost == 40:
		if zluta_up != "null":
			on(zluta_up,1)
		else:
			nejedu("Zluta horni")
	elif rychlost == 60:
		if zluta_up != "null":
			on(zluta_up,2)
		else:
			nejedu("Zluta horni")
	elif rychlost == 80:
		if zelena != "null":
			on(zelena,1)
		else:
			nejedu("Zelena")
	elif rychlost == 100:
		if zelena != "null":
			on(zelena,2)
		else:
			nejedu("Zelena")
	else:
		print("Neocekavana rychlost. Pouzijte ocekavej(40/60/80/100), napr. ocekavej(40)")
def rychlost40(rychlost):
	zmena()
	spodni()
	if rychlost == 40:
               	if zluta_up != "null":
               	        on(zluta_up,1)
               	else:
               	        nejedu("Zluta horni")
       	elif rychlost == 60:
               	if zluta_up != "null":
                       	on(zluta_up,2)
      		else:
                       	nejedu("Zluta horni")
	elif rychlost == 80:
               	if zelena != "null":
                       	on(zelena,1)
               	else:
                       	nejedu("Zelena")
  	elif rychlost == 100:
               	if zelena != "null":
                       	on(zelena,2)
   		else:
                       	nejedu("Zelena")
       	elif rychlost == vystraha:
		vystraha(null)
	elif rychlost == volno:
		volno(null)
	else:
               	print("Neocekavany vstup. Pouzijte rychlost(vystraha/volno/40/60/80/100), napr. rychlost40(40) = Rychlost 40 a ocekavej 40.")
def jizda_vlaku_dovolena():
	zmena()
	if modra != "null":
		on(modra,1)
	else:
		nejedu("Modra")
def privolavaci():
	stuj()
	if bila != "null":
		on(bila,1)
	else:
		nejedu("Bila")
def privolavaci_jen_bile():
	zmena()
	if bila != "null":
		on(bila, 1)
	else:
		nejedu("Bila")
def jizda_dle_rozhl_pomeru():
	vystraha()
	if bila != "null":
		on(bila, 1)
	else:
		nejedu("Bila")
print("\n POZOR! LED svitilny vzdy zapojujte tak, aby byl z jednoho pinu odebiran proud max 16 mA, celkove max 50 mA soucasne. Autor aplikace a knihovny neruci za poskozeni zpusobene (nespravnym) pouzivanim tohoto programu.")
