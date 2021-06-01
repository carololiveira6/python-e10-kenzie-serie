from flask.json import jsonify
from .service_services import conn_cur, finalize_conn_cur

class SeriesTable:
    table_header = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

    def _create_table(self) -> None:
        conn, cur = conn_cur()

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS ka_series
                    (
                        id BIGSERIAL PRIMARY KEY,
                        serie VARCHAR(100) NOT NULL UNIQUE,
                        seasons INTEGER NOT NULL,
                        released_date DATE NOT NULL,
                        genre VARCHAR(50) NOT NULL,
                        imdb_rating FLOAT NOT NULL
                    );
            """
        )

        finalize_conn_cur(conn, cur)
        
    def create_serie(self, data: dict):
        conn, cur = conn_cur()
        self._create_table()

        data['serie'] = data['serie'].title()
        data['genre'] = data['genre'].title()

        cur.execute(
            """
                INSERT INTO ka_series
                    (serie, seasons, released_date, genre, imdb_rating)
                VALUES
                    (%(serie)s, %(seasons)s, %(released_date)s, %(genre)s, %(imdb_rating)s)
                RETURNING *
            """,
            data,
        )
        query = cur.fetchone()

        finalize_conn_cur(conn, cur)

        result = dict(zip(self.table_header, query))

        result["released_date"] = result["released_date"].strftime("%d/%m/%Y")

        return result

    def return_data(self):
        conn, cur = conn_cur()

        SeriesTable._create_table(self)

        cur.execute("SELECT * FROM ka_series")

        #.fetchall(): busca todas as linhas de um resultado de consulta e retorna todas as linhas como uma lista de tuplas; uma lista vazia é retornada se não houver nenhum registro para buscar.
        query = cur.fetchall()

        finalize_conn_cur(conn, cur)

        result = [dict(zip(self.table_header, show_table)) for show_table in query]

        for data in result:
            data["released_date"] = data["released_date"].strftime("%d/%m/%Y")

        # result_dict = {data: result_list for data, result_list in enumerate(result)}

        return result

    def select_id(self):
        conn, cur = conn_cur()

        if SeriesTable.return_data(self) == {}:
            return {}, 404

        cur.execute("SELECT id FROM ka_series")

        query = cur.fetchall()

        finalize_conn_cur(conn, cur)

        result = dict(zip(self.table_header, query))

        return result
        