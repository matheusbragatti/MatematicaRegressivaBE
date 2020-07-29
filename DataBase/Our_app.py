import database

#Add a record to the database
#database.add_one("Cleo","Pires","Fiuck@mtv.com")

#Lookup by email
database.email_lookup("bambam@bbb")
#Add many records to the database
'''
stuff = [
    ('Rick','Sanchez','ricksanchez@rickandmorty.com'),
    ('Morty','Smith','mortysmith@rickandmorty.com')
    ]

database.add_many(stuff)
'''

#Delete record using rowid as string
#database.delete_one('5')

#show all the records
#database.show_all()