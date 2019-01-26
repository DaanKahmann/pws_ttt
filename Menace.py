import random




class Menace:

    def doe_zet(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        kans = random.randrange(len(zetten))
        print(self.opbouwen(bord))
        return zetten[kans - 1]

    def opbouwen(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        stapel = []

        for zet in zetten:  #geeft een list met wat de mogelijke zetten in zijn in de toestand van het huidige bord
            stapel.append(zet)
        return stapel
