import sqlite3

# Conectando a base
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

#Query no DB, usando LIMIT para limitar a quantidade de retornos na query, também estou ordenando por ordem decrescente
c.execute("SELECT rowid,* FROM costumers ORDER BY rowid DESC LIMIT 2")


items = c.fetchall()

print("NAME " + "\t \t" + "EMAIL")
print("______" + "\t\t______")
for item in items:
    print (item)
    #print (item[0] + " " + item[1] + " \t " + item[2] ) exemplo de outras visualizações

conn.commit()

conn.close()