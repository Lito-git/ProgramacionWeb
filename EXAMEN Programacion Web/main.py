from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    calculo_de_compra = {}

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        total_compra = tarros * 9000

        if 18 <= edad <= 30:
            descuento_de_compra = total_compra * 0.15

        elif edad > 30:
            descuento_de_compra = total_compra * 0.25

        else:
            descuento_de_compra = 0

        valor_total_final = total_compra - descuento_de_compra

        calculo_de_compra = {
            "Nombre": nombre,
            "Total_de_compra": total_compra,
            "Descuento_aplicado": descuento_de_compra,
            "Valor_total_final": valor_total_final
        }

    return render_template("Ejercicio1.html", calculo=calculo_de_compra)



app.config['SECRET_KEY'] = "clave_secreta"

users = {
    "juan" : "admin",
    "pepe" : "user"
}

@app.route("/Ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = ""
    if request.method == "POST":
        user = request.form.get("user")
        contrasena = request.form.get("contrasena")

        if user in users and users[user] == contrasena:
            if user == "juan":
                mensaje = f"Bienvenido administrador {user}"

            elif user == "pepe":
                mensaje = f"Bienvenido usuario {user}"

        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("Ejercicio2.html", mensaje=mensaje)



if __name__ == "__main__":
    app.run(debug=True)
