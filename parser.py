import json

inputnote={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
note={0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B',12:'C',13:'C#',14:'D',15:'D#',16:'E',17:'F',18:'F#',19:'G',20:'G#',21:'A',22:'A#',23:'B',24:'C'}
with open('Static/dataset/scales.json') as f:
    data = json.load(f),

#root=input('Enter root: ')
finalnotes=['G#','A#',"C","D","B"]
allscalekey=[]

#print(data[0][233]['name'])

for i in data[0]:
    scalekey=[]
    for j in i['notes']:
        scalekey.append(note[j+inputnote[finalnotes[0]]])
        #print(note[j+inputnote[finalnotes[0]]])
    allscalekey.append(scalekey)   

print(allscalekey)
    
##for i in data[0][233]['notes']:
##    print(i+inputnote[root],':',note[i+inputnote[root]])
