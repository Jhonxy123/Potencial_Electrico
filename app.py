from flask import Flask, render_template, request

app = Flask(__name__)

# Constantes
k = 8.99e9      # Nm²/C²
q = 8e-9        # 8 nC

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            R = float(request.form['R'])
            r = float(request.form['r'])
            unidad_R = request.form['unidad_R']
            unidad_r = request.form['unidad_r']

            # Convertir a metros si está en cm
            if unidad_R == 'cm':
                R /= 100
            if unidad_r == 'cm':
                r /= 100

            if r < R:
                V = (k * q) / R
                caso = "dentro de la esfera"
            else:
                V = (k * q) / r
                caso = "fuera de la esfera"

            resultado = {
                'R': round(R, 4),
                'r': round(r, 4),
                'V': round(V, 4),
                'caso': caso
            }

        except ValueError:
            resultado = {'error': 'Ingresa valores numéricos válidos.'}

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
