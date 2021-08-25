import numpy as np
import pandas as pd

from utils.deleting_from_array import deleting_from_array
from utils.place_sign import place_sign_1_player
from utils.place_sign import place_sign_2_players

table_tris = np.array(
    [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
)
possible_move_player = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
possible_move_computer = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
last_move_player = np.array([])
columns_table = ["Col 1", "Col 2", "Col 3"]
index_table = ["Row 1", "Row 2", "Row 3"]
dataset = pd.DataFrame(data=table_tris, columns=columns_table)
print(table_tris)

num_player = input(
    "Inserisci il numero della cella dove vuoi mettere il tuo segno. \nIl giocatore 1 ha il segno 0 mentre il giocatore 2 ha la X \nSe vuoi giocare contro il computer scrivi 1 altrimenti scrivi 2: "
)

i = 1
n = 10

if num_player == '1':
    while i < n:
        sign = input("Giocatore 1: ")
        if (i == 1):
            possible_new_move_player = deleting_from_array(possible_move_player, sign)
            possible_new_move_computer = deleting_from_array(possible_move_player, sign)
        else:
            possible_new_move_player = deleting_from_array(possible_new_move_player, sign)
            possible_new_move_computer = deleting_from_array(possible_new_move_player, sign)

        last_move_player = np.append(last_move_player, sign)

        result = place_sign_1_player(table_tris, sign, possible_new_move_player, possible_new_move_computer,
                                     last_move_player)
        if result == 1:
            print('Vittoria Giocatore 1')
            print(table_tris)
            break
        elif result == 2:
            print('Vittoria Computer')
            print(table_tris)
            break
        elif result == False:
            i = i
            print('Cella già inserita, riprova')
            print(table_tris)
        elif result == None:
            print('Prossimo turno')
            print(table_tris)
            i = i + 1

elif num_player == '2':
    while i < n:
        if i % 2 == 0:
            player = 2
            sign = input("Giocatore 2: ")
            result = place_sign_2_players(table_tris, sign, player)
            if result == 1:
                print('Vittoria Giocatore 1')
                print(table_tris)
                break
            elif result == 2:
                print('Vittoria Giocatore 2')
                print(table_tris)
                break
            elif result == False:
                i = i
                print('Cella già inserita, riprova')
                print(table_tris)
            elif result == None:
                print('Prossimo turno')
                print(table_tris)
                i = i + 1
        else:
            player = 1
            sign = input("Giocatore 1: ")
            result = place_sign_2_players(table_tris, sign, player)
            if result == 1:
                print('Vittoria Giocatore 1')
                print(table_tris)
                break
            elif result == 2:
                print('Vittoria Giocatore 2')
                print(table_tris)
                break
            elif result == False:
                i = i
                print('Cella già inserita, riprova')
                print(table_tris)
                continue
            elif result == None:
                print('Prossimo turno')
                print(table_tris)
                i = i + 1
                continue
else:
    num_player
