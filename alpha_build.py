
import bord


def tic_tac_toe(self=None):
    # bord_grootte = int(input("Hoe groot moet het bord zijn? "))
    print("Welkom bij ons geweldige spel, veel plezier!")
    spelTegen = bord.regels.tegen_wie(self)

    x = bord.regels.wie_begint(self)

    bord.regels(spelTegen, x)


tic_tac_toe()