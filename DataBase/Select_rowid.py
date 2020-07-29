import sqlite3

# Conectando a base
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

#Query no DB sleecionando também a rowid (chave primária que o sql lite cria)
c.execute("SELECT rowid, * FROM costumers")

items = c.fetchall()

for item in items:
    print (item)

conn.close()