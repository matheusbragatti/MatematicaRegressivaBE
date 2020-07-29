import sqlite3

#Conecta ao DB
conn = sqlite3.connect('costumer.db')

#Criando um apontador
c = conn.cursor()

#Criando a tabela usando SQL, vai ser case sensitive. Usei 6 "" pois é mais adequado para vários preenchimentos
c.execute("""CREATE TABLE costumers (
        primeiro_nome text,
        segundo_nome text,
        email text
    )""")

#DataTypes no Python são:
# NULL - Existe ou não existe (NULL ou NOT NULL)
# INTEGER - Números inteiros
# REAL - Números reais
# TEXT
# BLOB - qualquer outra coisa tipo mp3 ou imagem 

#Fazendo commit
conn.commit()

#Fechando conexão
conn.close()