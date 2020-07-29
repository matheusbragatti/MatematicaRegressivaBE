import sqlite3

# Conectando a base
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

#Updatar dados

#c.execute("""UPDATE costumers SET primeiro_nome = 'Mano Brown'
#            WHERE segundo_nome = 'Buchecha'
#        """)

c.execute("""UPDATE costumers SET primeiro_nome = 'Girls'
            WHERE rowid = 3
        """)

conn.commit()

c.execute("SELECT rowid, * FROM costumers")

items = c.fetchall()

for item in items:
    print (item)
    