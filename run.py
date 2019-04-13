from flask import Flask,request,render_template,redirect,url_for
import json

app = Flask(__name__)

filteredscales=[]
finalnotes=[]
inputnote={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
note={0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B',12:'C',13:'C#',14:'D',15:'D#',16:'E',17:'F',18:'F#',19:'G',20:'G#',21:'A',22:'A#',23:'B',24:'C'}

@app.route("/scalefinder")
def scalefind():
    global filteredscales
    global finalnotes
    print(filteredscales)
    return render_template('scalefinder.html',filteredscales=filteredscales,finalnotes=finalnotes)

@app.route("/")
def firstpage():
    return render_template('home.html')

@app.route("/scalefind", methods=["GET", "POST"])
def findit():

  global filteredscales
  global finalnotes
  filteredscales=[]
  notes=[]
  finalnotes=[]

  clickednotes=request.get_json()
  for i in clickednotes['clickednotes']:
      finalnotes.append(i)
  print('f',finalnotes)
  with open('Static/dataset/scales.json') as f:
      data = json.load(f),

  allscalekey=[]

  for i in data[0]:
     scalekey=[]
     scaledict={}
     scaledict['name']=i['name']
     scaledict['notes']=i['notes']
     allscalekey.append(scaledict)
  

  for i in range(0,len(allscalekey)):
     temp=[]
     for j in allscalekey[i]['notes']:
         temp.append(note[j+inputnote[finalnotes[0]]])
     allscalekey[i]['notes']=temp
  #print(allscalekey)
    

  for i in range(0,len(allscalekey)):
     if set(finalnotes).issubset(allscalekey[i]['notes']):
         filteredscales.append(allscalekey[i])
        
  #print('Filtered: ',filteredscales)


  return redirect("scalefinder") 

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=True)
