import numpy as np

def polyfitting_p1d1(number,x,y):
    p_list = []
    for i in range(13,number):
        p_list.append(np.polyfit(x,y,i))
    p1d_list = []
    for i in range(13,number):
        p1d_list.append(np.poly1d(p_list[i-13]))
    return p1d_list

def polyfitting_p1d2(number,x,y):
    p_list = []
    for i in range(0,number):
        p_list.append(np.polyfit(x,y,i))
    p1d_list = []
    for i in range(0,number):
        p1d_list.append(np.poly1d(p_list[i]))
    return p1d_list


def polyfitting_po(number,x,y):
    p_list = []
    for i in range(0,number):
        p_list.append(np.polyfit(x,y,i))
    p1d_list = []
    for i in range(0,number):
        p1d_list.append(np.poly1d(p_list[i]))
    po_list = []
    for i in range(0,number):
        po_list.append((p1d_list[i])(x))
    return po_list