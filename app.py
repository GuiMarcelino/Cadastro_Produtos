from configparser import RawConfigParser
from flask import Flask, render_template, redirect, request
from repository import conexao, insert, select, select_id, delete, update
from product import Produto




app = Flask(__name__)

@app.route('/', methods=['get'])
def pagina_inicial():
    return render_template('index.html')


@app.route('/cadastro', methods=['get'])
def cadastro():
    return render_template('cadastro.html')


@app.route('/inserir', methods=['POST'])
def inserir():
    produto = Produto(request.form['nome'],
                    request.form['descricao'],
                    request.form['marca'],
                    request.form['preco'],
                    request.form['cor'])
    db = conexao()
    insert(db, produto)
    return redirect('/listar/todos')


@app.route('/listar/<int:id>/', methods=['GET'])
def listar_por_id(id):
    db = conexao()
    registro = select_id(db, id)
    novo_produto = Produto(id=registro[0],
    nome=registro[1],
    descricao=registro[2],
    marca=registro[3],
    preco=registro[4],
    cor=registro[5])
    return render_template("listar.html", produto = novo_produto)

app.run(debug=True)