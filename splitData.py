import os
import random
import shutil
from itertools import islice

outputFolderPath = "Dataset/SplitData"
inputFolderPath = "Dataset/all"
splitRadio = {"train":0.7,"val":0.2,"test":0.1}
classes = ["fake","real"]

try:
    shutil.rmtree(outputFolderPath)
    #print("Removed Directory")
except OSError as e:
    os.mkdir(outputFolderPath)

#------------Directories to create--------
os.makedirs(f"{outputFolderPath}/train/images",exist_ok=True)
os.makedirs(f"{outputFolderPath}/train/labels",exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/images",exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/labels",exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/images",exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/labels",exist_ok=True)



#------------get the name--------
listNames = os.listdir(inputFolderPath)
#print(listNames)
#print(len(listNames))
uniqueNames = []
for name in listNames:
    uniqueNames.append(name.split('.')[0])
uniqueNames = list(set(uniqueNames))
#print(len(uniqueNames))



#------------Shuffle--------
random.shuffle(uniqueNames)
#print(uniqueNames)


#------------find the number of images for each folder --------
lenData = len(uniqueNames)
#print(f'Total Images:{uniqueNames}')
#print(f'Total Images:{lenData}')
lenTrain = int(lenData*splitRadio['train'])
lenval = int(lenData*splitRadio['val'])
lenTest = int(lenData*splitRadio['test'])
#print(f'Total Images:{lenData} \nsplit: {lenTrain} {lenval} {lenTest}')


#------------put remanind images in training--------
if lenData != lenTrain+lenTest+lenval:
    remaining = lenData-(lenTrain+lenTest+lenval)
    lenTrain += remaining
#print(f'Total Images:{lenData} \nsplit: {lenTrain} {lenval} {lenTest}')


#------------split the list--------
lengthToSplit = [lenTrain,lenval, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input,elem))for elem in lengthToSplit]
#print(Output)
print(f'Total Images:{lenData} \nsplit: {len(Output[0])} {len(Output[1])} {len(Output[2])}')


#------------copy the files--------

sequence = ['train','val','test']
for i,out in enumerate(Output):
    for filename in out:
            shutil.copy(f'{inputFolderPath}/{filename}.jpg',f'{outputFolderPath}/{sequence[i]}/images/{filename}.jpg')
            shutil.copy(f'{inputFolderPath}/{filename}.txt',f'{outputFolderPath}/{sequence[i]}/labels/{filename}.txt')


print("split presses is completed ")


#------creating data.yaml file----

dataYaml = f'path: ../Data\n\
train: ../train/images\n\
val: ../val/images\n\
test: ../test/images\n\
\n\
nc: {len(classes)}\n\
names: {classes}'

f = open(f"{outputFolderPath}/data.yaml", 'a')
f.write(dataYaml)
f.close()

print("Data.yaml file created")
