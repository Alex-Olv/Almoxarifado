import pymysql

try:
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="@Papel157",  
        database="db_almoxarifado"
    )

    print("✅ Conectado com sucesso ao MySQL com PyMySQL!")
    conexao.close()

except pymysql.MySQLError as e:
    print(f"❌ Erro na conexão: {e}")
