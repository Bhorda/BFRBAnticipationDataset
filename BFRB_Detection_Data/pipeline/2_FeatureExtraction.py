# Extract basic descriptive features from the raw data

import numpy as np
import pandas as ps
import sys
import os

Directory = sys.argv[1] + 'windows/'
# NumberOfWindows = int(sys.argv[2])

fileList = os.listdir(Directory)


f = open(f'{Directory}WindowFeatures.csv','w')
f.write('uID,label,accXmean,accXstd,accXmin,accXmax,accYmean,accYstd,accYmin,accYmax,accZmean,accZstd,accZmin,accZmax,gyrXmean,gyrXstd,gyrXmin,gyrXmax,gyrYmean,gyrYstd,gyrYmin,gyrYmax,gyrZmean,gyrZstd,gyrZmin,gyrZmax,hrvmean,hrvstd,hrvmin,hrvmax\n')

def ExtractFeature():
    NoGen = 0
    NotComplete = False
    for i in range(0,100):
        try:
            accFile = f'acc_+_{i+1}'
            gyrFile = f'gyr_+_{i+1}'
            hrmFile = f'hrm_+_{i+1}'
            for i in range(0,len(fileList)):
                # if fileList[i].endswith(str(accFile)):
                #     accFile = fileList[i]
                #     NotComplete = True
                # if fileList[i].endswith(str(gyrFile)):
                #     gyrFile = fileList[i]
                # if fileList[i].endswith(str(hrmFile)):
                #     hrmFile = fileList[i]
                if (accFile in fileList[i]) and ('.icloud' not in fileList[i]):
                    accFile = fileList[i]
                    NotComplete = True
                if (gyrFile in fileList[i]) and ('.icloud' not in fileList[i]):
                    gyrFile = fileList[i]
                if (hrmFile in fileList[i]) and ('.icloud' not in fileList[i]):
                    hrmFile = fileList[i]

            if not NotComplete:
                break
            
            elements = accFile.split('_')
            behaviour = elements[4].split('.')[0]
            print(elements)

            behaviourType = BehaviourSelect(accFile)
            window = ps.read_csv(Directory + accFile)
            windowDesc = window.describe()
            # string = str(windowDesc['stage']['mean']) + ',' + str(behaviourType) + ',' +  str(windowDesc['x']['mean']) + ',' + str(windowDesc['x']['std']) + ',' + str(windowDesc['x']['min']) + ',' + str(windowDesc['x']['max']) + ',' + str(windowDesc['y']['mean']) + ',' + str(windowDesc['y']['std']) + ',' + str(windowDesc['y']['min']) + ',' + str(windowDesc['y']['max']) + ',' + str(windowDesc['z']['mean']) + ',' + str(windowDesc['z']['std']) + ',' + str(windowDesc['z']['min']) + ',' + str(windowDesc['z']['max']) + ','
            # string =  elements[0] + ',' + behaviour + ',' +  str(windowDesc['x']['mean']) + ',' + str(windowDesc['x']['std']) + ',' + str(windowDesc['x']['min']) + ',' + str(windowDesc['x']['max']) + ',' + str(windowDesc['y']['mean']) + ',' + str(windowDesc['y']['std']) + ',' + str(windowDesc['y']['min']) + ',' + str(windowDesc['y']['max']) + ',' + str(windowDesc['z']['mean']) + ',' + str(windowDesc['z']['std']) + ',' + str(windowDesc['z']['min']) + ',' + str(windowDesc['z']['max']) + ','
            string =  elements[0] + ',' + '1' + ',' +  str(windowDesc['x']['mean']) + ',' + str(windowDesc['x']['std']) + ',' + str(windowDesc['x']['min']) + ',' + str(windowDesc['x']['max']) + ',' + str(windowDesc['y']['mean']) + ',' + str(windowDesc['y']['std']) + ',' + str(windowDesc['y']['min']) + ',' + str(windowDesc['y']['max']) + ',' + str(windowDesc['z']['mean']) + ',' + str(windowDesc['z']['std']) + ',' + str(windowDesc['z']['min']) + ',' + str(windowDesc['z']['max']) + ','

            f.write(string)

            window = ps.read_csv(Directory + gyrFile)
            windowDesc = window.describe()
            string = str(windowDesc['x']['mean']) + ',' + str(windowDesc['x']['std']) + ',' + str(windowDesc['x']['min']) + ',' + str(windowDesc['x']['max']) + ',' + str(windowDesc['y']['mean']) + ',' + str(windowDesc['y']['std']) + ',' + str(windowDesc['y']['min']) + ',' + str(windowDesc['y']['max']) + ',' + str(windowDesc['z']['mean']) + ',' + str(windowDesc['z']['std']) + ',' + str(windowDesc['z']['min']) + ',' + str(windowDesc['z']['max']) + ','

            f.write(string)

            window = ps.read_csv(Directory + hrmFile)
            windowDesc = window.describe()
            string = str(windowDesc['hrv']['mean']) + ',' + str(windowDesc['hrv']['std']) + ',' + str(windowDesc['hrv']['min']) + ',' + str(windowDesc['hrv']['max']) + '\n'

            f.write(string)
            NoGen = NoGen + 1
            NotComplete = False
        except:
            print(accFile)
            print(gyrFile)
            print(hrmFile)

    for i in range(0,NoGen):
        try:
            accFile = f'acc_-_{i+1}'
            gyrFile = f'gyr_-_{i+1}'
            hrmFile = f'hrm_-_{i+1}'
            for i in range(0,len(fileList)):
                # if fileList[i].endswith(str(accFile)):
                #     accFile = fileList[i]
                # if fileList[i].endswith(str(gyrFile)):
                #     gyrFile = fileList[i]
                # if fileList[i].endswith(str(hrmFile)):
                #     hrmFile = fileList[i]
                if (accFile in fileList[i]) and ('.icloud' not in fileList[i]):
                    accFile = fileList[i]
                    NotComplete = True
                if (gyrFile in fileList[i]) and ('.icloud' not in fileList[i]):
                    gyrFile = fileList[i]
                if (hrmFile in fileList[i]) and ('.icloud' not in fileList[i]):
                    hrmFile = fileList[i]

            elements = accFile.split('_')
            print(elements)

            window = ps.read_csv(Directory + accFile)
            windowDesc = window.describe()
            string = elements[0] + ',' + '0' + ',' +  str(windowDesc['x']['mean']) + ',' + str(windowDesc['x']['std']) + ',' + str(windowDesc['x']['min']) + ',' + str(windowDesc['x']['max']) + ',' + str(windowDesc['y']['mean']) + ',' + str(windowDesc['y']['std']) + ',' + str(windowDesc['y']['min']) + ',' + str(windowDesc['y']['max']) + ',' + str(windowDesc['z']['mean']) + ',' + str(windowDesc['z']['std']) + ',' + str(windowDesc['z']['min']) + ',' + str(windowDesc['z']['max']) + ','
            
            f.write(string)

            window = ps.read_csv(Directory + gyrFile)
            windowDesc = window.describe()
            string = str(windowDesc['x']['mean']) + ',' + str(windowDesc['x']['std']) + ',' + str(windowDesc['x']['min']) + ',' + str(windowDesc['x']['max']) + ',' + str(windowDesc['y']['mean']) + ',' + str(windowDesc['y']['std']) + ',' + str(windowDesc['y']['min']) + ',' + str(windowDesc['y']['max']) + ',' + str(windowDesc['z']['mean']) + ',' + str(windowDesc['z']['std']) + ',' + str(windowDesc['z']['min']) + ',' + str(windowDesc['z']['max']) + ','
            
            f.write(string)

            window = ps.read_csv(Directory + hrmFile)
            windowDesc = window.describe()
            string = str(windowDesc['hrv']['mean']) + ',' + str(windowDesc['hrv']['std']) + ',' + str(windowDesc['hrv']['min']) + ',' + str(windowDesc['hrv']['max']) + '\n'
            
            f.write(string)
        except:
            print(accFile)
            print(gyrFile)
            print(hrmFile)

def BehaviourSelect(filename):
    if  'face touching' in filename:
        return 1
    if 'skin picking' in filename:
        return 2
    if 'hand scratching' in filename:
        return 3
    if 'skin biting' in filename:
        return 4
    if 'fidgeting' in filename:
        return 5
    if 'nail biting' in filename:
        return 6

ExtractFeature()
f.close()