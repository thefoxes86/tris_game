import numpy as np


def check_place_computer(table):
    print(np.where(table != '-', table, 'X'))
    print(table)
