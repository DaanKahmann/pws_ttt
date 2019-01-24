import random


class RandomPlayer:

    def doe_zet(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        return random.choice(zetten)