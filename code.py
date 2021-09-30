import numpy as np


def p1(k: int) -> str:
    out=""
    for i in range(k,0):
        out = out + str(k**i) + ","
    
    return out


