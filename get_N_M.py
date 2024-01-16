import numpy as np
import sys
import logging
import time
import matplotlib.image as mpimg


Nargs = 2
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])



def get_n_m_fromfile(file):
    u = rgb2gray(mpimg.imread(file))
    u /= np.max(u)
    nx,ny=u.shape
    return  nx,ny

if len(sys.argv) != Nargs:
    print("Number of arguments is incorrect!")
    exit("usage: python get_N_M.py input_file")

N,M  = get_n_m_fromfile(sys.argv[1])
#print("N = ", nx)
#iprint("M = ", ny)
print(f"{N}_{M}")
