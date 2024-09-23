import numpy as np


def float_format():

    A=np.array(input("enter the number like 1.3:").split(','),dtype=float)


    return np.ceil(A) , np.floor(A) , np.rint(A)


# sample