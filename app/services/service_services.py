import psycopg2
from environs import Env

env = Env()

#conexão com banco de dados
def conn_cur():
    conn = psycopg2.connect(
        host=env("host"),
        database=env("database"),
        user=env("user"),
        password=env("password")
    )

    #cursor - tudo o que for executar dentro do banco de dados
    cur = conn.cursor()

    return (conn, cur,)

def finalize_conn_cur(conn, cur) -> None:
    conn.commit()
    cur.close()
    conn.close()