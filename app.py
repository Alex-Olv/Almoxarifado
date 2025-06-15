from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Função de conexão com MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Open@2627",
        database="db_almoxarifado"
    )

# 🔗 Página inicial
@app.route('/')
def inicio():
    return render_template('inicio.html')

# 🔗 Página do formulário de ferramentas
@app.route('/ferramentas')
def formulario():
    return render_template('ferramentas.html')

# 🔗 Cadastrar ferramentas
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    marca = request.form['marca']
    preco = request.form['preco']

    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO tb_ferramentas (nome, descricao, quantidade, marca, preco) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, descricao, quantidade, marca, preco)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect('/ferramentas')

if __name__ == '__main__':
    app.run(debug=True)




