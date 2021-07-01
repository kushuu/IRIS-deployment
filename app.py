from flask import Flask, render_template, url_for, request, flash
from flask.helpers import flash
import pickle
import sklearn
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = b'_12345#y2L"F4Q8z\n\xec]/'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    sl = request.form.get('sepal_length')
    sw = request.form.get('sepal_width')
    pl = request.form.get('petal_length')
    pw = request.form.get('petal_width')

    if(sl == "" or sw == "" or pl == "" or pw == ""):
        flash("Please fill all the fields.")
        return redirect(url_for('index'))

    model = pickle.load(open('classifier.sav', 'rb'))
    class_ = model.predict([[float(sl), float(sw), float(pl), float(pw)]])

    return render_template('result.html', class_ = str(class_)[2:-2].capitalize())


app.run()