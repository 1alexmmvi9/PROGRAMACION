from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inincio():
    mis_frutas = ["manzanas","platanos","fresas"]