import sqlite3

# Conectando a base
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

many_customers = [
                        ('Claudinho','Buchecha','buchecha@claudio.com'),
                        ('Kanye','West','monstro@.com'),
                        ('Men','Cleber','bambam@bbb'),
                ]

#Inserindo um valor por vez
#c.execute("INSERT INTO costumers VALUES ('Leo', 'Gomez','leogomez@gmail.com')")

#Inserindo múltiplos valores
c.executemany("INSERT INTO costumers VALUES (?,?,?)", many_customers)

print("Command executed succesfully...")

conn.commit()

conn.close()