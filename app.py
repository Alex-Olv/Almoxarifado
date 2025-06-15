from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Open@2627",
        database="db_almoxarifado"
    )

@app.route('/')
def inicio():
    return render_template('inicio.html')

# 🔗 Página do formulário + listagem
@app.route('/ferramentas')
def formulario():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, descricao, quantidade, marca, preco FROM tb_ferramentas")
    ferramentas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('ferramentas.html', ferramentas=ferramentas)

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
