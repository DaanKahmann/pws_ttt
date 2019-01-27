import random




class Menace:

    def doe_zet(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        kans = random.randrange(len(zetten))
        een_zet = zetten[kans-1]
        gedaan_player1 = []
        gedaan_player2 = []
        #print(self.opbouwen(bord))
        if bord.speler() == 1:              #zetten worden in een list gezet maar na elke beurt gereset doordat de functie opnieuw wordt aangeroepen
            gedaan_player1.append(een_zet)
            print('speler 1: ', gedaan_player1)
        else:
            gedaan_player2.append(een_zet)
            print('speler 2: ', gedaan_player2)
        return een_zet

    def opbouwen(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        stapel = []
        for zet in zetten:  #geeft een list met wat de mogelijke zetten in zijn in de toestand van het huidige bord
            stapel.append(zet)
        return stapel

