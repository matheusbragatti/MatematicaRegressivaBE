import sqlite3

#Query the DB and return all records
def show_all():
    # Conectando a base
    conn = sqlite3.connect('costumer.db')
    #Criando um apontador
    c = conn.cursor()

    #Query the Database
    c.execute("SELECT rowid, * FROM costumers")
    items = c.fetchall()

    for item in items:
        print (item)

    #Commit database
    conn.commit()
    #Close database   
    conn.close()

#Lookup with where
def email_lookup(email):
    # Conectando a base e criando um cursor
    conn = sqlite3.connect('costumer.db')
    c = conn.cursor()

    #Query the Database
    c.execute("SELECT * FROM costumers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print (item)

    #Close database   
    conn.close()

#Add a new record to the table
def add_one(first,last,email):
    # Conectando a base e criando um cursor
    conn = sqlite3.connect('costumer.db')
    c = conn.cursor()
    c.execute("INSERT INTO costumers VALUES (?,?,?)", (first,last,email))

    #Commit database
    conn.commit()
    #Close connection   
    conn.close()

#Add many records to the table
def add_many(list):
    # Conectando a base e criando um cursor
    conn = sqlite3.connect('costumer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO costumers VALUES (?,?,?)", (list))

    #Commit database
    conn.commit()
    #Close connection   
    conn.close()

#Delete a record from table
def delete_one(id):
    conn = sqlite3.connect('costumer.db')
    c = conn.cursor()
    c.execute("DELETE from costumers WHERE rowid = (?)", id)

    #Commit database
    conn.commit()
    #Close connection   
    conn.close()
