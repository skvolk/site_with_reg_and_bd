import sqlite3
from werkzeug.security import check_password_hash


class BDManager:
    @staticmethod
    def new_base():
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Users (
                       id INTeger NOT NULL PRIMARY KEY AUTOINCREMENT,
                       login text NOT NULL,
                       psw text NOT NULL,
                       time text NOT NULL
                       );''')
            conn.commit()


    @staticmethod
    def add_user(login, password_hash, registration_date):
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO Users (login, psw, time) VALUES (?, ?, ?)''',
                      (login, password_hash, registration_date))
            conn.commit()


    @staticmethod
    def get_user(login):
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            s = f"SELECT * from Users WHERE login = '{login}';"
            c.execute(s)
            rows = c.fetchall()
            if len(rows) == 0:
                conn.commit()
                return True
            else:
                conn.commit()
                return False


    @staticmethod
    def check_user(login, password_hash):
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            s = f"SELECT * from Users WHERE login = '{login}';"
            c.execute(s)
            rows = c.fetchall()
            if len(rows) == 0:
                conn.commit()
                return False
            else:
                if check_password_hash(rows[0][2], password_hash):
                    conn.commit()
                    return True
                else:
                    conn.commit()
                    return False


    @staticmethod
    def enter_user(login):
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            s = f"SELECT * from Users WHERE login = '{login}';"
            c.execute(s)
            return c.fetchone()