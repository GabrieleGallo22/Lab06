from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        try:
            conn =  get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT codice, marca, modello, anno, posti, disponibile FROM automobile;"
            )
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            if not result:
                return None

            automobili = [Automobile(*row) for row in result]
            return automobili
        except mysql.connector.Error as e:
            print(f"Errore DB in cerca_automobili_per_modello: {e}")
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        try:
            connect = get_connection()
            cursor = connect.cursor()
            cursor.execute(
                "SELECT codice, marca, modello, anno, posti, disponibile "
                "FROM automobile "
                "WHERE modello LIKE %s;",
                (f"%{modello}%",)
            )

            result = cursor.fetchall()
            cursor.close()
            connect.close()
            if not result:
                result = None

            automobili = [Automobile(*row) for row in result]
            return automobili
        except mysql.connector.Error as e:
            print(f"Errore DB in cerca_automobili_per_modello: {e}")
            return None


