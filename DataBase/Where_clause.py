import sqlite3

# Conectando a base
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

#Alguns Selects com where no DB 
#c.execute("SELECT * FROM costumers WHERE segundo_nome = 'Gomez'")
#c.execute("SELECT rowid, * FROM costumers WHERE rowid >= 2")
#c.execute("SELECT * FROM costumers WHERE primeiro_nome LIKE 'L%'")
c.execute("SELECT rowid,* FROM costumers where segundo_nome LIKE 'We%' OR  rowid = 3")

items = c.fetchall()

for item in items:
    print (item)
   
conn.close()