from flask import Flask,render_template
from flask_material import Material
from flask import request

app = Flask(__name__)
Material(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biseccion')
def biseccion():
    return render_template('biseccion.html')

@app.route('/newton')
def newton():
    return render_template('index.html')

@app.route('/newton2')
def newton2():
    return render_template('index.html')

@app.route('/paralelas')
def paralelas():
    return render_template('index.html')

@app.route('/gauss')
def gauss():
    return render_template('index.html')

@app.route('/gauss2')
def gauss2():
    return render_template('index.html')

@app.route('/mobile')
def mobile():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
