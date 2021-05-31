import glob2
import xml.etree.ElementTree as elemTree
import matplotlib.pyplot as plt
from IVplot import IVplot
from exp_fitting import IVfitting
from exp_fitting import return_R
from exp_fitting import return_IV_dic
import ILplot
import R_square
from datetime import datetime
import pandas as pd
import warnings
import os
warnings.filterwarnings(action='ignore')
import time

filename_list = []
wafer_list = []
lot_list = []
mask_list = []
testsite_list = []
name_list = []
date_list = []
dierow_list = []
diecolumn_list = []
pat_list = []
operator_list = []
error_flag_list = []
error_description_list = []
Rsq_IV_list = []
I_1 = []
I_2 = []
analy_list = []
IL_R2_list = []
testsiteinfo_list = [wafer_list,lot_list,mask_list,dierow_list,diecolumn_list,testsite_list]
testsite_attrib_list = ['Wafer','Batch','Maskset','DieRow','DieColumn','TestSite']
pddata_list = []
anal = ['DCM_LMZC','DCM_LMZO']
def run(path_file=False,show=False,save_fig=False,save_csv=False,file_input=None):
    j = 0
    data_dic = {'Lot' : lot_list,
                'Wafer': wafer_list,
                'Mask' : mask_list,
                'TestSite' : testsite_list,
                'Name' : name_list,
                'Date' : date_list,
                'Operator': operator_list,
                'Row' : dierow_list,
                'Column' : diecolumn_list,
                'error_flag' : error_flag_list,
                'error_description' : error_description_list,
                'Analysis Wavelength': analy_list,
                'Rsq of Ref. spectrum': IL_R2_list,
                'Rsq of IV' : Rsq_IV_list,
                'I at 1V[A]' : I_2,
                'I at -1V[A]' : I_1}

    if path_file == False:
        path = glob2.glob('.\data\**\*.xml')
    else:
        path = path_file

    file_list = []
    for i in path:
        if i.split('\\')[-1][-12:-4] in anal :
            file_list.append(i)
    file_num = len(file_list)

    start = time.time()

    for i in path:
        tree = elemTree.parse(i)
        testsiteinfo = list(tree.iter('TestSiteInfo'))[0]

        if testsiteinfo.attrib['TestSite'] in anal:
            filename = file_list[j].split('\\')[-1][:-4]
            for k in range(0,len(testsiteinfo_list)):
                testsiteinfo_list[k].append(testsiteinfo.attrib[testsite_attrib_list[k]])
            date = list(tree.iter('OIOMeasurement'))[0]
            dateti = datetime.strptime(date.attrib['CreationDate'], '%a %b %d %H:%M:%S %Y')
            datet = dateti.strftime('%Y%m%d_%H%M%S')
            date_list.append(datet)
            operator_list.append(date.attrib['Operator'])
            name = tree.find('ElectroOpticalMeasurements/ModulatorSite/Modulator')
            name_list.append(name.attrib['Name'])
            plt.figure(figsize = (18,12))
            plt.subplot(224)
            IVvoltage = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Voltage')
            IVcurrent = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current')
            IVplot(IVvoltage,IVcurrent)
            IVfitting(IVvoltage,IVcurrent)
            R_s = return_R()
            IV_dict = return_IV_dic()
            I_1.append(IV_dict[-1.0])
            I_2.append(IV_dict[1.0])
            Rsq_IV_list.append(R_s)
            analy_wavelength = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo/DesignParameters/DesignParameter')
            for k in range(0,len(analy_wavelength)):
                if analy_wavelength[k].attrib['Symbol'] == 'WL':
                    analy_list.append(analy_wavelength[k].text)
            if R_s < 0.95:
                error_flag_list.append(1)
                error_description_list.append('Rsq error')
            else:
                error_flag_list.append(0)
                error_description_list.append('No error')
            Wavelength = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep/L')
            IL = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep/IL')
            DCbias = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep')
            plt.subplot(221)
            ILplot.IL_raw_plot(Wavelength,IL,ILplot.find_DCbias(DCbias))
            plt.subplot(222)
            ILplot.IL_fitting_ref(Wavelength,IL,8)
            plt.subplot(223)
            ILplot.IL_processed_plot(Wavelength,IL,ILplot.find_DCbias(DCbias),8)
            IL_R_2 =R_square.get_R2()
            IL_R2_list.append(IL_R_2)
            if show == True:
                plt.show()

            if save_fig == False:
                if not os.path.exists('./result/{}'.format(i.split('\\')[2])):
                    os.makedirs('./result/{}'.format(i.split('\\')[2]))
                if not os.path.exists('./result/{}/{}'.format(i.split('\\')[2],i.split('\\')[3])):
                    os.makedirs('./result/{}/{}'.format(i.split('\\')[2],i.split('\\')[3]))
                if not os.path.exists('./result/{}/{}/{}'.format(i.split('\\')[2],i.split('\\')[3],i.split('\\')[4])):
                    os.makedirs('./result/{}/{}/{}'.format(i.split('\\')[2],i.split('\\')[3],i.split('\\')[4]))
                plt.savefig('./result/{}/{}/{}/{}.png'.format(i.split('\\')[2],i.split('\\')[3],i.split('\\')[4],filename), bbox_inches = 'tight')
            plt.cla()
            plt.subplot(224)
            plt.cla()
            plt.subplot(221)
            plt.cla()
            plt.subplot(222)
            plt.cla()
            if j < 98 :
                j = j+1

            print(filename, 'processed({}/{})'.format(j, file_num))

    if file_input != None:
        file_input_list = file_input.split(',')
        df_list = []
        index_list = []
        for i in file_input_list:
            df_list.append(data_dic[i])
        for _ in df_list[0]:
            index_list.append('')
        df = pd.DataFrame(data = df_list[:len(df_list)], index = file_input_list, columns = index_list)
        if save_csv == False:
            df.T.to_csv('./result/result.csv')
    else:
        index_list = []
        for _ in range(0,j):
            index_list.append('')
        df = pd.DataFrame(data = data_dic, index = index_list)
        if save_csv == False:
            df.to_csv('./result/result.csv')

    print("time for processed :", round(time.time() - start),"s")
