import random

class playerRandom:

    def __init__(self, bord, x):
        self.tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.valid_input = False
        self.invoer_pos = str(random.randrange(1, 10))
        playerRandom.zet(self, bord, x)

    def zet(self, bord, x):
        while not self.valid_input:
            if self.invoer_pos in self.tuple_getallen and bord[int(self.invoer_pos) - 1] in range(1, 10):
                self.valid_input = True
                self.invoer_pos = int(self.invoer_pos) - 1
                if x % 2 == 0:
                    bord[self.invoer_pos] = "X"  # voer 'X' in op gekozen plek
                else:
                    bord[self.invoer_pos] = "O"
            else:
                self.invoer_pos = str(random.randrange(1, 10))