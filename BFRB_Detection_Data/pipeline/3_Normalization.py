import pandas as ps
import numpy as np
import sys

Directory = sys.argv[1]
NormalizationType = sys.argv[2:]
Sensors = ('acc','gyr','hrm')
# data = ps.read_csv(f'{Directory}accLabelled.csv')

def Zscore():
    for sensor in Sensors:
        data = ps.read_csv(f'{Directory}{sensor}Labeled.csv')

        RestPeriods = data.loc[(data['stage'] == 1) | (data['stage'] == 4) | (data['stage'] == 6)]
        # RestPeriods = data.loc[(data['stage'] == 1)]
        RestFeatures = RestPeriods.describe()


        for col in data.keys():
            if 'label' in col or 'stage' in col or 'hand' in col or 'timestamp' in col:
                continue
            col_zscore = col + '_zscore'
            data[col_zscore] = (data[col] - RestFeatures[col].mean())/RestFeatures[col].std(ddof=0)
            data[col] = data[col_zscore]
            data.drop(col_zscore, axis = 1, inplace = True)

        data.to_csv(f'{Directory}{sensor}Zscore.csv', index = False)

def MinMax():
    for sensor in Sensors:
        data = ps.read_csv(f'{Directory}{sensor}Labeled.csv')
        for col in data.keys():
            if 'label' in col or 'stage' in col or 'hand' in col or 'timestamp' in col:
                continue
            col_minmax = col + '_minmax'
            data[col_minmax] = (data[col] - data[col].min())/(data[col].max() - data[col].min())
            data[col] = data[col_minmax]
            data.drop(col_minmax, axis = 1, inplace = True)

        data.to_csv(f'{Directory}{sensor}MinMax.csv', index = False)

if 'zscore' in NormalizationType:
    Zscore()
if 'minmax' in NormalizationType:
    MinMax()