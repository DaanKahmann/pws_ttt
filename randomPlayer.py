import random


class RandomPlayer:

    def doezet(self, bord):
        zetten = bord.mogelijkheden(uniek=True)
        return random.choice(zetten)