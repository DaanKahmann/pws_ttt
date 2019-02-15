from collections import Counter

from fastUI import FastUI
from personPlayer import Human
from randomPlayer import RandomPlayer
from Board import Board
from Menace import Menace, Lucifer
from graphical import Graphical


def ttt():
    print("Welkom bij ons geweldige spel, veel plezier!")
    bord = Board()
    winnaars = []
    #gui = Graphical()
    gui = FastUI()

    player1 = Menace()
    #player1 = RandomPlayer()
    #player1 = Human(gui)

    player2 = Menace()
    #player2 = Human(gui)
    #player2 = RandomPlayer()

    gui.tick()
    gui.render(bord)
    gui.initiate_csv()

    i = 0

    while i < 30000:
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
            bord = Board()
            if len(winnaars) % 100 == 0 and len(winnaars) > 0:
                #gui.add_csv(winnaars)      #haal de '#' weg als je de data wil opslaan
                print("Totaal: ", Counter(winnaars), "Laatste 100: ", Counter(winnaars[-101:-1]))

            if len(winnaars) == 30000:
                gui = Graphical()
                player2 = Human(gui)

            i = i + 1

ttt()