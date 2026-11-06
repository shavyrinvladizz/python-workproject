######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Vladislav Shavyrin
# Opiskelijanumero: 003425394
# Päivämäärä:01.11.2026
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla: W3Schools, InterviewBit, Claude, Gemini Notebook.  Näiden lähteiden avullla tuli saatu ymmärrystä miksi koodi ei toimi, sekä oppinut lisää teemaasta. Lähteet eivät kirjoittaneet minulle valmiiksi olevan koodin, vaan ohjanneet lisäkysymyksien avulla tekemään koodin itse.
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py

import HTPerusKirjasto

def valikko():
    print("1) Lue tiedosto")
    print("2) Analysoi ")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi CO2-päästöt")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    Ajoneuvot = []
    ViikkoTulokset = []
    PaastoKategoriat = []
    Valinta = -1
    while (Valinta != 0):
        Valinta = valikko()
        if (Valinta == 1):
            Nimi = HTPerusKirjasto.kysyTiedostonNimi("Anna luettavan tiedoston nimi: ")
            HTPerusKirjasto.lueTiedosto(Nimi, Ajoneuvot)
            print()
        elif (Valinta == 2):
            if (len(Ajoneuvot) > 0):
                HTPerusKirjasto.analysoiViikot(Ajoneuvot, ViikkoTulokset)
                print()
            else:
                print("Lue tiedosto ennen analysointia.")
                print()
        elif (Valinta == 3):
            if (len(ViikkoTulokset) > 0):
                Nimi = HTPerusKirjasto.kysyTiedostonNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.kirjoitaViikot(Nimi, ViikkoTulokset)
                print()
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallenusta.")
                print()
        elif (Valinta == 4):
            if (len(Ajoneuvot) > 0):
                HTPerusKirjasto.analysoiPaastot(Ajoneuvot, PaastoKategoriat)
                Nimi = HTPerusKirjasto.kysyTiedostonNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.kirjoitaPaastot(Nimi, PaastoKategoriat)
                print()
            else:
                print("Lue tiedosto ennen analysointia.")
                print()
    else:
        print("Tuntematon valinta, yritä uudestaan.")
    print("Lopetetaan.")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

