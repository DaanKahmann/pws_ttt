from collections import Counter

from personPlayer import Human
from randomPlayer import RandomPlayer
from Board import Board
from Menace import Menace
from graphical import Graphical
import csv


def ttt():
    print("Welkom bij ons geweldige spel, veel plezier!")
    bord = Board()
    winnaars = []
    gui = Graphical()
    player1 = Menace()
    player2 = Human(gui)
    #player2 = RandomPlayer()
    gui.tick()
    gui.render(bord)

    with open('test.csv', mode='a') as myfile:
        fieldnames = [1, 2, 3]
        mywriter = csv.DictWriter(myfile, fieldnames=fieldnames)
        mywriter.writeheader()

    i = 0

    while i < 1000:
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
                export(winnaars)
                print("Totaal: ", Counter(winnaars), "Laatste 100: ", Counter(winnaars[-100:-1]))
                #print(Counter(winnaars[-100:-1]))
            i = i + 1

def export(winnaars):
    with open('test.csv', mode='a') as myfile:
        fieldnames = [1, 2, 3]
        mywriter = csv.DictWriter(myfile, fieldnames=fieldnames)
        mywriter.writerow(Counter(winnaars[-101:-1]))

ttt()