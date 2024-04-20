import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('INSERT INTO cliente (nome_cliente, nome_juridico, cnpj) VALUES (?,?,?)',
            ('teste', 'teste ltda','23883748')
            )

connection.commit()
connection.close()
