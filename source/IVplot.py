from data_set import data_set
import matplotlib.pyplot as plt

def IVplot(x,y,number=0):
    IV_x = data_set(x)
    IV_y = data_set(y, 1)
    plt.scatter(IV_x[number], IV_y[number], label='{}'.format('Raw IV'))
    plt.xlabel('Voltage[V]')
    plt.ylabel('Current[A]')
    plt.title('IV-analysis raw & processed')
    plt.yscale("log")
