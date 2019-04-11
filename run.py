from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

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

  print(finalnotes)

  return redirect("scalefinder") 

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=True)
