#!usr/bin/env python
import sys
import sqlite3


conn = sqlite3.connect("phonebook.db")
c = conn.cursor()
	

def create(phonebook_name):
	c.execute("CREATE TABLE IF NOT EXISTS {0} (name text, phone text)".format(phonebook_name))
	conn.commit()
	print "Phonebook {0} created successfully".format(phonebook_name)
	

def add(name, phone_number, phonebook_name):
	c.execute("INSERT INTO {0} VALUES(?,?)".format(phonebook_name),(name,phone_number))
	conn.commit()
	print "{0} {1} added successfully".format(name, phone_number)
	

def change(name, phone_number, phonebook_name):
	c.execute("UPDATE {0} SET phone = ? WHERE name = ?".format(phonebook_name),(phone_number, name))
	conn.commit()
	print "{0} changed successfully".format(name)
	

def lookup(name, phonebook_name):
	c.execute("SELECT * FROM {0} WHERE name LIKE ?".format(phonebook_name), ('%'+name+'%',))
	result = c.fetchall()
	if len(result) == 0:
		print "{0} does not exist in the db".format(name)
	else:
		for tup in result:
			print "{0} {1}".format(tup[0], tup[1])
	

def reverse_lookup(phone_number, phonebook_name):
	c.execute("SELECT * FROM {0} WHERE phone = ?".format(phonebook_name),(phone_number,))
	result = c.fetchone()
	if result == None:
		print "Phone number {0} does not exist in the db".format(phone_number)
	else:
		print "{0} {1}".format(result[0], result[1])
	

def remove(name, phonebook_name):
	c.execute("DELETE FROM {0} WHERE name = ?".format(phonebook_name),(name,))
	conn.commit()
	print "{0} deleted successfully".format(name)
	


if __name__ == '__main__':

	if sys.argv[1] == "create":
		if len(sys.argv) < 3:
			print "Please provide a name for the phone book"
			print "The proper format is python phonebook.py create phonebook_name"
			sys.exit(-1)
		else:
			create(sys.argv[2])

	elif sys.argv[1] == "add":
		if len(sys.argv) < 4:
			print " Wrong Format"
			print "The proper format for adding is:  phonebook add 'John Michael' '123 456 4323' phonebook_name"
			sys.exit(-1)
		else:
			add(sys.argv[2],sys.argv[3], sys.argv[4])

	elif sys.argv[1] == "change":
		if len(sys.argv) < 4:
			print " Wrong Format"
			print "The proper format for changing is:  phonebook change 'John Michael' '123 456 4323' phonebook_name"
			sys.exit(-1)
		else:
			change(sys.argv[2],sys.argv[3], sys.argv[4])
		
	elif sys.argv[1] == "lookup":
		if len(sys.argv) < 3:
			print " Wrong Format"
			print "The proper format for lookup is:  phonebook lookup 'John Michael' phonebook_name"
			sys.exit(-1)
		else:
			lookup(sys.argv[2],sys.argv[3])

	elif sys.argv[1] == "reverse-lookup":
		if len(sys.argv) < 3:
			print " Wrong Format"
			print "The proper format for reverse-lookup is:  phonebook reverse-lookup '917 123 2343' phonebook_name"
			sys.exit(-1)
		else:
			reverse_lookup(sys.argv[2],sys.argv[3])

	elif sys.argv[1] == "remove":
		if len(sys.argv) < 3:
			print " Wrong Format"
			print "The proper format for removing is:  phonebook remove 'John Michael' phonebook_name"
			sys.exit(-1)
		else:
			remove(sys.argv[2],sys.argv[3])

	sys.exit(0)