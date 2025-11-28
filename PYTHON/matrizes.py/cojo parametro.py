from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    nombre = request.args.get("nombre")
    print(nombre)
    return "Mira en la consola si ha pasado algo"
if __name__ == "__main__":
    app.run(debug=True)

