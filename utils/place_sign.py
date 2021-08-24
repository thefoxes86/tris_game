from utils.check_empty import check_empty
from utils.check_victory import check_victory


def place_sign(table, pos, player):
    if player == 1:
        symbol = "0"
    else:
        symbol = "X"
        
    if pos == "1":
        if check_empty(table[0, 0]):
            table[0, 0] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "2":
        if check_empty(table[0, 1]):
            table[0, 1] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "3":
        if check_empty(table[0, 2]):
            table[0, 2] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "4":
        if check_empty(table[1, 0]):
            table[1, 0] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "5":
        if check_empty(table[1, 1]):
            table[1, 1] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "6":
        if check_empty(table[1, 2]):
            table[1, 2] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "7":
        if check_empty(table[2, 0]):
            table[2, 0] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "8":
        if check_empty(table[2, 1]):
            table[2, 1] = symbol
            return check_victory(table)
        else:
            return False
    elif pos == "9":
        if check_empty(table[2, 2]):
            table[2, 2] = symbol
            return check_victory(table)
        else:
            return False
    else:
        return table
