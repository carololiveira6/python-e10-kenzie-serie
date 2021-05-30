import psycopg2

#conexão com banco de dados
def conn_cur():
    conn = psycopg2.connect(
        host='localhost',
        database='ka_series',
        user='carolina',
        password='1234'
    )

    #cursor - tudo o que for executar dentro do banco de dados
    cur = conn.cursor()

    return (conn, cur,)