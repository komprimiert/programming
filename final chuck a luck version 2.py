from random import randint

class Spielzahl(object):
    def __init__(self):
        self.spielzahl = None

    def setzen(self,wert):
        self.spielzahl = wert

class Wuerfel(object):
    def __init__(self):
        self.augen = randint(1,6)
    def werfen(self):
        self.augen = randint(1,6)

class Konto(object):
    def __init__(self):
        self.stand = 100

    def einzahlen(self,betrag):
        self.stand += betrag

    def auszahlen(self,betrag):
        self.stand -= betrag

class chuckaluck(object):
    def __init__(self):
        self.k = Konto()
        self.s = Spielzahl()
        self.wA = Wuerfel()
        self.wB = Wuerfel()
        self.wC = Wuerfel()

    def einsatzZahlen(self,einsatz):
        if self.k.stand<=0:
            print("Konto leer")
            return 1
        else:
            if self.k.stand-einsatz < 0:
                print("zu großer Einsatz gesetzt")
                return 2
            else:
                self.k.auszahlen(einsatz)
                self.einsatz = einsatz
                return 3

    def spielzahlSetzen(self,zahl):
        self.s.setzen(zahl)

    def wuerfelWerfen(self):
        self.wA.werfen()
        self.wB.werfen()
        self.wC.werfen()
        print(self.wA.augen)
        print(self.wB.augen)
        print(self.wC.augen)
        
    def überprüfen(self):
        anzahlTreffer=0
        if self.wA.augen == self.s.spielzahl:
            anzahlTreffer += 1
            print(anzahlTreffer)
        if self.wB.augen == self.s.spielzahl:
            anzahlTreffer += 1
            print(anzahlTreffer)
        if self.wC.augen == self.s.spielzahl:
            anzahlTreffer += 1
            print(anzahlTreffer)
    
    #def einsatz(self):
        #x=self.einsatzZahlen(int(self.einsatzEntry.get()))
        
    #def zahl(self):
        #global
        #self.spielzahlSetzen(self.spielzahl.get())

    #def werfen(self):
        #if self.hilfzaehler<=10:
            #self.hilfzaehler+=1
            #self.wuerfelWerfen()
        #else:
            #self.hilfzaehler=0

    def gewinn(self):
        self.gewinnAuszahlen()

    #def geldEinzahlen(self):
        #passwort=input("Passwort eingeben: ")
        #if passwort==str(self.k.stand):
            #geld=int(input("Wie viel Geld soll eingezahlt werden?"))
        #else:
            #geld=0
        #self.k.einzahlen(geld)

