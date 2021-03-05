from gpiozero import *
from time import sleep
from signal import pause

def on(led,speed):
	if speed == 0:
		led.on()
	if speed == 1:
		led.blink(0.55, 0.55) #pomale blikani
	if speed == 2:
		led.blink(0.27, 0.27) #rychle blikani
def off(led):
	led.off() 
#definice promennych
null = "null"
vystraha = "vystraha"
volno = "volno"
pahrbek = "pahrbek"
X = "X"
trojkolejny = "trojkolejny"
dvoukolejny = "dvoukolejny"
jednokolejny = "jednokolejny"
zkracena_vzdalenost = "zkracena_vzdalenost"
Z = "Z"
zpet = "Z"
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
def vari():
	global seznam
	global zluta_up
        global zelena
        global cervena
        global bila
        global zluta_dn
        global modra
	global disp_a
	global disp_b
	global disp_c
	global disp_d
	global disp_e
	global disp_f
	global disp_g
	global disp_h
	seznam = []
	zluta_up = "null"
	zelena = "null"
	cervena = "null"
	bila = "null"
	zluta_dn = "null"
	modra = "null"
	disp_a = "null"
	disp_b = "null"
	disp_c = "null"
	disp_d = "null"
	disp_e = "null"
	disp_f = "null"
	disp_g = "null"
	disp_h = "null"
vari()
def konfigurovat(): #funkce pro rucni konfiguraci
	#definice promennych
	global seznam
	global zluta_up
	global zelena
	global cervena
	global bila
	global zluta_dn
	global modra
	vari()
	#dialog
	print("\nNastavte GPIO piny na kterych jsou pripojeny svitilny.")
	print("Pokud svitilna neni pripojena, napiste null nebo nepiste nic (odenterujte).\n")
	zluta_up = raw_input("Zluta horni: ")
	zelena = raw_input("Zelena: ")
	cervena = raw_input("Cervena: ")
	bila = raw_input("Bila: ")
	zluta_dn = raw_input("Zluta spodni: ")
	modra = raw_input("Modra (pro posun): ")
	if zluta_up == "": #kontrola validity vstupu
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
	if zluta_up != "null": #nahrani konfigurace LED do promenne
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
	help() #vypsat seznam funkci
	stuj("startmanual") #pocatecni navest Stuj
def konfigurovat_auto(y1="null", g="null", r="null", w="null", y2="null", b="null"): #konfigurace LED pres argumenty funkce
	global zluta_up #definice promennych
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
	stuj("startauto") #pocatecni poloha Stuj
def zmena(): #vypnout vsechny nakonfigurovane LED
	for i in seznam:
		i.off()
def zhasnout_vse(): #viz zmena()
	zmena()
def nejedu(nav="LED"): #neni nastavena potrebna LED
	stuj("err")
	print("Neni nastavena svitilna potrebna pro tuto navest: " + nav)
	return "nejedu"
def help(): #vypsat seznam funkci
	print("Podporovane prikazy:")
	print("help(), konfigurovat(), zhasnout_vse(), opakovani(); volno(), stuj(), vystraha(), posun_zakazan(), posun_dovolen(), ocekavej(40/60/80/100), rychlost40(volno/vystraha/40/60/80/100), jizda_vlaku_dovolena(), privolavaci(), privolavaci_jen_bile(), jizda_dle_rozhl_pomeru(), odj_nav_dovoluje_jizdu(), jednokolejny/dvoukolejny/trojkolejny_provoz(), na_svazny_pahrbek_postaveno(), posun_zpet(), neplatne_navestidlo(), na_kratkou_vzdalenost()")
	print("Do funkce ocekavej(rychlost) vepiste rychlost. Do funkce rychlost40(volno/vystraha/40/60/80/100) vepiste navest horni casti. Funkci opakovani() pro aktivaci navesti na nedost. zabrzdnou vzdalenost pouzijte az po aktivaci opakovane navesti.\n")
	print("Pro konfiguraci indikatoru pouzijte konfigurovat_indikator(a, b, c,... g, True/False, podle navodu na strankach rail_lib.")
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

def spodni(): #spustit spodni zlutou LED
	if zluta_dn != "null":
		zluta_dn.on()
	else:
		nejedu("Zluta spodni")
def ocekavej(rychlost):
	zmena()
	if rychlost == 40 or rychlost == 30 or rychlost == 50:
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
		stuj("err")
		print("Neocekavana rychlost. Pouzijte ocekavej(40/60/80/100), napr. ocekavej(40)")
def rychlost40(): #obsolete
	print("Tato funkce jiz neni podporovana. Pouzijte funkci rychlost(aktualni, ocekavej).")
