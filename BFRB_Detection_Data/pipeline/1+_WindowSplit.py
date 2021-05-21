import numpy as np
import pandas as ps
import math
import sys

### Positive windows

# prediction window and labeled window length in seconds
directory = sys.argv[1]
xSize = int(sys.argv[2]) # xwindow size
ySize = int(sys.argv[3]) # ywindow size
uID = sys.argv[4] # participant ID
norm = sys.argv[5] # normalisation type: zscore/minmax

timecodes = ps.read_csv(f'{directory}timestamps.csv')

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

# generate positive and negative windows of length
def GeneratePositiveWindows(sensorType):
    if 'ppg' in sensorType:
        sensorData = ps.read_csv(f'{directory}{sensorType}Labeled.csv')
    else:
        sensorData = ps.read_csv(f'{directory}{sensorType}{norm}.csv')
    window = ps.DataFrame()
    wIndex = 1
    lastTuple = (listStart[0],listEnd[0])

    for i in dfTimestamps.itertuples():
        if i[4] == '' or i[1] - xSize * 1000 < startRecording or i[5] == 7:
            continue

        

        window = sensorData.loc[(sensorData['timestamp'] >= i[1] - xSize * 1000) & (sensorData['timestamp'] <= i[1] + ySize * 1000)]
        window.drop('hand',axis=1,inplace=True)

        behaviour = BehaviourSelect(i[4])

        window.to_csv(f'{directory}windows/{uID}_{sensorType}_+_{wIndex}_{behaviour}.csv', index=False)

        wIndex += 1

def BehaviourSelect(behaviourName):
    if behaviourName == 'skin picking':
        return 1
    elif behaviourName == 'face touching':
        return 2
    elif behaviourName == 'fidgeting':
        return 3
    elif behaviourName == 'skin biting':
        return 4
    elif behaviourName == 'hand scratching':
        return 5
    elif behaviourName == 'leg scratching':
        return 6
    elif behaviourName == 'nail biting':
        return 7

GeneratePositiveWindows('acc')

GeneratePositiveWindows('gyr')

GeneratePositiveWindows('hrm')

GeneratePositiveWindows('ppg')
