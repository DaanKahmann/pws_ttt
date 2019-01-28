import random
from numpy.random import choice

from Board import Board


class Menace:

    def __init__(self):
        self.zet_gedaan = []
        self.ld_gedaan = []
        self.stapel = self.opbouwen()

    def doe_zet(self, bord):
        beurt = self.stapel[bord.ronde()]
        for luciferdoosje in beurt:
            if luciferdoosje.bord == bord:
                zet = luciferdoosje.geef_zet()
                self.zet_gedaan.append(zet)
                self.ld_gedaan.append(luciferdoosje)
                zet = bord.translate(luciferdoosje.bord, zet)
                if zet is None:
                    print(luciferdoosje)
                else:
                    return zet
        print("geen ld gevonden \n" + str(bord))

    def opbouwen(self):
        stapel = [[Lucifer(Board())]]
        for n in range(1,9):
            mogelijkheden = set()
            for luciferdoosje in stapel[n - 1]:
                for zet in luciferdoosje.zetten:
                    mogelijkheden.add(luciferdoosje.bord.make_move(zet, minimal=True))

            beurt = []
            for bord in mogelijkheden:
                beurt.append(Lucifer(bord))
            stapel.append(beurt)
        return stapel

    def uitkomst(self, winnaar):
        for zet, luciferdoosje  in zip(self.zet_gedaan, self.ld_gedaan):
            luciferdoosje.uitkomst(zet, winnaar)
        self.zet_gedaan = []
        self.ld_gedaan = []

class Lucifer:
    #staat van een spel
    #kraaltje / opties: mogelijke zetten met kans
    def __init__(self, bord):
        self.bord = bord
        self.zetten = bord.mogelijkheden(uniek=True)
        self.kans = [7] * len(self.zetten)

    def geef_zet(self):
        totaal_kraaltjes = sum(self.kans)
        random_getal = random.randint(1, totaal_kraaltjes)
        for zet, kans in zip(self.zetten, self.kans):
            random_getal -= kans
            if random_getal <= 0:
                return zet

    def uitkomst(self, zet, winnaar):
        index = self.zetten.index(zet)
        if winnaar == 3:
            #bij gelijkspel doen we nu niks
            return
        elif self.bord.speler() == winnaar:
            #bij winst doe iets
            self.kans[index] += 3
            return
        else:
            #haal wat eraf
            if self.kans[index] > 0 and sum(self.kans) > 2: #deze waarden moeten aangepast worden als dat in de if aangepast wordt
                self.kans[index] -= 1
            return