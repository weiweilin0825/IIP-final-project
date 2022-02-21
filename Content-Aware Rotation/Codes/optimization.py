import numpy as np 
from line_matrix import *
from shape_matrix import *
from boundary_matrix import *
from pk import *
from math import cos, sin

def fix_theta_solve_v(line, shape, boundary, b, lambda_l, lambda_r, lambda_b, n, k):
    
    A = shape/n + lambda_b*(np.transpose(boundary).dot(boundary)) + lambda_l*line/k
    b = -lambda_b*(np.transpose(boundary).dot(b))
    V = np.linalg.solve(A,b)

    return V



def fix_v_solve_theta(UK, lines, thetas, V_new, rotation_angle, dx, dy, N, x, y, sdelta, lambda_l, lambda_r):

    k = len(lines)
    delta = rotation_angle

    beta_min = 1
    beta_max = 10000
    beta = beta_min

    M = len(thetas)
    A = np.zeros((k,M))

    for i in range(len(lines)):
        temp=  lines[i][5]
        A[i][int(temp) - 1] = 1

    T_1 = np.zeros((M, M))
    T_1[0:M-1, 1:M] = np.eye(M - 1)
    T_1[M-1, 0] = 1
    D = np.eye(M, M) - T_1
    Pk = computepk(lines, dx, dy, N, x, y)
    Vx = np.zeros(N)
    Vy = np.zeros(N)
    for i in range(N):
        Vx[i] = V_new[2 * i]
        Vy[i] = V_new[2 * i + 1]      
    e_x = Pk.dot(Vx)
    e_y = Pk.dot(Vy)
    e = np.array([e_x,e_y, np.arccos(np.divide(e_x,(np.sqrt(np.square(e_x)+np.square(e_y)))))*180 / np.pi])
    e = e.transpose()
    phi_k = np.zeros(k)
    phi = np.zeros((k, 100))

    while(beta <= beta_max):
        for i in range(len(lines)):
            ek_uk = e[i][2] - lines[i][4]   # Angle between line and bin
            bin_ = lines[i][5]              # Bin for the line in question
            thetam_k = thetas[int(bin_)-1]  # Computing the angle if beta->infintiy

            phi[i] = (np.linspace(ek_uk, thetam_k, num= 100))
            temp = np.zeros(100)
            U = UK[i]     

            for j in range(100):
                Rk = np.array([[cos(phi[i][j]/np.pi*180),-sin(phi[i][j]/np.pi*180)],
                    [sin(phi[i][j]/np.pi*180), cos(phi[i][j]/np.pi*180)]])

                current = (Rk.dot(U).dot(np.transpose(Rk)) - np.eye(2)).dot((e[i][0:2]))

                temp[j] = lambda_l/k*(sum(np.square(current))) + beta*(np.square(phi[i][j] - thetam_k)).sum()

            index = np.argmin(temp)

            phi_k[i] = phi[i][index]    # Find that phi that minimizes the energy by creating a small table

        H = beta*(np.transpose(A).dot(A)) + lambda_r*np.diag(sdelta) + lambda_r*np.transpose(D).dot(D)
        h = beta*np.transpose(A).dot(phi_k) + (lambda_r*np.diag(sdelta).dot(np.ones(M))*delta)
        thetas = np.linalg.solve(H,h)
        beta = beta*10

    return thetas