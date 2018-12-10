import speler
import spelerRandom


class regels:

    def spel(self, spelTegen, x):
        scoreX = [0, 0, 0]  # gewonnen, verloren, gelijk
        scoreO = [0, 0, 0]

        winx = 0
        verliesx = 0

        wino = 0
        verlieso = 0

        gelijk = 0

        bord = list(range(1, 10))  # Maak het bord
        #x = regels.wie_begint(self)

        #spelTegen = regels.tegen_wie(self)          #haalt variabele spelTegen uit de functie tegen_wie,
                                                    #moet voor zorgen dat functie niet wordt aangeroepen in spel
        print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord zien

        for i in range(9):
            if x % 2 == 0:  # even getallen: 'X'
                if spelTegen in ("2", "3"):
                    spelerRandom.spelerrandom.spelerRobot2(self, bord)
                else:
                    speler.playermens.spelerX(self, bord)
                beurtX = True

            else:  # oneven getallen 'O'
                if spelTegen in ("1", "3"):
                    spelerRandom.spelerrandom.spelerRobot(self, bord)
                else:
                    speler.playermens.spelerO(self, bord)
                beurtX = False

            print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord met wijziging zien

            if regels.winnaar(self, beurtX, bord):
                if beurtX:
                    winx = winx + 1
                    scoreX[0] = winx
                    verlieso = verlieso + 1
                    scoreO[1] = verlieso

                else:
                    wino = wino + 1
                    scoreO[0] = wino
                    verliesx = verliesx + 1
                    scoreX[1] = verliesx
                print('stand van X:', scoreX)
                print('stand van O:', scoreO)

                break
            elif i == 8:
                print("It's a Tie")
                gelijk = gelijk + 1
                scoreX[2] = gelijk
                scoreO[2] = gelijk
                print('stand van X:', scoreX)
                print('stand van O:', scoreO)
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

            else:
                print("O heeft gewonnen")
            return True


class stand:

    def score(self):
        scoreX = [0, 0, 0]  # gewonnen, verloren, gelijk
        scoreO = [0, 0, 0]

        winx = 0
        verliesx = 0

        wino = 0
        verlieso = 0

        gelijk = 0

    def scorewinX(self, winx, scoreX, verlieso, scoreO):
        winx = winx + 1
        scoreX[0] = winx
        verlieso = verlieso + 1
        scoreO[1] = verlieso

    def scorewinO(self, wino, scoreO, verliesx, scoreX):
        wino = wino + 1
        scoreO[0] = wino
        verliesx = verliesx + 1
        scoreX[1] = verliesx

    def gelijkscore(self,gelijk, scoreX, scoreO):
        gelijk = gelijk + 1
        scoreX[2] = gelijk
        scoreO[2] = gelijk





