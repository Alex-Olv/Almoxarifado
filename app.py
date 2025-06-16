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
    cursor.execute("SELECT id, nome, descricao, quantidade, marca, preco FROM tb_ferramentas")
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

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tb_ferramentas WHERE id = %s", (id,))
    ferramenta = cursor.fetchone()
    cursor.close()
    conexao.close()
    return render_template('editar.html', ferramenta=ferramenta)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    nome = request.form['nome']
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    marca = request.form['marca']
    preco = request.form['preco']

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        UPDATE tb_ferramentas
        SET nome=%s, descricao=%s, quantidade=%s, marca=%s, preco=%s
        WHERE id=%s
    """
    valores = (nome, descricao, quantidade, marca, preco, id)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/ferramentas')

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM tb_ferramentas WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/ferramentas')

@app.route('/emprestimo')
def emprestimo():
    conexao = conectar()
    cursor = conexao.cursor()

    # Buscar ferramentas
    cursor.execute("SELECT id, nome FROM tb_ferramentas")
    ferramentas = cursor.fetchall()

    # Buscar empréstimos
    cursor.execute("""
        SELECT e.id, e.dt_emprestimo, e.dt_entrega, e.nome_responsavel, 
               e.nome_obra, e.nome_almoxarife, f.nome 
        FROM tb_emprestimo e
        JOIN tb_ferramentas f ON e.id_ferramenta = f.id
    """)
    emprestimos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('emprestimo.html', ferramentas=ferramentas, emprestimos=emprestimos)

@app.route('/cadastrar_emprestimo', methods=['POST'])
def cadastrar_emprestimo():
    dt_emprestimo = request.form['dt_emprestimo']
    dt_entrega = request.form['dt_entrega']
    nome_responsavel = request.form['nome_responsavel']
    nome_obra = request.form['nome_obra']
    nome_almoxarife = request.form['nome_almoxarife']
    id_ferramenta = request.form['id_ferramenta']

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tb_emprestimo 
        (dt_emprestimo, dt_entrega, nome_responsavel, nome_obra, nome_almoxarife, id_ferramenta)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (dt_emprestimo, dt_entrega, nome_responsavel, nome_obra, nome_almoxarife, id_ferramenta))

    cursor.execute("""
        UPDATE tb_ferramentas
        SET quantidade = quantidade - 1
        WHERE id = %s AND quantidade > 0
    """, (id_ferramenta,))

    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect('/emprestimo')

@app.route('/editar_emprestimo/<int:id>', methods=['GET'])
def editar_emprestimo(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT e.id, e.dt_emprestimo, e.dt_entrega, e.nome_responsavel, 
               e.nome_obra, e.nome_almoxarife, f.nome, e.id_ferramenta
        FROM tb_emprestimo e
        JOIN tb_ferramentas f ON e.id_ferramenta = f.id
        WHERE e.id = %s
    """, (id,))
    emprestimo = cursor.fetchone()
    cursor.close()
    conexao.close()
    return render_template('editar_emprestimo.html', emprestimo=emprestimo)


@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar_emprestimo(id):
    data_emprestimo = request.form['dt_emprestimo']
    data_entrega = request.form['dt_entrega']
    responsavel = request.form['nome_responsavel']
    obra = request.form['nome_obra']
    almoxarife = request.form['nome_almoxarife']
    ferramenta = request.form['id_ferramenta']

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        UPDATE tb_emprestimo
        SET dt_emprestimo=%s, dt_entrega=%s, nome_responsavel=%s, nome_obra=%s, nome_almoxarife=%s, id_ferramenta=%s
        WHERE id=%s
    """
    valores = (data_emprestimo, data_entrega, responsavel, obra, almoxarife, ferramenta, id)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/emprestimo')    

@app.route('/excluir_emprestimo/<int:id>', methods=['POST'])
def excluir_emprestimo(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_ferramenta FROM tb_emprestimo WHERE id = %s", (id,))
    resultado = cursor.fetchone()
    if resultado:
        id_ferramenta = resultado[0]
        cursor.execute("""
            UPDATE tb_ferramentas
            SET quantidade = quantidade + 1
            WHERE id = %s
        """, (id_ferramenta,))
    sql = "DELETE FROM tb_emprestimo WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/emprestimo')

if __name__ == '__main__':
    app.run(debug=True)
