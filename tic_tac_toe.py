from collections import Counter

from randomPlayer import RandomPlayer
from Board import Board
from Menace import Menace
from graphical import Graphical


def ttt():
    print("Welkom bij ons geweldige spel, veel plezier!")
    bord = Board()
    winnaars = []
    player1 = Menace()
    player2 = Menace()
    #player2 = RandomPlayer()
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
            player1.uitkomst(bord.winner())
            player2.uitkomst(bord.winner())
            gui.add_score(bord.winner())
            winnaars.append(bord.winner())
            #print(bord.winner())
            bord = Board()
            if len(winnaars) % 100 == 0 and len(winnaars) > 0:
                print("Totaal: ", Counter(winnaars), "Laatste 100: ", Counter(winnaars[-100:-1]))
                #print(Counter(winnaars[-100:-1]))

ttt()