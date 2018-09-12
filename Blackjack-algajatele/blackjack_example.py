"""Valmis kood koos märkmetega, millal miski koolitusel teemaks võiks tulla."""
import random

"""
Antud kood võtab tublimate algajatega umbes tunni ja veerand (koos lisadega).
Kui ambitsiooni on rohkem (ja järelejäänud aega üle poole tunni),võib realiseerida lisaks 
järgnevaid siit puuduvaid asju:
    1. Teha leaderboard tekstifailina ja muuta "uue mängu" while-tsükkel hoopis mängu menüüks.
    2. Lisada igale prinditavale tagasisidesõnele mängija nimi ja anda see argumendina blackjack()-i kaasa.
    3. Siluda koodi ja vaadata, mis printimisi saaks eraldi funktsioonideks teha.
    4. Teha järjend numbritest, mis on sõnades välja kirjutatud ja kasutada neid printimisel.
"""

def blackjack():
    """
    Ühe mängu jagu koodi.

    Funktsioon tuleks luua pärast ühe mängu tegemise realiseerimist ja sellega seletada
    funktsiooni vajalikkust koodi taaskasutusel. Lisaks kirjutamise nipid: valida
    mitu rida koodi ja vajutada Tab, et tekiks mitmele reale taane.
    """

    # Luua päris alguses, kui seletada lahti muutujanime-muutujaväärtuse paari.
    mängija_punktid = 0

    # Alul võib olla 0, randint() realiseerida siis, kui vaja arvuti skoori võrrelda mängija omaga.
    arvutipunktid = random.randint(0, 21)

    # Realiseerida pärast ühe kaardivõtu koodi realiseerimist.
    while True:

        suvakas_kaart = random.randint(2, 10)

        # Teha alguses mängija_punktide muutuja testimiseks.
        print("Sul on " + str(mängija_punktid) + " punkti.")

        # Lisada pärast punktide muutujate loomist ja enne kaardivõtu sisendi valideerimist.
        sisend = input("Kas soovid võtta uue kaardi? Vastasel juhul mäng lõppeb. (Y/N)")

        # Kaardivõtu sisendi valideerimine. Seletada lahti if-lause ja ta omadused.
        if sisend == "Y":
            print("Võtsid uue kaardi!")

            # Realiseerida pärast kaardivõtu sisendi valideerimist koos suvaka_kaardi loomisega.
            mängija_punktid = mängija_punktid + suvakas_kaart

        elif sisend == "N":
            print("Olgu. Mäng läbi!")

            # Lisada koos while-tsükliga, mis ülal kirjas.
            break

        else:
            print("Ei saanud aru.")

        # Lisaülesanne, et inimesed saaksid nuputada.
        if mängija_punktid > 21:
            break

    # Mängu lõpptulemuse kuva. Realiseerida pärast while-tsüklit, tutvustada sõne vormimist f-stringide või
    # %-vormimise kaudu.
    if mängija_punktid > 21:
        print("Sul on %d punkti." % mängija_punktid)
        print("See on kaugelt üle 21-he! Oled kaotanud.")
    elif mängija_punktid > arvutipunktid:
        print("Sa oled võitnud!")
        print("Sul oli %d punkti, arvutil vaid %d." % (mängija_punktid, arvutipunktid))
    elif mängija_punktid == arvutipunktid:
        print("Mängisid viiki!")
        print("Sul oli %d punkti, arvutil ka %d." % (mängija_punktid, arvutipunktid))
    else:
        print("Kaotasid!")
        print("Sul oli %d punkti, arvutil aga %d." % (mängija_punktid, arvutipunktid))


# Teha kõige alguses, et seletada konsooliga suhtlust.
kasutaja_nimi = input("Mis su nimi on?")
print("Tere, " + kasutaja_nimi + ", mängime blackjacki!")

# Kutsu esimene mäng välja. Seletada, miks väljakutse peab olema definitsiooni all. Teha meelega
# NameError: name 'blackjack' is not defined, et näitlikustada selgitust.
blackjack()

# Kui aega üle jääb. Eelnev kood võtab tublide algajatega umbes tunni, järgnev võib võtta umbes 15min.
# Lisab mängule lõpliku viimistluse.
while True:
    sisend = input("Uus mäng?(Y/N)")

    if sisend == "Y":
        blackjack()
        continue
    elif sisend == "N":
        print("Aitäh mängimast!")
        break
    else:
        print("Ei saanud aru.")
#Sissejuhatus
#============

#Tere ja tutvustused
#Kus asuvad jutumärgid, ümarsulud, kantsulud, suurem-kui-väiksem-kui märgid, alakriips, plussmärk, koolon, koma?
#Lapikud
#Pythoni koolitus
#Lihtne blackjacki mäng
#Mängureeglid

#On kaardipakk ja nii arvuti kui ka mängija võtavad kordamööda sealt kaarte.
#Mängija saab igal võtmisel valida, kas ta võtab kaarte juurde või lõpetab mängu.
#Mängu lõppemisel võidab mängija siis, kui kaartide summa on väiksem kui 21 ja
#suurem kui arvutil.

#Tere, mängija!

print("Tere, mängija, mängime blackjacki!")

#Kasutajasisendiga mängijanimi

kasutajanimi = input("Ütle, mis su nimi on!")

print("Tere, " + kasutajanimi + ", mängime blackjacki!")

#Kaardisumma muutujate loomine

kasutaja_punktid = 0
arvuti_punktid = 0

#Kaardisumma väljaprintimine

print("Sul on " + str(kasutaja_punktid) + " punkti.")

#Kaardivõtmine

sisend = input("Soovid kaarid võtta? Kui mitte, siis mäng lõppeb. (Y/N)")

#Sisendi testimine

if sisend == "Y":
	print("Võtsid uue kaardi.")
elif sisend == "N":
	print("Mäng läbi!")
else:
	print("Ei saanud nüüd täpselt aru.")

#Suvaka kaardi võtmine ja summale lisamine

import random

suvakas_kaart = random.randint(2, 10)

if sisend == "Y":
	print("Võtsid kaardi ja said " + str(suvakas_kaart) + " punkti juurde.")
	kasutaja_punktid = kasutaja_punktid + suvakas_kaart
	print("Sinu punktisumma on nüüd " + str(kasutaja_punktid) + " punkti.") #jne..

#While-loop ümber ja break

#Arvuti punktid

arvutipunktid = random.randint(2, 10)

#Mängu kokkuvõte
if kasutaja_punktid > 21:
	print("Läksid lõhki ja kaotasid!")
	print("Sul oli " + str(kasutaja_punktid) + " punkti. See on küll üle kahekümne ühe.")
elif kasutaja_punktid < arvuti_punktid:
	print("Arvuti mängis su üle!")
	print("Sul oli " + str(kasutaja_punktid) + " punkti, arvutil aga" + str(arvutipunktid) + " punkti.")
else:
	print("Sa võitsid!")

#Uus mäng?
while True:
    sisend = input("Uus mäng?(Y/N)")

    if sisend == "Y":
        blackjack()
        continue
    elif sisend == "N":
        print("Aitäh mängimast!")
        break
    else:
        print("Ei saanud aru.")
