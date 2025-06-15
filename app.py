from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão com o MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Open@2627",
        database="db_almoxarifado"
    )

# Página do formulário
@app.route('/')
def formulario():
    return render_template('ferramentas.html')

# Recebe os dados do formulário e insere no banco
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    marca = request.form['marca']

    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO tb_ferramenta (nome, descricao, quantidade, marca) VALUES (%s, %s, %s, %s)"
    valores = (nome, descricao, quantidade, marca)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)




