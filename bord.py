import speler
import spelerRandom
import random
import graphical

class regels:

    def __init__(self, spelTegen, x):
        self.data = []
        self.countList = []
        self.ui = graphical.Graphical() # gebruik deze regel voor de PyGame UI
        # self.ui = None # gebruik deze regel voor de oude UI
        for a in range(70):
            bord = list(range(1, 10))  # Maak het bord
            regels.spel(self, spelTegen, x, bord, self.ui)
            #print(self.data)
            self.countList = [self.data.count("X"), self.data.count("O"), self.data.count("Tie")]
            print("De stand is (X, O, gelijk): ", self.countList)

    def spel(self, spelTegen, x, bord, ui=None):
        if ui is None:
            print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord zien
        else:
            ui.tick()
            ui.render(bord)
        for i in range(9):
            if x % 2 == 0:  # even getallen: 'X'
                if spelTegen in ("2", "3"):
                    invoer_pos = str(random.randrange(1, 10))
                    spelerRandom.playerRandom(bord, invoer_pos, x)
                else:
                    #invoer_pos = input("positie X: ")
                    speler.playermens(bord, x)
                beurtX = True

            else:  # oneven getallen 'O'
                if spelTegen in ("1", "3"):
                    invoer_pos = str(random.randrange(1,10))
                    spelerRandom.playerRandom(bord, invoer_pos, x)
                else:
                    #invoer_pos = input("positie O: ")
                    speler.playermens(bord, x)
                beurtX = False

            if ui is None:
                print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord met wijziging zien
            else:
                ui.tick()
                ui.render(bord)

            if regels.winnaar(self, beurtX, bord):
                break
            elif i == 8:
                self.data.append("Tie")
                self.ui.add_score(2)
                print("It's a Tie")
                break
            x = x + 1


    def tegen_wie(self):
        validInput = False
        spelTegen = input("Tegen wie wil je spelen? kies uit: 1) O random 2) X random 3) allebei random 4) allebei speler ")
        while not validInput:
            if spelTegen in ("1", "2", "3", "4"):
                validInput = True
            else:
                spelTegen = input("Tegen wie wil je spelen? kies uit: 1) O random 2) X random 3) allebei random 4) allebei speler ")

        return spelTegen

    def wie_begint(self):
        input_valid = False
        while not input_valid:
            beginner = input("Wie moet beginnen? ")
            if beginner in "Xx":  # zorgt voor wie begint
                x = 0  # 'X' begint
                input_valid = True
            elif beginner in "Oo":
                x = 1  # 'O' begint
                input_valid = True
        return x

    def winnaar(self, beurtX, bord):

        if bord[0] == bord[1] == bord[2] or bord[3] == bord[4] == bord[5] or bord[6] == bord[7] == bord[8] \
                or bord[2] == bord[4] == bord[6] or bord[0] == bord[4] == bord[8] or bord[0] == bord[3] == bord[6] \
                or bord[1] == bord[4] == bord[7] or bord[2] == bord[5] == bord[8]:
            if beurtX:
                print("X heeft gewonnen")
                self.data.append("X")
                self.ui.add_score(1)

            else:
                print("O heeft gewonnen")
                self.data.append("O")
                self.ui.add_score(0)
            return True