def rychlost(ted, rychlost): #rychlost nejaka a vystraha/volno ocekavej..
	zmena()
	spodni()
	if ted == 10:
		indikator(1)
	elif ted == 20:
		indikator(2)
	elif ted == 30:
		indikator(3)
	elif ted == 40:
		pass
	elif ted == 50:
		indikator(5)
	elif ted == 60:
		indikator(6)
	elif ted == 70:
		indikator(7)
	elif ted == 80:
		indikator(8)
	elif ted == 90:
		indikator(9)
	else:
		stuj("err")
		print("Neocekavany vstup. Pouzijte rychlost(aktualni,ocekavej), napr. rychlost(40,60)")
	if rychlost == 40 or rychlost == 30 or rychlost == 50:
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
		stuj("err")
               	print("Neocekavany vstup. Pouzijte rychlost(aktualni, vystraha/volno/40/60/80/100), napr. rychlost(40,40) = Rychlost 40 a ocekavej 40.")
def jizda_vlaku_dovolena():
	zmena()
	if modra != "null":
		on(modra,1)
	else:
		nejedu("Modra")
def privolavaci(): #PN
	stuj()
	if bila != "null":
		on(bila,1)
	else:
		nejedu("Bila")
def privolavaci_jen_bile(): #PN bez Stuj - jen bile kmitave svetlo
	zmena()
	if bila != "null":
		on(bila, 1)
	else:
		nejedu("Bila")
def jizda_dle_rozhl_pomeru(): # Jizda dle rozhledovych pomeru
	vystraha()
	if bila != "null":
		on(bila, 1)
	else:
		nejedu("Bila")
def odj_nav_dovoluje_jizdu(): # Odjezdove navestidlo dovoluje jizdu - navest na vlozenem navestidle
	privolavaci_jen_bile()
def posun_zpet():
	zmena()
	if bila != "null":
		bila.on()
	else:
		nejedu("Bila")
	indikator(Z)
def neplatne_navestidlo():
	zmena()
	indikator(X)
def na_svazny_pahrbek_postaveno():
	zmena()
	if bila != "null":
		bila.on()
	else:
		nejedu("Bila")
	indikator(pahrbek)
def jednokolejny_provoz():
	indikator(jednokolejny)
def dvoukolejny_provoz():
	indikator(dvoukolejny)
def trojkolejny_provoz():
	indikator(trojkolejny)
def na_kratkou_vzdalenost():
	indikator(zkracena_vzdalenost)
def opakovani(): # Pridat k existujici navesti opakovani
	if bila != "null":
		bila.on()
	else:
		nejedu("Bila")
#upozorneni pri startu
print("\n POZOR! LED svitilny vzdy zapojujte tak, aby byl z jednoho pinu odebiran proud max 16 mA, celkove max 50 mA soucasne. Autor aplikace neruci za poskozeni zpusobene pouzivanim tohoto programu.")

# indikator

def konfigurovat_indikator(a="null", b="null", c="null", d="null", e="null", f="null", g="null", ak=False, h="null"):
	global disp_a
        global disp_b
        global disp_c
        global disp_d
        global disp_e
        global disp_f
        global disp_g
        global disp_h
	if a != "null":
                disp_a = LED(int(a), active_high=ak)
		seznam.append(disp_a)
	if b != "null":
                disp_b = LED(int(b), active_high=ak)
                seznam.append(disp_b)
	if c != "null":
                disp_c = LED(int(c), active_high=ak)
                seznam.append(disp_c)
	if d != "null":
                disp_d = LED(int(d), active_high=ak)
                seznam.append(disp_d)
	if e != "null":
                disp_e = LED(int(e), active_high=ak)
                seznam.append(disp_e)
	if f != "null":
                disp_f = LED(int(f), active_high=ak)
                seznam.append(disp_f)
	if g != "null":
                disp_g = LED(int(g), active_high=ak)
                seznam.append(disp_g)
	if h != "null":
		disp_h = LED(int(h), active_high=ak)
		seznam.append(disp_h)
