from flask import Flask, render_template
import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy

#abre o arquivo database.db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

#instruções de configuração
app = Flask('__name__')
#app.config('SECRET_KEY') = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

#classes
class cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.Varchar(45), nullable=False)
    nome_juridico = db.Column(db.Varchar(45), nullable=False)
    cnpj = db.Column(db.Varchar(45), nullable=False)

@app.route("/")
def inicio():
    link_inicio =  'http://127.0.0.1:5000/'
    return render_template('inicio.html')
