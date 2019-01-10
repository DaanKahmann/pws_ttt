import random
import Board

def randomPlayer():
    return random.sample(Board._rotations[0][0], 1)