import random


class Menace:


    def doe_zet(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        kans = random.randrange(len(zetten))
        return zetten[kans - 1]


    def opbouwen(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        stapel = []
        for zet in zetten:          #ik wou voor elk "iets" dat in de list zetten zit moet het een zet bij de stapel doen maar dit klopt niet
            stapel.append(zet)

        return stapel



