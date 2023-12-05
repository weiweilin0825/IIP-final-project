import numpy as np
from math import floor
from math import ceil
from math import pi
from line_matrix import *
from shape_matrix import *
from boundary_matrix import *
from pk import *

def perp(a) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1, a2, b1, b2) :
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = np.dot(dap, db)
    num = np.dot(dap, dp)
    return (num / denom.astype(float)) * db + b1


def quantize_and_get(X,Y,threshold,linesegthreshold,dx,dy,delta,file_name):

    # Reading the file corresponding to the image that was generated 
    # using the Line Segment Detector that the authors have used
    file = open(file_name,'r')
    lines_list = []
    for i in file:
        arr = i.split()
        for elem in range(len(arr)):
            arr[elem] = float(arr[elem])
        lines_list.append(arr)
    file.close()

    lines = np.zeros((1, 6))
    lines_count = 0

    for i in range(len(lines_list)):
        x1 = lines_list[i][0]; y1 = lines_list[i][1]; x2 = lines_list[i][2]; y2 = lines_list[i][3]

        if (max(x1, x2) > X or max(y1, y2) > Y or min(x1, x2, y1, y2)<1):
            continue

        if ((x1 - x2)**2 + (y1 - y2)**2) < linesegthreshold:
            continue

        if x1 > x2:
            right_x = x1
            left_x = x2
        else:
            left_x = x1
            right_x = x2

        if y1 > y2:
            y_top = y2
            y_bottom = y1
        else:
            y_top = y1
            y_bottom = y2
        
        xi_ = np.array([x1,x2])
        yi_ = np.array([y1,y2])

        value = ceil(left_x / dx) * dx
        while(value <= floor((right_x) / dx) * dx):            
            arg1, arg2 = np.array([x1, y1]), np.array([x2, y2])
            val = seg_intersect(arg1, arg2, np.array([value, 0]), np.array([value, Y]))     

            if val[0] != np.inf and val[0] != np.nan and val[1] != np.inf and val[1] != np.nan: 
                xi_ = np.append(xi_, val[0])
                yi_ = np.append(yi_, val[1])
            value = value+dx
        
        value = ceil(y_top / dy) * dy
        while(value <= floor(y_bottom / dy) * dy + 1):
            arg1,arg2 = np.array([x1, y1]), np.array([x2, y2])
            val = seg_intersect(arg1, arg2, np.array([0, value]), np.array([X, value]))
            if val[0] != np.inf and val[0] != np.nan and val[1] != np.inf and val[1] != np.nan:
                xi_ = np.append(xi_, val[0])
                yi_ = np.append(yi_, val[1])
            value = value + dy
            
        xi_sorted = []
        yi_sorted = []
        for i_ in range(len(xi_)):
            xi_sorted.append(xi_[i_])
            yi_sorted.append(yi_[i_])
    
        val_ = np.argsort(yi_)
        yi_sorted.sort()
        new_arr = []
        for i_ in range(len(val_)):
            new_arr.append(xi_sorted[val_[i_]])
        xi_sorted = new_arr
        
        for j in range(len(yi_sorted) - 1):
            if((xi_sorted[j] - xi_sorted[j+1])**2 + (yi_sorted[j] - yi_sorted[j+1])**2 < linesegthreshold):
                continue
            else:
                lines_count+=1

                temp = np.zeros((1,6))
                temp[0][0] = xi_sorted[j]
                temp[0][1] = yi_sorted[j]
                temp[0][2] = xi_sorted[j+1]
                temp[0][3] = yi_sorted[j+1]
                temp[0][4] = np.arctan((temp[0][3]-temp[0][1])/(temp[0][2]-temp[0][0]))*180/pi
                
                if temp[0][4] <= 0:
                    temp[0][4] += 180

                temp[0][5] = ceil((temp[0][4]+delta)/(180/90))
                if temp[0][5] < 0:
                    temp[0][5] = temp[0][5]+90
                if temp[0][5] > 90:
                    temp[0][5] = temp[0][5]-90
                lines = np.append(lines,temp)

    lines = lines[6:]  # Remove the inital initialisation for the lines - lines  = np.zeros(6)
    lines = lines.reshape((lines_count,6))

    return lines