
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/Ejercicio1", methods = ["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        notas = [nota1, nota2, nota3]
        promedio_notas = round(sum(notas)/len(notas), 2)

        if promedio_notas >= 40 and asistencia >= 75:
            estado_asig = "Aprobado"

        else:
            estado_asig = "Reprobado"

        return render_template("Ejercicio1.html", promNotas = promedio_notas, estadoAsig = estado_asig)

    return render_template("Ejercicio1.html")


@app.route("/Ejercicio2", methods = ["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        nombres = [nombre1, nombre2, nombre3]
        nom_mas_largo = max(nombres, key = len)

        return render_template("Ejercicio2.html", resNom = nom_mas_largo, cantCaracteres = len(nom_mas_largo))

    return render_template("Ejercicio2.html")


if __name__ == "__main__":
    app.run(debug = True)