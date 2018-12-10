import random

class playerRandom:

    def __init__(self, bord, invoer_pos, x):
        tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        valid_input = False
        while not valid_input:
            if invoer_pos in tuple_getallen and bord[int(invoer_pos) - 1] in range(1, 10):
                valid_input = True
                invoer_pos = int(invoer_pos) - 1
                if x % 2 == 0:
                    bord[invoer_pos] = "X"  # voer 'X' in op gekozen plek
                else:
                    bord[invoer_pos] = "O"
            else:
                invoer_pos = str(random.randrange(1,10))