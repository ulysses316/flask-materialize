from flask import Flask,render_template
from flask_material import Material
from flask import request

import forms

app = Flask(__name__)
Material(app)

@app.route('/')
def index():
    return render_template('index.html')
# =============== BISECCION BEGIN =====================
@app.route('/biseccion', methods = ['GET', 'POST'])
def biseccion():
    fbiseccion = forms.FormularioBiseccion(request.form)
    print 'pryeba'
    print fbiseccion.data
    if request.method == 'POST':
        print fbiseccion.xi.data
        print fbiseccion.xs.data
        print fbiseccion.error.data
    return render_template('biseccion.html', form = fbiseccion)
        # xistring = fbiseccion.xi.data
        # xstring = fbiseccion.xs.data
        # errorstring =  fbiseccion.error.data
        # xi = int(xistring)
        # xs = int(xstring)
        # error = int(errorstring)

        # def poli(x):
        #     y=pow(x,2)-(3*x)-4
        #     return(y)
        #     #Programa principal
        # xa = (xi+xs)/2.0
        # while (abs(poli(xa)) > error):
        #     xa = (xi+xs)/2.0
        #     if poli(xi)*poli(xa) < 0.00:
        #         xs=xa
        #         signo="negativo"
        #         limite="superior"
        #     else:
        #         xs=xa
        #         signo="positivo"
        #         limite="inferior"
        #         print(xa)



# =============== BISECCION END =====================

@app.route('/newton', methods = ['GET', 'POST'])
def newton():
    return render_template('newton.html')

@app.route('/newton2', methods = ['GET', 'POST'])
def newton2():
    return render_template('newton2.html')

# @app.route('/paralelas')
# def paralelas():
#     return render_template('index.html')

@app.route('/gauss', methods = ['GET', 'POST'])
def gauss():
    return render_template('gauss.html')

@app.route('/gauss2', methods = ['GET', 'POST'])
def gauss2():
    return render_template('gauss2.html')

# @app.route('/mobile')
# def mobile():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
