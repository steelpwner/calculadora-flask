from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    return "<h1>Hello world</h1>"

@app.route("/calculadora",methods=["GET"])
def calculadora():
    return render_template("calculadora.html")

@app.route("/calculadora",methods=["POST"])
def calculo():
    args = request.form
    n1 = args['n1']
    n2 = args['n2']
    operacion = args['operacion']
    return render_template("calculadora.html",resultado=calcular_operacion(n1,n2,operacion))

def calcular_operacion(n1,n2,operacion):
    resultado = "Resultado: "
    if verificar_numero(n1) and verificar_numero(n2):
        n1 = float(n1)
        n2 = float(n2)
        if operacion == "+":
            resultado += str(n1+n2)
        elif operacion == "-":
            resultado += str(n1-n2)
        elif operacion == "*":
            resultado += str(n1*n2)
        elif operacion == "/":
            if n2 != 0:
                resultado += str(n1/n2)
            else:
                resultado = "Error, no se puede dividir entre cero"
        else:
            resultado = "Operación inválida"
    else:
        resultado = "Error en digitación de números"
    return resultado

def verificar_numero(x):
    try:
        float(x)
        return True
    except:
        return False

app.run(port=5000,host="0.0.0.0",debug=True)