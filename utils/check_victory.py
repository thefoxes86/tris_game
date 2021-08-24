def check_victory(table):
    # INIZIO CONTROLLO GIOCATORE 1
    # Controllo prima riga orizzontale Giocatore 1
    if table[0, 0] == '0' and table[0, 1] == '0' and table[0, 2] == '0':
        return 1
    # Controllo seconda riga orizzontale Giocatore 1
    elif table[1, 0] == '0' and table[1, 1] == '0' and table[1, 2] == '0':
        return 1
    # Controllo terza riga orizzontale Giocatore 1
    elif table[2, 0] == '0' and table[2, 1] == '0' and table[2, 2] == '0':
        return 1
    # Controllo prima colonna verticale Giocatore 1
    elif table[0, 0] == '0' and table[1, 0] == '0' and table[2, 0] == '0':
        return 1
    # Controllo seconda colonna verticale Giocatore 1
    elif table[0, 1] == '0' and table[1, 1] == '0' and table[2, 1] == '0':
        return 1
    # Controllo terza colonna verticale Giocatore 1
    elif table[0, 2] == '0' and table[1, 2] == '0' and table[2, 2] == '0':
        return 1
    # Controllo prima diagonale Giocatore 1
    elif table[0, 0] == '0' and table[1, 1] == '0' and table[2, 2] == '0':
        return 1
    # Controllo seconda diagonale Giocatore 1
    elif table[0, 2] == '0' and table[1, 1] == '0' and table[2, 0] == '0':
        return 1
    # INIZIO CONTROLLO GIOCATORE 2
    # Controllo prima riga orizzontale Giocatore 2
    if table[0, 0] == 'X' and table[0, 1] == 'X' and table[0, 2] == 'X':
        return 2
    # Controllo seconda riga orizzontale Giocatore 2
    elif table[1, 0] == 'X' and table[1, 1] == 'X' and table[1, 2] == 'X':
        return 2
    # Controllo terza riga orizzontale Giocatore 2
    elif table[2, 0] == 'X' and table[2, 1] == 'X' and table[2, 2] == 'X':
        return 2
    # Controllo prima colonna verticale Giocatore 2
    elif table[0, 0] == 'X' and table[1, 0] == 'X' and table[2, 0] == 'X':
        return 2
    # Controllo seconda colonna verticale Giocatore 2
    elif table[0, 1] == 'X' and table[1, 1] == 'X' and table[2, 1] == 'X':
        return 2
    # Controllo terza colonna verticale Giocatore 2
    elif table[0, 2] == 'X' and table[1, 2] == 'X' and table[2, 2] == 'X':
        return 2
    # Controllo prima diagonale Giocatore 2
    elif table[0, 0] == 'X' and table[1, 1] == 'X' and table[2, 2] == 'X':
        return 2
    # Controllo seconda diagonale Giocatore 2
    elif table[0, 2] == 'X' and table[1, 1] == 'X' and table[2, 0] == 'X':
        return 2
    else:
        pass
