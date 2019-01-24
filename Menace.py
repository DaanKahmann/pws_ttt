import random


class Menace:


    def doe_zet(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        kans = random.randrange(len(zetten))
        return zetten[kans - 1]


    def opbouwen(self, bord, zetten):
        stapel = []
