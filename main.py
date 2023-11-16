from flask import Flask, request, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('principal.html')

@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3)/3
        if asistencia >= 75 and promedio >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        return render_template('formulario1.html', promedio=promedio, estado=estado)
    return render_template('formulario1.html')

@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = []
        nombres.append(nombre1)
        nombres.append(nombre2)
        nombres.append(nombre3)
        if nombre1 == nombre2:
            error = "ERROR! Deben ser nombres diferentes."
            return render_template ('formulario2.html', error=error)
        elif nombre1 == nombre3:
            error = "ERROR! Deben ser nombres diferentes."
            return render_template('formulario2.html', error=error)
        elif nombre2 == nombre3:
            error = "ERROR! Deben ser nombres diferentes."
            return render_template('formulario2.html', error=error)
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template ('formulario2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
    return render_template('formulario2.html')

if __name__ == '__main__':
    app.run(debug=True)