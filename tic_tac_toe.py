import randomPlayer
from Board import Board
from graphical import Graphical


def ttt():
    print("Welkom bij ons geweldige spel, veel plezier!")

    player1 = randomPlayer.RandomPlayer()
    player2 = randomPlayer.RandomPlayer()
    bord = Board()
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
            print(bord.winner())
            bord = Board()

ttt()