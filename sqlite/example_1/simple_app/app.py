import database as database

# add one record to table
database.add_one("Laura", "Smith", "laura@smith.com")

# show all results
database.show_all()

# Delete one record
database.delete_one('6')

# show all results
database.show_all()

# Add many records
stuff = [('Brenda', 'Smitherton', 'brenda@smitherton.com'),
         ('Joshua', 'Raintree', 'joshua@raintree.com')]
database.add_many(stuff)

# show all results
database.show_all()

# Find the record with a email
database.email_lookup('john@codemy.com')
