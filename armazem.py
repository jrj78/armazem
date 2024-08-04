from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Armazém de Vendas</p>"