def indikator(char, change="null"):
	if change != "null":
		zmena()
	if char == 1:
		if disp_b != "null" and disp_c != "null":
			disp_b.on()
			disp_c.on()
		else:
			nejedu("Indikator, pole B a C")
	elif char == 2 or char == Z:
		if disp_a != "null" and disp_b != "null" and disp_g != "null" and disp_e != "null" and disp_d != "null":
			disp_a.on()
			disp_b.on()
			disp_g.on()
			disp_e.on()
			disp_d.on()
		else:
			nejedu("Indikator, pole A, B, D, E a G")
	elif char == 3:
		if disp_a != "null" and disp_b != "null" and disp_g != "null" and disp_c != "null" and disp_d != "null":
			disp_a.on()
			disp_b.on()
			disp_c.on()
			disp_d.on()
			disp_g.on()
		else:
			nejedu("Indikator, pole A-D a G")
	elif char == 4:
		if disp_f != "null" and disp_g != "null" and disp_b != "null" and disp_c != "null":
			disp_f.on()
			disp_g.on()
			disp_b.on()
			disp_c.on()
		else:
			nejedu("Indikator, pole B, C, F a G")
	elif char == 5:
		if disp_a != "null" and disp_f != "null" and disp_g != "null" and disp_c != "null" and disp_d != "null":
			disp_a.on()
			disp_f.on()
			disp_g.on()
			disp_c.on()
			disp_d.on()
		else:
			nejedu("Indikator, pole A, C, D, F a G")
	elif char == 6:
		if disp_a != "null" and disp_f != "null" and disp_g != "null" and disp_e != "null" and disp_d != "null" and disp_c != "null":
			disp_a.on()
			disp_f.on()
			disp_g.on()
			disp_e.on()
			disp_d.on()
			disp_c.on()
		else:
			nejedu("Indikator, pole A, C-G")
	elif char == 7:
		if disp_a != "null" and disp_b != "null" and disp_c != "null":
			disp_a.on()
			disp_b.on()
			disp_c.on()
		else:
			nejedu("Indikator, pole A-C")
	elif char == 8:
		if disp_a != "null" and disp_b != "null" and disp_c != "null" and disp_d != "null" and disp_e != "null" and disp_f != "null" and disp_g != "null":
			disp_a.on()
			disp_b.on()
			disp_c.on()
			disp_d.on()
			disp_e.on()
			disp_f.on()
			disp_g.on()
	elif char == 9:
		if disp_a != "null" and disp_b != "null" and disp_f != "null" and disp_g != "null" and disp_c != "null" and disp_d != "null":
			disp_a.on()
			disp_f.on()
			disp_g.on()
			disp_b.on()
			disp_c.on()
			disp_d.on()
		else:
			nejedu("Indikator, pole A-D, F-G")
	elif char == "pahrbek":
		if disp_e != "null" and disp_f != "null" and disp_a != "null" and disp_b != "null" and disp_c != "null":
			disp_e.on()
			disp_f.on()
			disp_a.on()
			disp_b.on()
			disp_c.on()
		else:
			nejedu("Indikator, pole A-C, E-F")
	elif char == "X":
		if disp_f != "null" and disp_g != "null" and disp_b != "null" and disp_e != "null" and disp_c != "null":
			disp_f.on()
			disp_g.on()
			disp_b.on()
			disp_c.on()
			disp_e.on()
		else:
			nejedu("Indikator, pole B, C, E-G")
	elif char == "trojkolejny":
		if disp_a != "null" and disp_g != "null" and disp_d != "null":
			disp_a.on()
			disp_g.on()
			disp_d.on()
	elif char == "dvoukolejny":
		if disp_a != "null" and disp_d != "null":
			disp_a.on()
			disp_d.on()
		else:
			nejedu("Indikator, pole A a D")
	elif char == "jednokolejny":
		if disp_g != "null":
			disp_g.on()
		else:
			nejedu("Indikator, pole G")
	elif char == "zkracena_vzdalenost":
		if disp_f != "null"  and disp_b != "null":
			disp_f.on()
			disp_b.on()
		else:
			nejedu("Indikator, pole B, C, E a F")
	elif char == "a":
		if disp_a != "null":
			disp_a.on()
	elif char == "b":
		if disp_b != "null":
			disp_b.on()
	elif char == "c":
		if disp_c != "null":
			disp_c.on()
	elif char == "d":
		if disp_d != "null":
			disp_d.on()
	elif char == "e":
		if disp_e != "null":
			disp_e.on()
	elif char == "f":
		if disp_f != "null":
			disp_f.on()
	elif char == "g":
		if disp_g != "null":
			disp_g.on()
	elif char == "h":
		if disp_h != "null":
			disp_h.on()
	elif char == 0:
		if disp_a != "null" and disp_b != "null" and disp_c != "null" and disp_d != "null" and disp_e != "null" and disp_f != "null":
			disp_a.on()
			disp_b.on()
			disp_c.on()
			disp_d.on()
			disp_e.on()
			disp_f.on()
		else:
			nejedu("Indikator, pole A-F")
	else:
		print("Neocekavany znak na indikatoru")
def display(char):
	indikator(char)
def disoff():
	disp_a.off()
        disp_b.off()
        disp_c.off()
        disp_d.off()
        disp_e.off()
        disp_f.off()
	disp_g.off()
	disp_h.off()
