import numpy as np


def deleting_from_array(arr, pos):
    newArr = np.delete(arr, np.where(arr == int(pos)))
    return newArr
