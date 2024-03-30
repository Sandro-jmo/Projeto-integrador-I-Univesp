#
from flask import Flask, render_template, request, redirect

class Cliente:
    def __init__(self, id_cliente, nome_cliente, nome_juridico, cnpj_cliente):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.nome_juridico = nome_juridico
        self.cnpj_cliente = cnpj_cliente

app = Flask(__name__)

@app.route('/')
def index():
    link_cadastro = 'http://127.0.0.1:5000/cadastro'
    return render_template('lista.html', titulo_site ='EMPRESA AMBIENTAL', nome = 'Empresa Ambiental', nome_jur = 'Empresa Consultoria e Planejamento em Meio Ambiente LTDA')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='NOVO CADASTRO')

@app.route('/criar', methods=['POST', ])
def criar():
    id_cliente = request.form['id_cliente']
    nome_cliente = request.form['nome_cliente']
    nome_juridico = request.form['nome_juridico']
    cnpj_cliente = request.form['cnpj_cliente']
    cliente = Cliente('id_cliente', 'nome_cliente', 'nome_juridico', 'cnpj_cliente')
    return redirect('/criado', )

@app.route('/criado')
def criado():
    return render_template('criado.html', lista='cliente')

app.run(debug=True)
