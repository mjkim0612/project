from data_set import data_set
import matplotlib.pyplot as plt
from poly_fitting import polyfitting_po
import R_square

def find_DCbias(x):
    DCbias = x
    global DC_li
    DC_li = []
    for i in range(0,len(DCbias)-1):
        DC = DCbias[i].get('DCBias')
        DC_li.append(DC+'V')
    DC_li.append('ref')
    return DC_li

def IL_raw_plot(x,y):
    IL_x = data_set(x)
    IL_y = data_set(y)
    for i in range(0,len(x)):
        plt.scatter(IL_x[i],IL_y[i],label = DC_li[i])
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.title('Transmission spectra - as measured')
    plt.legend(ncol=4)

def IL_fitting_ref(x,y,order=6):
    IL_x = data_set(x)
    IL_y = data_set(y)
    rs_list = R_square.find_R_square(order, IL_x[6], IL_y[6])
    fit_data = polyfitting_po(order, IL_x[6], IL_y[6])
    for i in range(4,order):
        plt.plot(IL_x[6],fit_data[i-4],label='{}{} {} {}'.format(i,'$^{th}$','$R^{2}$ =',round(rs_list[i-4],5)))
    plt.legend(ncol=2, loc=8)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.title('Transmission spectra - processed ref')

def IL_processed_plot(x,y,order=6):
    IL_x = data_set(x)
    IL_y = data_set(y)
    ind_IL = R_square.find_best_fit_ind(order, IL_x[6], IL_y[6])
    fit_data = polyfitting_po(order,IL_x[6],IL_y[6])
    for i in range(0, len(x)):
        x = IL_x[i]
        y = []
        try:
            for k in range(0,len(IL_y[i])):
                y.append(float(IL_y[i][k])-fit_data[ind_IL][k])
        except:
            x = IL_x[i][0:len(fit_data[ind_IL])]
            y = y[0:len(fit_data[ind_IL])]
        plt.plot(x, y, label=DC_li[i])
    plt.legend(ncol=4)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.title('Transmission spectra - as measured & processed for {}{} fit ref'.format(ind_IL+4, '$^{th}$'))