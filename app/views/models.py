from ..services.services import conn_cur

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

        conn.commit()
        cur.close()
        conn.close()

    def create_serie(self, data: dict):
        conn, cur = conn_cur()
        self._create_table()

        cur.execute(
            """
                INSERT TO ka_series
                    (id, serie, seasons, released_date, genre, imdb_rating)
                VALUES
                    (%(id)s, %(serie)s, %(seasons)s, %(released_date)s, %(genre)s, %(imdb_rating)s)
                RETURNING *
            """,
            data,
        )
        query = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        result = dict(zip(self.table_header, query))

        result['serie', 'gender'] = result['serie', 'gender'].title()

        return result

    def return_data(self):
        conn, cur = conn_cur()

        cur.execute("SELECT * FROM ka_series")

        query = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()

        result = [dict(zip(self.table_header, show_table)) for show_table in query]

        for data in result:
            data['serie', 'gender'] = data['serie', 'gender'].title()

        return result