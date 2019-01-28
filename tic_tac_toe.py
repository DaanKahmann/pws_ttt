from collections import Counter

import randomPlayer
from Board import Board
from Menace import Menace
from graphical import Graphical


def ttt():
    print("Welkom bij ons geweldige spel, veel plezier!")
    bord = Board()
    winnaars = [];
    player1 = Menace()
    player2 = Menace()
    gui = Graphical()
    gui.tick()
    gui.render(bord)
    while True:
        if bord.speler() == 1:
            zet = player1.doe_zet(bord)
        else:
            zet = player2.doe_zet(bord)

        bord = bord.make_move(zet)
        gui.tick()
        gui.render(bord)
        if bord.winner():
            gui.add_score(bord.winner())
            winnaars.append(bord.winner())
            #print(bord.winner())
            bord = Board()
            if len(winnaars) % 100 == 0 and len(winnaars) > 0:
                print(Counter(winnaars))
                #print(Counter(winnaars[-100]))

ttt()