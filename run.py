from flask import Flask,request,render_template,redirect,url_for
import json

app = Flask(__name__)

inputnote={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
note={0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B',12:'C',13:'C#',14:'D',15:'D#',16:'E',17:'F',18:'F#',19:'G',20:'G#',21:'A',22:'A#',23:'B',24:'C'}

@app.route("/scalefinder")
def scalefind():
    return render_template('scalefinder.html')

@app.route("/")
def firstpage():
    return render_template('home.html')

@app.route("/scalefind", methods=["GET", "POST"])
def findit():
  
  notes=[]
  finalnotes=[]

  notes.append(request.form['key'])
  notes.append(request.form['note2'])
  notes.append(request.form['note3'])
  notes.append(request.form['note4'])
  notes.append(request.form['note5'])
  notes.append(request.form['note6'])
  notes.append(request.form['note7'])
  notes.append(request.form['note8'])
  notes.append(request.form['note9'])
  notes.append(request.form['note10'])
  notes.append(request.form['note11'])
  
  for i in notes:
      if i!='0':
          finalnotes.append(i)
  print('Entered Notes: ',finalnotes)


  with open('Ignore/scales.json') as f:
      data = json.load(f),

  root=finalnotes[0]
  print(data[0][233]['name'])
  for i in data[0][233]['notes']:
      print(i+inputnote[root],':',note[i+inputnote[root]])


  return redirect("scalefinder") 

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=True)
