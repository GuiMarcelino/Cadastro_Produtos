import mysql.connector

def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database='CADASTRO_PRODUTOS',
        user='root',
        password='Gui281209'
    )
    return db

def select(db):
    comando_sql = 'SELECT * FROM CONTATOS'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    except Exception as error:
        print(error)

def select_id(db, id_registro):
    comando_sql = f'SELECT * FROM CONTATOS WHERE id = {id_registro}'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    except Exception as error:
        print(error)

def delete(db, id_registro):
    comando_sql = f'DELETE FROM CONTATOS WHERE ID = {id_registro}'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)

def insert(db, nome, sobrenome, cpf, email, telefone):
    comando_sql = 'INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES (%s, %s, %s, %s, %s)'
    parametros = (nome, sobrenome, cpf, email, telefone)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
        print('Registro inserido com sucesso.')
    except Exception as error:
        print(error)

def update(db, id, nome, sobrenome, cpf, email, telefone):
    comando_sql = "UPDATE CONTATOS SET NOME = %s, SOBRENOME = %s, CPF = %s, EMAIL = %s, TELEFONE = %s WHERE ID = %s"
    parametros = (nome, sobrenome, cpf, email, telefone, id)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)
