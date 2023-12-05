import numpy as np
from math import floor
from line_matrix import *
from shape_matrix import *
from boundary_matrix import *


def computepk(lines, dx, dy, N, x, y):

    Pk = np.zeros((len(lines),N))
    x = x+1
    y = y+1
    for i in range(len(lines)):

        x1 = lines[i][0]+1
        y1 = lines[i][1]+1
        x2 = lines[i][2]+1
        y2 = lines[i][3]+1
        
        min_x = min(x1,x2) 
        min_y = min(y1,y2)
        
        xleft = floor((min_x-1)/dx)+1
        xright= xleft+1

        ytop = floor((min_y-1)/dy)+1
        ybottom= ytop+1

        Pkmatrix1 = np.zeros((len(y),len(x)))
        Pkmatrix2 = np.zeros((len(y),len(x)))
        PkmatrixV = np.zeros((len(y),len(x)))

        
        # Using bilinear interpolation to construct Pk 
        Pkmatrix1[ytop-1,xleft-1] = ((x[xright-1]-x1)/dx)*((y[ybottom-1]-y1)/dy)
        Pkmatrix1[ytop-1,xright-1]= ((x1-x[xleft-1])/dx)*((y[ybottom-1]-y1)/dy)
        Pkmatrix1[ybottom-1,xleft-1]= ((x[xright-1]-x1)/dx)*((y1-y[ytop-1])/dy)
        Pkmatrix1[ybottom-1,xright-1]=((x1-x[xleft-1])/dx)*((y1-y[ytop-1])/dy)

        Pkmatrix2[ytop-1,xleft-1] = ((x[xright-1]-x2)/dx)*((y[ybottom-1]-y2)/dy)
        Pkmatrix2[ytop-1,xright-1]= ((x2-x[xleft-1])/dx)*((y[ybottom-1]-y2)/dy)
        Pkmatrix2[ybottom-1,xleft-1]= ((x[xright-1]-x2)/dx)*((y2-y[ytop-1])/dy)
        Pkmatrix2[ybottom-1,xright-1]=((x2-x[xleft-1])/dx)*((y2-y[ytop-1])/dy)

        Pk[i] = np.reshape((Pkmatrix2- Pkmatrix1).transpose(),N)
        
    return Pk