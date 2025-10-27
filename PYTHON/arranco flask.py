from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return "Esto es HTML desde Flask"

# Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)