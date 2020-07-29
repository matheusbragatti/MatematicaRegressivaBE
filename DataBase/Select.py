import sqlite3

# Conectando a base
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

#Query no DB
c.execute("SELECT * FROM costumers")
#print(c.fetchone())
#print(c.fetchmany(3))
#print(c.fetchall ())

items = c.fetchall()

print("NAME " + "\t \t" + "EMAIL")
print("______" + "\t\t______")
for item in items:
    print (item[0] + " " + item[1] + " | " + item[2] )
    #print (item[0] + " " + item[1] + " \t " + item[2] ) exemplo de outras visualizações

conn.commit()

conn.close()