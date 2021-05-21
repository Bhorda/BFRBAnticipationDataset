import numpy as np
import pandas as ps
import math
import sys
import random

### Negative windows

# prediction window and labeled window length in seconds
directory = sys.argv[1]
xSize = int(sys.argv[2]) # xwindow size
ySize = int(sys.argv[3]) # ywindow size
uID = sys.argv[4] # participant ID
norm = sys.argv[5] # normalisation type: zscore/minmax

timecodes = ps.read_csv(directory + 'timestamps.csv')

startRecording = int(timecodes['start'][0])
endRecording = int(timecodes['end'][0])

listStart = timecodes['start'][1:].tolist()
listEnd = timecodes['end'][1:].tolist()
listHand = timecodes['hand'][1:].tolist()
listLabel = timecodes['label'][1:].tolist()
listStage = timecodes['stage'][1:].tolist()

for i in range(0,len(listStart)):
    listStart[i] = int(startRecording + math.floor(listStart[i])*60*1000 + (listStart[i] - math.floor(listStart[i]))*100*1000)
    listEnd[i] = int(startRecording + math.floor(listEnd[i])*60*1000 + (listEnd[i] - math.floor(listEnd[i]))*100*1000)

dfTimestamps = ps.DataFrame(list(zip(listStart,listEnd,listHand,listLabel,listStage)), columns=['start','end','hand','label','stage'])
dfTimestamps = dfTimestamps.replace(np.nan,'',regex=True)
dfTimestamps = dfTimestamps.loc[(dfTimestamps['label'] != '')]

def GenerateNegativeWindows():
    sensorDataAcc = ps.read_csv(directory + f'acc{norm}.csv')
    sensorDataGyr = ps.read_csv(directory + f'gyr{norm}.csv')
    sensorDataHrm = ps.read_csv(directory + f'hrm{norm}.csv')
    sensorDataPpg = ps.read_csv(directory + 'ppgLabeled.csv') # ppg processed separately
    window = ps.DataFrame()

    for i in range(0,len(dfTimestamps)):
        check = True
        wIndex = i + 1
        while check:
            mark = random.randrange(startRecording/1000,endRecording/1000,1) * 1000
            # print(mark)
            if mark < startRecording + xSize * 1000:
                continue

            for j in dfTimestamps.itertuples():
                if mark > j[1] and mark < j[2]:
                    # print('during behaviour period ' + str(wIndex) + ' ')
                    break
                elif mark + ySize * 1000 > j[1] and mark + ySize * 1000 < j[2]:
                    # print('behaviour overlap ' + str(wIndex) + ' ' + str(j[1]))
                    break
                
                check = False

        window = sensorDataAcc.loc[(sensorDataAcc['timestamp'] >= mark - xSize * 1000) & (sensorDataAcc['timestamp'] <= mark + ySize * 1000)]
        window.drop('hand',axis=1,inplace=True)
        window.to_csv(f'{directory}windows/{uID}_acc_-_{wIndex}.csv', index=False)
        # print('acc windows generated')
        window = sensorDataGyr.loc[(sensorDataGyr['timestamp'] >= mark - xSize * 1000) & (sensorDataGyr['timestamp'] <= mark + ySize * 1000)]
        window.drop('hand',axis=1,inplace=True)
        window.to_csv(f'{directory}windows/{uID}_gyr_-_{wIndex}.csv', index=False)
        # print('gyr windows generated')
        window = sensorDataHrm.loc[(sensorDataHrm['timestamp'] >= mark - xSize * 1000) & (sensorDataHrm['timestamp'] <= mark + ySize * 1000)]
        window.drop('hand',axis=1,inplace=True)
        window.to_csv(f'{directory}windows/{uID}_hrm_-_{wIndex}.csv', index=False)
        # print('hrm windows generated')

        # window = sensorDataPpg.loc[(sensorDataPpg['timestamp'] >= mark - xSize * 1000) & (sensorDataPpg['timestamp'] <= mark + ySize * 1000)]
        # window.drop('hand',axis=1,inplace=True)
        # window.to_csv(f'{directory}windows/P{uID}_ppg_{wIndex}_-_.csv', index=False)

GenerateNegativeWindows()
# # generate positive and negative windows of length
# def GeneratePositiveWindows(sensorType):
#     sensorData = ps.read_csv(directory + sensorType + 'Labeled.csv')
#     window = ps.DataFrame()
#     wIndex = 1
#     lastTuple = (listStart[0],listEnd[0])

#     for i in dfTimestamps.itertuples():
#         if i[1] - xSize * 1000 < startRecording or i[4] == -1:
#             continue
        
#         # If behaviour not as long as y window
#         # if i[2]-i[1] < ySize * 1000:
#         #     continue
#         window = sensorData.loc[(sensorData['timestamp'] >= i[1] - xSize * 1000) & (sensorData['timestamp'] <= i[2] + ySize * 1000)]

#         print(i)
#         if i[1] - lastTuple[1] > xSize * 1000:
#             # window.to_csv(directory + sensorType + 'Window' + '_' + str(wIndex) + '_' + str(i[4]) + '_clean' + '.csv', index=False)
#             window.to_csv(f'{directory}{sensorType}Window_{wIndex}_{i[4]}_clean.csv', index=False)
#         else:
#             # window.to_csv(directory + sensorType + 'Window' + '_' + str(wIndex) + '_' + str(i[4]) + '_dirty' + '.csv', index=False)
#             window.to_csv(f'{directory}{sensorType}Window_{wIndex}_{i[4]}_dirty.csv', index=False)
#         wIndex += 1
# # f'Window_{wIndex}_{i[4]}_clean.csv'
# GeneratePositiveWindows('acc')