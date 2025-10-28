from flask import Flask, request, jsonify

app = Flask(__name__)

def _to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

@app.route('/sumar')
def sumar():
    a = _to_float(request.args.get('a'))
    b = _to_float(request.args.get('b'))
    return jsonify(resultado=a + b)

@app.route('/restar')
def restar():
    a = _to_float(request.args.get('a'))
    b = _to_float(request.args.get('b'))
    return jsonify(resultado=a - b)

@app.route('/multiplicar')
def multiplicar():
    a = _to_float(request.args.get('a'))
    b = _to_float(request.args.get('b'))
    return jsonify(resultado=a * b)

@app.route('/dividir')
def dividir():
    a = _to_float(request.args.get('a'))
    b = _to_float(request.args.get('b'))
    if b == 0:
        return jsonify(error="No se puede dividir entre cero"), 400
    return jsonify(resultado=a / b)

if __name__ == '__main__':
    app.run(debug=True)
