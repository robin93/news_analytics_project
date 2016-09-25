# # Check Current Working Directory
# import os
# os.getcwd()

# # Set Current Working Directory
# os.chdir('D:\\PGDBA\\IIM C Sem 3\\HFF Project\\Equity Data')

import pandas as pd
import csv as csv
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import math

# cwd = os.getcwd()

#Log returns for Equity
ACC = pd.read_csv("/home/robin/Desktop/hff_project/Data/Price_Data_by_equity/ChennaiPetro_in.csv",header=0,sep=",")
ACC['Date_new'] = pd.to_datetime(ACC['Date'] , format='%d/%m/%y %H:%M')
ACC2 = ACC.set_index('Date_new')
ACC2 = ACC2.between_time('9:07','15:30')

ACC2['log_ret'] = np.log(ACC2.LAST_PRICE) - np.log(ACC2.LAST_PRICE.shift(1))

# Log returns for SENSEX
SENSEX = pd.read_csv("/home/robin/Desktop/hff_project/SENSEX.csv",header=0,sep=",")
SENSEX['Date_new'] = pd.to_datetime(SENSEX['Date'] , format='%m/%d/%Y %H:%M')
SENSEX2 = SENSEX.set_index('Date_new')
SENSEX2 = SENSEX2.between_time('9:07','15:30')

SENSEX2['log_ret'] = np.log(SENSEX2.LAST_PRICE) - np.log(SENSEX2.LAST_PRICE.shift(1))

#SENSEX2.log_ret['2016-09-22 13:27:00']
#SENSEX2.index.get_loc('2016-09-22 13:27:00')
#SENSEX2.log_ret[49377:49379].sum()

# Events file
Event = pd.read_csv("/home/robin/Desktop/hff_project/Data/meta_csv_files/ChennaiPetroleum_meta.csv",header=None,sep=",")
Event.columns = ['date']
Event['date2']= pd.to_datetime(Event['date'] , format='%d %B %Y %H:%M')
#Event.date2[1]
#i = np.argmin(np.abs(ACC2.index.to_pydatetime() - Event.date2[1]))

beta = 0.71
def CAR(before, after, time):
    acc_ix = np.argmin(np.abs(ACC2.index.to_pydatetime() - time))
    sen_ix = np.argmin(np.abs(SENSEX2.index.to_pydatetime() - time))
#    sen_ix=SENSEX2.index.get_loc(time)
#    acc_ix=ACC2.index.get_loc(time)
    
    Ret = math.exp(ACC2.log_ret[acc_ix - before : acc_ix + after + 1].sum()) - 1
    mar_ret = math.exp(SENSEX2.log_ret[sen_ix - before : sen_ix + after + 1].sum()) - 1
    
    CAR = Ret - (beta * mar_ret)
    
    return CAR

print CAR(2,3,Event.date2[1])

Event['CAR_2_3'] = Event.date2.apply(lambda s: CAR(2,3,s))

#'2016-08-31 13:20:00')

print Event

(Event['CAR_2_3']).to_csv("/home/robin/Desktop/hff_project/Data/car_output_files/ChennaiPetroleum_car.csv")
