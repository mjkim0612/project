from data_set import data_set
import matplotlib.pyplot as plt
from poly_fitting import polyfitting_po
import R_square

def find_DCbias(x):
    DCbias = x
    DC_li = []
    for i in range(0,len(DCbias)-1):
        DC = DCbias[i].get('DCBias')
        DC_li.append(DC+'V')
    DC_li.append('ref')
    return DC_li

def IL_raw_plot(x,y,DC):
    IL_x = data_set(x)
    IL_y = data_set(y)
    for i in range(0,len(x)):
        plt.scatter(IL_x[i],IL_y[i],label = DC[i])
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.title('Transmission spectra - as measured')
    plt.legend(ncol=4)

def IL_fitting_ref(x,y,order=6):
    IL_x = data_set(x)
    IL_y = data_set(y)
    global rs_list
    rs_list = []
    global fit_data
    fit_data = polyfitting_po(order, IL_x[6], IL_y[6])
    for k in range(0,len(fit_data)):
        rs_list.append(R_square.R_square(IL_y[6],fit_data[k]))
    for i in range(0,3):
        plt.plot(IL_x[6],fit_data[i],label='{}{} {} {}'.format(i+4,'$^{th}$','$R^{2}$ =',round(rs_list[i],5)))
    plt.legend(ncol=3, loc=8)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.title('Transmission spectra - processed ref')

def IL_processed_plot(x,y,DC,order=6):
    IL_x = data_set(x)
    IL_y = data_set(y)
    for i in range(0, len(x)):
        x = IL_x[i]
        y = []
        try:
            for k in range(0,len(IL_y[i])):
                y.append(float(IL_y[i][k])-fit_data[-1][k])
        except:
            x = IL_x[i][0:len(fit_data[-1])]
            y = y[0:len(fit_data[-1])]
        plt.plot(x, y, label=DC[i])
    plt.legend(ncol=4)
    plt.ylabel('Measured transmission[dB]')
    plt.xlabel('Wavelength[nm]')
    plt.title('Transmission spectra - as measured & processed for {}{} fit ref'.format(6, '$^{th}$'))

def get_R():
    return rs_list