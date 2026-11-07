from joblib import load
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
clf = load("model/model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method=="POST":
    hasil_prediksi = clf.predict([[
      float(request.form['palo']),
      float(request.form['lelo']),
      float(request.form['pako']),
      float(request.form['leko'])
    ]])
    
    return render_template("index.html", hasil = hasil_prediksi[0])

  else:
    return render_template("index.html")

@app.route('/modeling')
def modeling():
  return render_template("modeling.html")
