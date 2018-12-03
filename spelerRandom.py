import random



class spelerrandom:
    def spelerRobot(self, bord):
        tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        valid_input = False
        invoer_posR = str(random.randrange(1, 10))
        while not valid_input:
            if invoer_posR in tuple_getallen and bord[int(invoer_posR) - 1] in range(1, 10):
                valid_input = True
                invoer_posR = int(invoer_posR) - 1
                bord[invoer_posR] = "O"  # voer 'O' in op gekozen plek
            else:
                invoer_posR = str(random.randrange(1, 10))

    def spelerRobot2(self, bord):
        tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        valid_input = False
        invoer_posR = str(random.randrange(1, 10))
        while not valid_input:
            if invoer_posR in tuple_getallen and bord[int(invoer_posR) - 1] in range(1, 10):
                valid_input = True
                invoer_posR = int(invoer_posR) - 1
                bord[invoer_posR] = "X"  # voer 'O' in op gekozen plek
            else:
                invoer_posR = str(random.randrange(1, 10))
