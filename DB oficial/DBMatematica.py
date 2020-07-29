import sqlite3

#conn = sqlite3.connect(':memory:'), cria um banco na memoria volatil

#Variável que reecebe a conexão ao customer.db, caso ele não exista o python vai criar
conn = sqlite3.connect('matematicaregressiva.db')

print('Executado com sucesso')