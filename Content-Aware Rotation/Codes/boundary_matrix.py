import numpy as np
from line_matrix import *
from shape_matrix import *
from pk import *

# Ensure that very rigid conditions are imposed on the boundaries
def formboundary(N,X,Y,gridX,gridY):

    energy_vx = np.zeros(N)  # energy for x coordinate vertices
    energy_vy = np.zeros(N)  # energy for y coordinate vertices
    energy_v = np.zeros(2*N)  # total energy
    bx = np.zeros(N)
    by = np.zeros(N)
    b = np.zeros(2*N)  # the RHS in the first part of the linear equations

    tempgridX = gridX.astype(np.uint16)
    tempgridY = np.rint(gridY)
    
    # left border
    idx = (tempgridX == 0)
    idx = idx.transpose().reshape(N)
    energy_vx[idx]=1
    bx[idx] = -1

    # right border
    idx = (tempgridX==X-1)
    idx = idx.transpose().reshape(N)
    energy_vx[idx] = 1
    bx[idx] = -(X)

    # top border
    idx = (tempgridY==0)
    idx = idx.transpose().reshape(N)
    energy_vy[idx]=1
    by[idx] = -(1)

    # bottom border
    idx = (tempgridY == Y-1)
    idx = idx.transpose().reshape(N)
    energy_vy[idx] = 1
    by[idx] = -(Y)


    for i in range(N):
        energy_v[2*i] = energy_vx[i]
        energy_v[2*i+1] = energy_vy[i]
        b[2*i] = bx[i]
        b[2*i+1] = by[i]

    boundary_matrix = np.diag(energy_v)     
    return boundary_matrix,b
