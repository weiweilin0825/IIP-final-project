import pandas as pd
import cv2 as cv
import numpy as np 
from line_matrix import *
from shape_matrix import *
from extractlines import quantize_and_get
from boundary_matrix import *
from pk import *
from optimization import *


angle = input('Enter the Angle of Rotation ')
rotation_angle = float(angle)
delta = rotation_angle

img = cv.imread('tower_3.jpeg')
Y, X = img.shape[:2]
name = 'tower.result.txt'

cx = int(X/30)  # Number of Quads along the horizontal direction
cy = int(Y/30)  # Number of Quads along the vertical direction
n_quads = cx * cy
number_of_vertices = (cx + 1) * (cy + 1)  # Total Number of Mesh Vertices
x_len = (X - 1) / cx  # Distance between subsequent Quads along x_direction
y_len = (Y - 1) / cy  # Distance between subsequent Quads along y_direction

# For choosing the correct line segements among those that were detected
threshold = 16
linesegthreshold = (x_len**2 + y_len**2) / 64

temp = 0
vertexX = np.zeros(1)  # List of all the X_coordinates of the grid points
while(1):
    temp += x_len
    temp = (round(temp, 10))
    vertexX = np.append(vertexX, temp)
    if temp > X-2:
        break

temp = 0
vertexY = np.zeros(1)  # List of all the Y_coordinates of the grid points
while(1):
    temp += y_len
    temp = (round(temp, 10))
    vertexY = np.append(vertexY, temp)
    if temp > Y-2:
        break

gridX, gridY = np.meshgrid(vertexX, vertexY)  # Meshgrid that we form using these vertices
Vx = np.reshape(gridX,number_of_vertices, 'C')
Vy = np.reshape(gridY,number_of_vertices, 'C')
V = np.zeros((number_of_vertices * 2))
for i in range(number_of_vertices):
    V[2*i] = Vx[i]
    V[2*i+1] = Vy[i]
V = V+1
print('The Dimension of the Image are ', X, Y)


sdelta = np.zeros(90)
sdelta[0] = 1000
sdelta[44] = 1000
sdelta[45] = 1000
sdelta[89] = 1000


print("Line Extraction and Quantization Begin....")
lines = quantize_and_get(X, Y, threshold, linesegthreshold, x_len, y_len, delta, name)
print("Line Extraction and Quantization Done .... ")
print("Forming the functions for Shape, Line, Boundary and Rotation Constraints...")


thetas = np.ones((90))*delta

Pk_all,line,UK = formline(lines,number_of_vertices,x_len,y_len,vertexX,vertexY,thetas)
shape_preservation = formshape(vertexX,vertexY,number_of_vertices,n_quads)
boundary,b = formboundary(number_of_vertices,X,Y,gridX,gridY)

lambda_l = 100
lambda_b = 10 ** 8
lambda_r = 100  


###### Optimization Begin ######
print('Boundary Matrix Dimension is ',boundary.shape)
print('Shape Matrix Dimension is ',shape_preservation.shape)
print('Line Matrix Dimension is ',line.shape)
print('PK_all is ',Pk_all.shape)
print('Dimension of b used in fix_theta_solve_v is ',b.shape)

n = number_of_vertices
k = len(lines)
print('The Total Number of vertices used are', n)
print('The total number of lines detected using the author usage line segment detector are',k)

V_new = np.zeros(len(V))

dx = x_len  # Increments in X
dy = y_len  # Increments in Y
N = number_of_vertices
x = vertexX  # List of all the vertices in the meshgrid
y = vertexY  # List of all the vertices in the meshgrid

for number_of_iteration in range(1,11):
	print("Iteration Number ", number_of_iteration)
	V_new = fix_theta_solve_v(line, shape_preservation, boundary, b, lambda_l, lambda_r, lambda_b, n, k)
	thetas = fix_v_solve_theta(UK, lines, thetas, V_new, rotation_angle, dx, dy, N, x, y, sdelta, lambda_l, lambda_r)
	if number_of_iteration != 10:
		Pk_all, line, UK = formline(lines, number_of_vertices, x_len, y_len, vertexX, vertexY, thetas)

print('Optimization Done.')


df = pd.DataFrame(thetas)
df.to_csv('theta.csv')
df = pd.DataFrame(V_new)
df.to_csv('vertex.csv')


