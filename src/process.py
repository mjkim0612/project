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
import shutil

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
error_flag_IL_list = []
error_description_IL_list = []
error_flag_IV_list = []
error_description_IV_list = []
Rsq_IV_list = []
I_1 = []
I_2 = []
analy_list = []
IL_R2_list = []
max_trans_list = []
testsiteinfo_list = [wafer_list,lot_list,mask_list,dierow_list,diecolumn_list,testsite_list]
testsite_attrib_list = ['Wafer','Batch','Maskset','DieRow','DieColumn','TestSite']
pddata_list = []
anal = ['DCM_LMZC','DCM_LMZO']
def run(path_input,show=False,save_fig=False,save_csv=False,wafer=False,file_input=None):
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
                'error_flag_TMW' : error_flag_IL_list,
                'error_description_TMW' : error_description_IL_list,
                'Analysis Wavelength': analy_list,
                'Rsq of Ref. spectrum (Nth)': IL_R2_list,
                'Max transmission of Ref. spec. (dB)' : max_trans_list,
                'error_flag_IV': error_flag_IV_list,
                'error_description_IV' : error_description_IV_list,
                'Rsq of IV' : Rsq_IV_list,
                'I at 1V[A]' : I_2,
                'I at -1V[A]' : I_1}

    if path_input == False:
        path = glob2.glob('.\data\**\*.xml')
    else:
        path = glob2.glob('{}'.format(path_input))
    if os.path.exists('./result'):
        shutil.rmtree('./result')
    ap = []
    if ',' in wafer:
        wafer = wafer.split(',')
    else:
        ap.append(wafer)
        wafer = ap
    path_list = []
    if wafer != ['all']:
        for i in path:
            for wafe in wafer:
                if wafe in i:
                    path_list.append(i)
    else:
        path_list = path

    file_list = []
    for i in path_list:
        if i.split('\\')[-1][-12:-4] in anal :
            file_list.append(i)
    file_num = len(file_list)

    start = time.time()

    for i in path_list:
        tree = elemTree.parse(i)
        testsiteinfo = list(tree.iter('TestSiteInfo'))[0]
        print(path_list[0])
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
            plt.subplot(234)
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
                error_flag_IV_list.append(1)
                error_description_IV_list.append('Rsq error')
            else:
                error_flag_IV_list.append(0)
                error_description_IV_list.append('No error')
            Wavelength = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep/L')
            IL = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep/IL')
            DCbias = tree.findall(
                'ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep')
            ILplot.find_DCbias(DCbias)
            max_trans_list.append(ILplot.max_trans(IL))
            plt.subplot(231)
            ILplot.IL_raw_plot(Wavelength,IL)

            plt.subplot(232)
            ILplot.IL_fitting_ref(Wavelength,IL,8)

            plt.subplot(233)
            ILplot.IL_processed_plot(Wavelength,IL,8)
            IL_R_2 =R_square.get_R2()
            IL_R2_list.append(IL_R_2)
            if IL_R_2 < 0.95:
                error_flag_IL_list.append(1)
                error_description_IL_list.append('Rsq error')
            else:
                error_flag_IL_list.append(0)
                error_description_IL_list.append('No error')

            if show == True:
                plt.show()

            if save_fig == False:

                if not os.path.exists('./result'):
                    os.makedirs('./result')
                if not os.path.exists('./result/figure'):
                    os.makedirs('./result/figure')
                if not os.path.exists('./result/figure/{}'.format(i.split('\\')[-4])):
                    os.makedirs('./result/figure/{}'.format(i.split('\\')[-4]))
                if not os.path.exists('./result/figure/{}/{}'.format(i.split('\\')[-4],i.split('\\')[-3])):
                    os.makedirs('./result/figure/{}/{}'.format(i.split('\\')[-4],i.split('\\')[-3]))
                if not os.path.exists('./result/figure/{}/{}/{}'.format(i.split('\\')[-4],i.split('\\')[-3],i.split('\\')[-2])):
                    os.makedirs('./result/figure/{}/{}/{}'.format(i.split('\\')[-4],i.split('\\')[-3],i.split('\\')[-2]))
                plt.savefig('./result/figure/{}/{}/{}/{}.png'.format(i.split('\\')[-4],i.split('\\')[-3],i.split('\\')[-2],filename), dpi=80)
            plt.close()
            if j < file_num :
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
            if not os.path.exists('./result'):
                os.makedirs('./result')
            if not os.path.exists('./result/csv'):
                os.makedirs('./result/csv')
            df.to_csv('./result/csv/analy_result.csv')

    print("time for processed :", round(time.time() - start),"s")
