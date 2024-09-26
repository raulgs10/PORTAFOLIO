from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        bio = request.form['bio']
        imagen = request.files['imagen']
        imagen_filename = imagen.filename
        imagen_path = os.path.join(app.config['UPLOAD_FOLDER'], imagen_filename)
        imagen.save(imagen_path)
        
        # Guardar la información en un archivo de datos (ejemplo simple)
        with open('data.txt', 'w') as file:
            file.write(f"{nombre}\n{bio}\n{imagen_filename}\n")

    # Leer el registro más reciente
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                nombre = lines[0].strip()
                bio = lines[1].strip()
                imagen = lines[2].strip()
            else:
                nombre = bio = imagen = None
    else:
        nombre = bio = imagen = None

    return render_template('index.html', nombre=nombre, bio=bio, imagen=imagen, year=2024)

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Actualizar el archivo de datos
    if os.path.exists('data.txt'):
        with open('data.txt', 'w') as file:
            file.write("")  # Vaciar el archivo de datos

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

