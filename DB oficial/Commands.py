import sqlite3

def create_table():
    #Creating table
    #First connecting to de base
    conn = sqlite3.connect('matematicaregressiva.db')
    #criando apontador
    c = conn.cursor()

    #c.execute("""CREATE TABLE perfil (
    #    perfil_id INTEGER NOT NULL PRIMARY KEY,
    #    progresso_total INTEGER,
    #    recomendacoes TEXT,
    #    login TEXT,
    #    password TEXT
    #)""")

    #c.execute("""CREATE TABLE aluno (
    #    aluno_id INTEGER NOT NULL PRIMARY KEY,
    #    nome TEXT,
    #    email TEXT,
    #    escolaridade TEXT,
    #    idade INTEGER
    #)""")

    #c.execute("""CREATE TABLE aulas (
    #    aula_id INTEGER NOT NULL PRIMARY KEY,
    #    nome TEXT,
    #    progresso_atual INTEGER,
    #    progresso_maximo INTEGER
    #)""")

    print ("Comando executado com sucesso")

    #Commit database
    conn.commit()
    #Close database   
    conn.close()

def drop_table():
    #First connecting to de base
    conn = sqlite3.connect('matematicaregressiva.db')
    #criando apontador
    c = conn.cursor()

    c.execute("DROP TABLE aluno")

    print("Tabela removida")

    #Commit database
    conn.commit()
    #Close database   
    conn.close()


#Query the DB and return all records
def show_all():
    # Conectando a base
    conn = sqlite3.connect('matematicaregressiva.db')
    #Criando um apontador
    c = conn.cursor()

    #Query the Database
    c.execute("SELECT rowid, * FROM perfil")
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
    conn = sqlite3.connect('matematicaregressiva.db')
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
    conn = sqlite3.connect('matematicaregressiva.db')
    c = conn.cursor()
    c.execute("INSERT INTO costumers VALUES (?,?,?)", (first,last,email))

    #Commit database
    conn.commit()
    #Close connection   
    conn.close()

#Add many records to the table
def add_many(list):
    # Conectando a base e criando um cursor
    conn = sqlite3.connect('matematicaregressiva.db')
    c = conn.cursor()
    c.executemany("INSERT INTO costumers VALUES (?,?,?)", (list))

    #Commit database
    conn.commit()
    #Close connection   
    conn.close()

#Delete a record from table
def delete_one(id):
    conn = sqlite3.connect('matematicaregressiva.db')
    c = conn.cursor()
    c.execute("DELETE from costumers WHERE rowid = (?)", id)

    #Commit database
    conn.commit()
    #Close connection   
    conn.close()
