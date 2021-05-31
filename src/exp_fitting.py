from lmfit import Model
from R_square import R_square
import numpy as np
from data_set import data_set
import matplotlib.pyplot as plt
from poly_fitting import polyfitting_p1d1

def IVfitting(x,y,number=0):
    global R
    def expfuc(x, a, b, c):
        return b * (np.exp(a * x) - 1) * c + IV_fit_value[i](x)
    IV_x = data_set(x)
    IV_y = data_set(y,1)
    IV_fit_value = polyfitting_p1d1(15,IV_x[number][:10],IV_y[number][:10])
    emodel = Model(expfuc)
    fit_result = []
    fit = []
    for i in range(0,len(IV_fit_value)):
        result1 = emodel.fit(IV_y[number],x = IV_x[number], b = 1, a = 1, c = 1)
        R = R_square(IV_y[number],result1.best_fit)
        fit_result.append(R)
        fit.append(result1.best_fit)
    rs_min = []
    for i in range(0,len(fit_result)):
        rs_min.append(abs(fit_result[i]-1))
    rs_min2 = min(rs_min)
    IV_ind = rs_min.index(rs_min2)
    R = fit_result[IV_ind]

    global IV_dic
    plt.plot(IV_x[number],fit[IV_ind],'r-',label = '{} {}{} {} {}'.format('processed',IV_ind+13,'$^{th}$','$R^{2}$ =',R))
    IV_dic = {y:x for x,y in zip(fit[IV_ind],IV_x[number])}
    plt.text(1.0,IV_dic[1.0],IV_dic[1.0],fontsize = 8,horizontalalignment = 'right')
    plt.text(-1.0,IV_dic[-1.0],IV_dic[-1.0],fontsize = 8)
    plt.xlabel('Voltage[V]')
    plt.ylabel('Current[A]')
    plt.title('IV-analysis raw & processed')
    plt.yscale("log")
    plt.legend(loc = 'best')

def return_R():
    return R

def return_IV_dic():
    return IV_dic