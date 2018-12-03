import speler
import spelerRandom

class regels:
    def spel(self):
        bord = list(range(1, 10))  # Maak het bord
        x = regels.wie_begint(self)
        print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord zien

        for i in range(9):
            if x % 2 == 0:  # even getallen: 'X'
                speler.playermens.spelerX(self, bord)
                #spelerRandom.spelerrandom.spelerRobot2(self, bord)
                beurtX = True
            else:  # oneven getallen 'O'
                speler.playermens.spelerO(self, bord)
                #spelerRandom.spelerrandom.spelerRobot(self, bord)
                beurtX = False
            print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord met wijziging zien
            if regels.winnaar(self, beurtX, bord):
                break
            x = x + 1



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



