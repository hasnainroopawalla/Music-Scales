from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def firstpage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=9000, debug=True)