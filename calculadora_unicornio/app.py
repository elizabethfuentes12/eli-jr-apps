from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = ""
    if request.method == 'POST':
        numero1 = float(request.form.get('numero1', 0))
        numero2 = float(request.form.get('numero2', 0))
        operacion = request.form.get('operacion')
        
        if operacion == 'suma':
            resultado = numero1 + numero2
        elif operacion == 'resta':
            resultado = numero1 - numero2
        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2
        elif operacion == 'division':
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = "¡No se puede dividir por cero!"
    
    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
