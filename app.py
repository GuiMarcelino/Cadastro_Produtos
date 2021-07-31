from flask import Flask
from flask.wrappers import Request
from werkzeug.wrappers import request
from product import Produto
from repository import conexao, insert, select, select_id, delete, update




app = Flask(__name__)

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
    produto = Produto()
    return render_template("listar_id.html", lista_banco_no_html = registro)

