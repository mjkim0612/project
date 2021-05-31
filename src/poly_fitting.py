import numpy as np

def polyfitting_p1d1(number,x,y):
    p_list = []
    for i in range(12,number):
        p_list.append(np.polyfit(x,y,i))
    p1d_list = []
    for i in range(12,number):
        p1d_list.append(np.poly1d(p_list[i-12]))
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
    for i in range(4,number):
        p_list.append(np.polyfit(x,y,i-4))
    p1d_list = []
    for i in range(4,number):
        p1d_list.append(np.poly1d(p_list[i-4]))
    po_list = []
    for i in range(4,number):
        po_list.append((p1d_list[i-4])(x))
    return po_list