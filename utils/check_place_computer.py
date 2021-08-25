import numpy as np

from utils.deleting_from_array import deleting_from_array


def check_place_computer(table, possible_move_player, possible_move_computer, last_move_player):
    # Controlla due caselle di fila e chiudi
    last_move_player_num = last_move_player[len(last_move_player) - 1]
    last_move_computer = [0]
    last_move_computer_num = last_move_computer[len(last_move_computer) - 1]
    if not np.any(np.isin(possible_move_player, [1, 2])) and np.any(np.isin(possible_move_computer, [3])):
        table[0, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 3)
        print('chiudo')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)
    elif not np.any(np.isin(possible_move_player, [2, 3])) and np.any(np.isin(possible_move_computer, [1])):
        table[0, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 1)
        print('chiudo')
        deleting_from_array(possible_move_player, 1)
        deleting_from_array(possible_move_computer, 1)
    elif not np.any(np.isin(possible_move_player, [4, 5])) and np.any(np.isin(possible_move_computer, [6])):
        table[1, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 6)
        print('chiudo')
        deleting_from_array(possible_move_player, 8)
        deleting_from_array(possible_move_computer, 8)
    elif not np.any(np.isin(possible_move_player, [5, 6])) and np.any(np.isin(possible_move_computer, [4])):
        table[1, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 4)
        print('chiudo')
        deleting_from_array(possible_move_player, 2)
        deleting_from_array(possible_move_computer, 2)
    elif not np.any(np.isin(possible_move_player, [7, 8])) and np.any(np.isin(possible_move_computer, [9])):
        table[2, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 9)
        print('chiudo')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)
    elif not np.any(np.isin(possible_move_player, [8, 9])) and np.any(np.isin(possible_move_computer, [7])):
        table[2, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 7)
        print('chiudo')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)
    elif not np.any(np.isin(possible_move_player, [1, 4])) and np.any(np.isin(possible_move_computer, [7])):
        table[2, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 7)
        print('chiudo')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)
    elif not np.any(np.isin(possible_move_player, [4, 7])) and np.any(np.isin(possible_move_computer, [1])):
        table[0, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 1)
        print('chiudo')
        deleting_from_array(possible_move_player, 1)
        deleting_from_array(possible_move_computer, 1)
    elif not np.any(np.isin(possible_move_player, [2, 5])) and np.any(np.isin(possible_move_computer, [8])):
        table[2, 1] = 'X'
        last_move_computer = np.append(last_move_computer, 8)
        print('chiudo')
        deleting_from_array(possible_move_player, 8)
        deleting_from_array(possible_move_computer, 8)
    elif not np.any(np.isin(possible_move_player, [5, 8])) and np.any(np.isin(possible_move_computer, [2])):
        table[0, 1] = 'X'
        last_move_computer = np.append(last_move_computer, 8)
        print('chiudo')
        deleting_from_array(possible_move_player, 2)
        deleting_from_array(possible_move_computer, 2)
    elif not np.any(np.isin(possible_move_player, [3, 6])) and np.any(np.isin(possible_move_computer, [9])):
        table[2, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 9)
        print('chiudo')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)
    elif not np.any(np.isin(possible_move_player, [6, 9])) and np.any(np.isin(possible_move_computer, [3])):
        table[0, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 3)
        print('chiudo')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)
    elif not np.any(np.isin(possible_move_player, [1, 5])) and np.any(np.isin(possible_move_computer, [9])):
        table[2, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 9)
        print('chiudo')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)
    elif not np.any(np.isin(possible_move_player, [5, 9])) and np.any(np.isin(possible_move_computer, [1])):
        table[0, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 1)
        print('chiudo')
        deleting_from_array(possible_move_player, 1)
        deleting_from_array(possible_move_computer, 1)
    elif not np.any(np.isin(possible_move_player, [3, 5])) and np.any(np.isin(possible_move_computer, [7])):
        table[2, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 7)
        print('chiudo')
        deleting_from_array(possible_move_player, 7)
        deleting_from_array(possible_move_computer, 7)
    elif not np.any(np.isin(possible_move_player, [5, 7])) and np.any(np.isin(possible_move_computer, [3])):
        table[0, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 3)
        print('chiudo')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)

    # Mossa per mettere due X adiacenti
    elif last_move_computer_num == 1 and np.any(np.isin(possible_move_computer, [2])):
        table[0, 1]
        last_move_computer = np.append(last_move_computer, 2)
        print('avanzo')
        deleting_from_array(possible_move_player, 2)
        deleting_from_array(possible_move_computer, 2)
    elif last_move_computer_num == 1 and np.any(np.isin(possible_move_computer, [4])):
        table[1, 0]
        last_move_computer = np.append(last_move_computer, 4)
        print('avanzo')
        deleting_from_array(possible_move_player, 4)
        deleting_from_array(possible_move_computer, 4)

    elif last_move_computer_num == 3 and np.any(np.isin(possible_move_computer, [2])):
        table[0, 1]
        last_move_computer = np.append(last_move_computer, 2)
        print('avanzo')
        deleting_from_array(possible_move_player, 2)
        deleting_from_array(possible_move_computer, 2)
    elif last_move_computer_num == 3 and np.any(np.isin(possible_move_computer, [6])):
        table[1, 2]
        last_move_computer = np.append(last_move_computer, 6)
        print('avanzo')
        deleting_from_array(possible_move_player, 6)
        deleting_from_array(possible_move_computer, 6)

    elif last_move_computer_num == 9 and np.any(np.isin(possible_move_computer, [6])):
        table[1, 2]
        last_move_computer = np.append(last_move_computer, 6)
        print('avanzo')
        deleting_from_array(possible_move_player, 6)
        deleting_from_array(possible_move_computer, 6)
    elif last_move_computer_num == 9 and np.any(np.isin(possible_move_computer, [8])):
        table[2, 1]
        last_move_computer = np.append(last_move_computer, 8)
        print('avanzo')
        deleting_from_array(possible_move_player, 8)
        deleting_from_array(possible_move_computer, 8)

    elif last_move_computer_num == 7 and np.any(np.isin(possible_move_computer, [4])):
        table[1, 0]
        last_move_computer = np.append(last_move_computer, 4)
        print('avanzo')
        deleting_from_array(possible_move_player, 4)
        deleting_from_array(possible_move_computer, 4)
    elif last_move_computer_num == 7 and np.any(np.isin(possible_move_computer, [8])):
        table[2, 1]
        last_move_computer = np.append(last_move_computer, 8)
        print('avanzo')
        deleting_from_array(possible_move_player, 8)
        deleting_from_array(possible_move_computer, 8)

    elif last_move_computer_num == 2 and np.any(np.isin(possible_move_computer, [1])):
        table[0, 0]
        last_move_computer = np.append(last_move_computer, 1)
        print('avanzo')
        deleting_from_array(possible_move_player, 1)
        deleting_from_array(possible_move_computer, 1)
    elif last_move_computer_num == 2 and np.any(np.isin(possible_move_computer, [3])):
        table[0, 2]
        last_move_computer = np.append(last_move_computer, 3)
        print('avanzo')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)
    elif last_move_computer_num == 2 and np.any(np.isin(possible_move_computer, [5])):
        table[1, 1]
        last_move_computer = np.append(last_move_computer, 5)
        print('avanzo')
        deleting_from_array(possible_move_player, 5)
        deleting_from_array(possible_move_computer, 5)

    elif last_move_computer_num == 6 and np.any(np.isin(possible_move_computer, [3])):
        table[0, 2]
        last_move_computer = np.append(last_move_computer, 3)
        print('avanzo')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)
    elif last_move_computer_num == 6 and np.any(np.isin(possible_move_computer, [5])):
        table[1, 1]
        last_move_computer = np.append(last_move_computer, 5)
        print('avanzo')
        deleting_from_array(possible_move_player, 5)
        deleting_from_array(possible_move_computer, 5)
    elif last_move_computer_num == 6 and np.any(np.isin(possible_move_computer, [9])):
        table[2, 2]
        last_move_computer = np.append(last_move_computer, 9)
        print('avanzo')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)

    elif last_move_computer_num == 8 and np.any(np.isin(possible_move_computer, [9])):
        table[2, 2]
        last_move_computer = np.append(last_move_computer, 9)
        print('avanzo')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)
    elif last_move_computer_num == 8 and np.any(np.isin(possible_move_computer, [5])):
        table[1, 1]
        last_move_computer = np.append(last_move_computer, 5)
        print('avanzo')
        deleting_from_array(possible_move_player, 5)
        deleting_from_array(possible_move_computer, 5)
    elif last_move_computer_num == 8 and np.any(np.isin(possible_move_computer, [7])):
        table[2, 0]
        last_move_computer = np.append(last_move_computer, 7)
        print('avanzo')
        deleting_from_array(possible_move_player, 7)
        deleting_from_array(possible_move_computer, 7)
    elif last_move_computer_num == 4 and np.any(np.isin(possible_move_computer, [1])):
        table[0, 0]
        last_move_computer = np.append(last_move_computer, 1)
        print('avanzo')
        deleting_from_array(possible_move_player, 1)
        deleting_from_array(possible_move_computer, 1)
    elif last_move_computer_num == 4 and np.any(np.isin(possible_move_computer, [5])):
        table[1, 1]
        last_move_computer = np.append(last_move_computer, 5)
        print('avanzo')
        deleting_from_array(possible_move_player, 5)
        deleting_from_array(possible_move_computer, 5)
    elif last_move_computer_num == 4 and np.any(np.isin(possible_move_computer, [7])):
        table[2, 0]
        last_move_computer = np.append(last_move_computer, 7)
        print('avanzo')
        deleting_from_array(possible_move_player, 7)
        deleting_from_array(possible_move_computer, 7)

    # Metti la X al centro se libera
    elif np.any(np.isin(possible_move_computer, [1, 2, 3, 4, 5, 6, 7, 8, 9])) and table[1, 1] != 'X' and table[
        1, 1] != '0':
        table[1, 1] = 'X'
        last_move_computer = np.append(last_move_computer, 5)
        print('centro')
        deleting_from_array(possible_move_player, 5)
        deleting_from_array(possible_move_computer, 5)

    # Metti la X all'angolo opposto di quello dell'avversario
    elif last_move_player_num == 1 and np.any(np.isin(possible_move_computer, [9])):
        table[2, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 9)
        print('1')
        deleting_from_array(possible_move_player, 9)
        deleting_from_array(possible_move_computer, 9)
    elif last_move_player_num == 3 and np.any(np.isin(possible_move_computer, [7])):
        table[2, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 7)
        print('3')
        deleting_from_array(possible_move_player, 7)
        deleting_from_array(possible_move_computer, 7)
    elif last_move_player_num == 7 and np.any(np.isin(possible_move_computer, [3])):
        table[0, 2] = 'X'
        last_move_computer = np.append(last_move_computer, 3)
        print('7')
        deleting_from_array(possible_move_player, 3)
        deleting_from_array(possible_move_computer, 3)
    elif last_move_player_num == 9 and np.any(np.isin(possible_move_computer, [1])):
        print('9')
        table[0, 0] = 'X'
        last_move_computer = np.append(last_move_computer, 1)
        deleting_from_array(possible_move_player, 1)
        deleting_from_array(possible_move_computer, 1)

    # Occupa un angolo vuoto qualsiasi
    elif np.any(np.isin(possible_move_computer, [1, 3, 7, 9])):
        print('Occupa un angolo')
        if np.any(np.isin(possible_move_computer, [1])):
            table[0, 0] = 'X'
            last_move_computer = np.append(last_move_computer, 1)
            deleting_from_array(possible_move_player, 1)
            deleting_from_array(possible_move_computer, 1)
        elif np.any(np.isin(possible_move_computer, [3])):
            table[0, 2] = 'X'
            last_move_computer = np.append(last_move_computer, 3)
            deleting_from_array(possible_move_player, 3)
            deleting_from_array(possible_move_computer, 3)
        elif np.any(np.isin(possible_move_computer, [7])):
            table[2, 0] = 'X'
            last_move_computer = np.append(last_move_computer, 7)
            deleting_from_array(possible_move_player, 7)
            deleting_from_array(possible_move_computer, 7)
        elif np.any(np.isin(possible_move_computer, [9])):
            table[2, 2] = 'X'
            last_move_computer = np.append(last_move_computer, 9)
            deleting_from_array(possible_move_player, 9)
            deleting_from_array(possible_move_computer, 9)

    # Occupa una casella vuota qualiasi
    elif not np.any(np.isin(possible_move_computer, [1, 2, 3, 4, 5, 6, 7, 8, 9])):
        print('Occupa una casella vuota')
        if np.any(np.isin(possible_move_computer, [1])):
            table[0, 0] = 'X'
            last_move_computer = np.append(last_move_computer, 1)
            deleting_from_array(possible_move_player, 1)
            deleting_from_array(possible_move_computer, 1)
        elif np.any(np.isin(possible_move_computer, [2])):
            table[0, 1] = 'X'
            last_move_computer = np.append(last_move_computer, 2)
            deleting_from_array(possible_move_player, 2)
            deleting_from_array(possible_move_computer, 2)
        elif np.any(np.isin(possible_move_computer, [3])):
            table[0, 2] = 'X'
            last_move_computer = np.append(last_move_computer, 3)
            deleting_from_array(possible_move_player, 3)
            deleting_from_array(possible_move_computer, 3)
        elif np.any(np.isin(possible_move_computer, [4])):
            table[1, 0] = 'X'
            last_move_computer = np.append(last_move_computer, 4)
            deleting_from_array(possible_move_player, 4)
            deleting_from_array(possible_move_computer, 4)
        elif np.any(np.isin(possible_move_computer, [5])):
            table[1, 1] = 'X'
            last_move_computer = np.append(last_move_computer, 5)
            deleting_from_array(possible_move_player, 5)
            deleting_from_array(possible_move_computer, 5)
        elif np.any(np.isin(possible_move_computer, [6])):
            table[1, 2] = 'X'
            last_move_computer = np.append(last_move_computer, 6)
            deleting_from_array(possible_move_player, 6)
            deleting_from_array(possible_move_computer, 6)
        elif np.any(np.isin(possible_move_computer, [7])):
            table[2, 0] = 'X'
            last_move_computer = np.append(last_move_computer, 7)
            deleting_from_array(possible_move_player, 7)
            deleting_from_array(possible_move_computer, 7)
        elif np.any(np.isin(possible_move_computer, [8])):
            table[2, 1] = 'X'
            last_move_computer = np.append(last_move_computer, 8)
            deleting_from_array(possible_move_player, 8)
            deleting_from_array(possible_move_computer, 8)
        elif np.any(np.isin(possible_move_computer, [9])):
            table[2, 2] = 'X'
            last_move_computer = np.append(last_move_computer, 9)
            deleting_from_array(possible_move_player, 9)
            deleting_from_array(possible_move_computer, 9)
