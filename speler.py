class playermens:

    def spelerX(self, bord):
        tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        valid_input = False
        invoer_posx = input("positie X: ")
        while not valid_input:
            if invoer_posx in tuple_getallen and bord[int(invoer_posx) - 1] in range(1, 10):
                valid_input = True
                invoer_posx = int(invoer_posx) - 1
                bord[invoer_posx] = "X"  # voer 'X' in op gekozen plek
            else:
                invoer_posx = input("positie X: ")

    def spelerO(self, bord):
        tuple_getallen = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        valid_input = False
        invoer_poso = input("positie O: ")
        while not valid_input:
            if invoer_poso in tuple_getallen and bord[int(invoer_poso) - 1] in range(1, 10):
                valid_input = True
                invoer_poso = int(invoer_poso) - 1
                bord[invoer_poso] = "O"  # voer 'O' in op gekozen plek
            else:
                invoer_poso = input("positie O: ")

