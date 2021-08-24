import numpy as np
import pandas as pd

from utils.place_sign import place_sign

table_tris = np.array(
    [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
)
columns_table = ["Col 1", "Col 2", "Col 3"]
index_table = ["Row 1", "Row 2", "Row 3"]
dataset = pd.DataFrame(data=table_tris, columns=columns_table)
print(table_tris)

input(
    "Inserisci il numero della cella dove vuoi mettere il tuo segno. \nIl giocatore 1 ha il segno 0 mentre il giocatore 2 ha la X \n"
)

i = 1
n = 10
while i < n:
    if i % 2 == 0:
        player = 2
        sign = input("Giocatore 2: ")
        result = place_sign(table_tris, sign, player)
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
        result = place_sign(table_tris, sign, player)
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
