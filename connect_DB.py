import psycopg2

try:
    # Conectar ao banco (substitua pelos seus dados)
    conn = psycopg2.connect(
        dbname="banco666",
        user="postgres",
        password="******",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Executa consulta simples
    cur.execute("SELECT nome FROM cliente;")
    versao = cur.fetchone()

    print("Conexão bem-sucedida! Versão do PostgreSQL:", versao[0])

    # Fechar cursor e conexão
    cur.close()
    conn.close()

except Exception as e:
    print("Erro na conexão:", e)
