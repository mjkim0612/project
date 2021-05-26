import numpy as np
from poly_fitting import polyfitting_po
def R_square(y_value,fit_value):
    y_value_mean = np.mean(np.ravel(y_value))
    Tss = np.sum((np.ravel(y_value)-y_value_mean)**2)
    Rss = np.sum((np.ravel(y_value)-np.ravel(fit_value))**2)
    results = 1 - (Rss/Tss)
    return results

def find_best_fit_ind(order,x_value,y_value):
    IL_fit_value = polyfitting_po(order, x_value, y_value)
    rs_list = []
    for i in range(0,len(IL_fit_value)):
        IL_R = R_square(y_value,IL_fit_value[i])
        rs_list.append(IL_R)
    rs_min = []
    for i in range(0,len(rs_list)):
        rs_min.append(abs(rs_list[i]-1))
    global rs_min3
    rs_min2 = min(rs_min)
    IL_ind = rs_min.index(rs_min2)
    rs_min3 = rs_list[IL_ind]
    return IL_ind

def find_R_square(order,x_value,y_value):
    IL_fit_value = polyfitting_po(order, x_value, y_value)
    rs_list = []
    for i in range(0,len(IL_fit_value)):
        IL_R = R_square(y_value,IL_fit_value[i])
        rs_list.append(IL_R)
    return rs_list

def get_R2():
    return rs_min3