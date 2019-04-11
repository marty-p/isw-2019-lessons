# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:57:40 2019

@author: Studente
"""

#https://finance.yahoo.com/quote/BTC-USD/history?period1=1428703200&period2=1428703200&interval=1d&filter=history&frequency=1d
#Time Period:
#Apr 11, 2015 - Apr 11, 2015
#Show:Historical PricesFrequency:Daily

import pandas as pd

path = r"C:\Users\Studente\Desktop\isw\lezione06\\"
filename = path+"BTC-USD.csv"

#opening csv file
dataset = pd.read_csv(filename, sep=',')

#iloc selection, only numbers accepted
set_1 = dataset.iloc[:,3:]

set_2 = dataset.iloc[:500, :3]

set_3 = dataset.loc[:, 'Close'] #pandas series

#conversion from pandas series to numpy array
np_set_3 = set_3.values

#in the loc selection the last index is included
set_4 = dataset.loc[:500, ['Close', 'Open', 'Volume']]

#how to create a new pandas column

import numpy as np
dataset['new'] = np.random.randint(0,10,dataset.shape[0])

#how to drop a column
dataset.drop(['new','new_check'], axis=1, inplace=True)
#or
#dataset.drop('new', axis=1, inplace=True)

#selection with conditions
#creating new column
dataset['new_check'] = np.random.choice([True,False],dataset.shape[6])

#dataset['Check'] =0
#for i in range(0,dataset.shape[0])
new_dataset = dataset.loc[dataset['Check'] == True, [col for in dataset.columns if xxx]]
new_dataset = dataset.loc[dataset['Check'] == True, :]

data = pd.DataFrame({
        'Students':[
            'Joe',
            'Russel',
            'Craig',
            'Jow',
            'Joe',
            'Craig',
            'Joe',
            'Russel',
            'Craig'],
        'Scores': [
                25.6,
                28.1,
                32.6,
                22.3,
                21.5,
                29.5,
                32.6,
                37.6,
                27.4,
        ]
        })


#grouping by students and taking average
data.groupby(['Students'], as_index=False).mean()

# to datetime method
type(dataset['Date'][0])
dataset['Date'] = pd.to_datetime(dataset['Date'])

#only data - from pandas TimeStamp to datetime.date object conversion
dataset['Date'] = pd.to_datetime(dataset['Date']).dt_date
#check
type(dataset['Date'][0])

