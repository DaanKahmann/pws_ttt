import random

class tic_tac_toe:
    def __init__(self):
        # bord_grootte = int(input("Hoe groot moet het bord zijn? "))
        print("Welkom bij ons geweldige spel, veel plezier!")
        self.spel()  # roep spel aan

    def spel(self):
        bord = list(range(1, 10))  # Maak het bord
        tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        x = self.wie_begint()
        print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord zien

        for i in range(9):
            if x % 2 == 0:  # even getallen: 'X'
                #self.spelerX(tuple_getallen,bord)
                self.spelerRobot2(tuple_getallen, bord)
                beurtX = True
            else:  # oneven getallen 'O'
                #self.spelerO(tuple_getallen, bord)
                self.spelerRobot(tuple_getallen, bord)
                beurtX = False
            print("\n", bord[:3], "\n", bord[3:6], "\n", bord[6:])  # laat bord met wijziging zien
            if self.winnaar(beurtX, bord):
                break
            x = x + 1

    def spelerX(self, tuple_getallen, bord):
        valid_input = False
        invoer_posx = input("positie X: ")
        while not valid_input:
            if invoer_posx in tuple_getallen and bord[int(invoer_posx) - 1] in range(1, 10):
                valid_input = True
                invoer_posx = int(invoer_posx) - 1
                bord[invoer_posx] = "X"  # voer 'X' in op gekozen plek
            else:
                invoer_posx = input("positie X: ")

    def spelerO(self, tuple_getallen, bord):
        valid_input = False
        invoer_poso = input("positie O: ")
        while not valid_input:
            if invoer_poso in tuple_getallen and bord[int(invoer_poso) - 1] in range(1, 10):
                valid_input = True
                invoer_poso = int(invoer_poso) - 1
                bord[invoer_poso] = "O"  # voer 'O' in op gekozen plek
            else:
                invoer_poso = input("positie O: ")

    def spelerRobot(self, tuple_getallen, bord):
        valid_input = False
        invoer_posR = str(random.randrange(1, 10))
        while not valid_input:
            if invoer_posR in tuple_getallen and bord[int(invoer_posR) - 1] in range(1, 10):
                valid_input = True
                invoer_posR = int(invoer_posR) - 1
                bord[invoer_posR] = "O"  # voer 'O' in op gekozen plek
            else:
                invoer_posR = str(random.randrange(1, 10))

    def spelerRobot2(self, tuple_getallen, bord):
        valid_input = False
        invoer_posR = str(random.randrange(1, 10))
        while not valid_input:
            if invoer_posR in tuple_getallen and bord[int(invoer_posR) - 1] in range(1, 10):
                valid_input = True
                invoer_posR = int(invoer_posR) - 1
                bord[invoer_posR] = "X"  # voer 'O' in op gekozen plek
            else:
                invoer_posR = str(random.randrange(1, 10))

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

tic_tac_toe()