######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Vladislav Shavyrin
# Opiskelijanumero: 003425394
# Päivämäärä:01.11.2026
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla: W3Schools, InterviewBit, Claude, Gemini Notebook. Näiden lähteiden avullla tuli saatu ymmärrystä miksi koodi ei toimi, sekä oppinut lisää teemaasta. Lähteet eivät kirjoittaneet minulle valmiiksi olevan koodin, vaan ohjanneet lisäkysymyksien avulla tekemään koodin itse.
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerusKirjasto.py
import time
import sys
EROTIN = ";"

class AJONEUVO:
    Tunniste = None
    Aikaleima = None
    Luokka = None
    Paasto = None

class VIIKKO:
    Viikko = None
    Lkm = None

class KATEGORIA:
    Nimi = None
    Lkm = None

def kysyTiedostonNimi(kehote):
    Nimi = input(kehote)
    while (not Nimi.endswith(".txt")):
        print("Tiedostopääte väärin, vaadittu pääte on .txt")
        Nimi = input(kehote)
    return Nimi

def lueTiedosto(Nimi, Lista):
    Lista.clear()

    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivi = Tiedosto.readline()
        while (len(Rivi)  >0):
            Sarakkeet = Rivi.strip().split(EROTIN)
            Ajoneuvo = AJONEUVO()
            Ajoneuvo.Tunniste = Sarakkeet[0]
            Ajoneuvo.Aikaleima = time.strptime(Sarakkeet[1], "%d.%m.%Y")
            Ajoneuvo.Luokka = Sarakkeet[2]
            Ajoneuvo.Paasto = int(Sarakkeet[3])
            Lista.append(Ajoneuvo)
            Rivi = Tiedosto.readline()
        Tiedosto.close()
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    print("Tiedosto '" + Nimi + "' luettu.")
    print("Tiedostosta lisättiin " + str(len(Lista)) + " datariviä listaan.")
    return Lista

def analysoiViikot(Lista, Tulos):
    Tulos.clear()
    for Ajoneuvo in Lista:
        Viikkonumero = time.strftime("%W", Ajoneuvo.Aikaleima)
        if ((len(Tulos) ==0) or (Tulos [-1].Viikko != Viikkonumero)):
            uusiViikko = VIIKKO()
            uusiViikko.Viikko = Viikkonumero
            uusiViikko.Lkm = 1
            Tulos.append(uusiViikko)
        else:
            Tulos[-1].Lkm = Tulos[-1].Lkm + 1
    print("Viikkottaiset summat laskettu " + str(len(Tulos)) + " viikolle.")
    return Tulos

def kirjoitaViikot(Nimi, Tulos):
    try:
        Tiedosto = open(Nimi, "w", encoding = "UTF-8")
        Tiedosto.write("Ensirekisteröityjen ajoneuvojen määrä viikoittain:\n")
        Tiedosto.write("Viikko;Lkm\n")
        for Alkio in Tulos:
            Rivi = Alkio.Viikko + EROTIN + str(Alkio.Lkm) + "\n"
            Tiedosto.write(Rivi)
        Tiedosto.close()
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None

def analysoiPaastot(Lista, Kategoriat):
    Kategoriat.clear()
    Kat1 = KATEGORIA()
    Kat1.Nimi = "Kategoria 1"
    Kat1.Lkm = 0
    Kat2 = KATEGORIA()
    Kat2.Nimi = "Kategoria 2"
    Kat2.Lkm = 0
    Kat3 = KATEGORIA()
    Kat3.Nimi = "Kategoria 3"
    Kat3.Lkm = 0
    Kat4 = KATEGORIA()
    Kat4.Nimi = "Kategoria 4"
    Kat4.Lkm = 0
    for Ajoneuvo in Lista:
        if (Ajoneuvo.Paasto < 125):
            Kat1.Lkm = Kat1.Lkm + 1
        elif (Ajoneuvo.Paasto < 175):
            Kat2.Lkm = Kat2.Lkm + 1
        elif (Ajoneuvo.Paasto < 225):
            Kat3.Lkm = Kat3.Lkm + 1
        else:
            Kat4.Lkm = Kat4.Lkm + 1
    Kategoriat.append(Kat1)
    Kategoriat.append(Kat2)
    Kategoriat.append(Kat3)
    Kategoriat.append(Kat4)
    print("Ajoneuvot kategorisoitu 4 kategoriaan.")
    return Kategoriat

def kirjoitaPaastot(Nimi, Kategoriat):
    try:
        Tiedosto = open(Nimi, "w", encoding = "UTF-8")
        Tiedosto.write("Ajoneuvojen määrät kategorioittain:\n")
        Tiedosto.write("Kategoria;Ajoneuvojen lukumäärä\n")
        for Alkio in Kategoriat:
            Rivi = Alkio.Nimi + EROTIN + str(Alkio.Lkm) + "\n"
            Tiedosto.write(Rivi)
        Tiedosto.close()
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None
