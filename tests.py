import unittest
import phonebook

class TestPhoneBook(unittest.TestCase):
	
	def test_successful_create(self):
		phonebook.create("testing.db")
		self.assertEqual(phonebook.create("testing.db"), "Phonebook testing.db created successfully")
		

	def test_successful_add(self):
		self.assertEqual(phonebook.add("Joe Jean", "123 123 4556","testing.db"),
			"Joe Jean 123 123 4556 added successfully")
		
	def test_successful_change(self):
		self.assertEqual(phonebook.change("Joe Jean","123 345 2332", "testing.db"),
			"Joe Jean changed successfully")

	def test_remove(self):
		self.assertEqual(phonebook.remove("Joe Jean", "testing.db"), 
		"Joe Jean deleted successfully"	)
		

	def test_successful_lookup(self):
		self.assertEqual(phonebook.lookup("Joe Jean", "testing.db"),
			"Joe Jean 123 345 2332")

	def test_failed_lookup(self):
		self.assertEqual(phonebook.lookup("Joe Jan", "testing.db"),
			"Joe Jan does not exist in the db")

	def test_successful_reverse_lookup(self):
		self.assertEqual(phonebook.reverse_lookup("123 345 2332", "testing.db"),
			"Joe Jean 123 345 2332")

	def test_failed_reverse_lookup(self):
		self.assertEqual(phonebook.reverse_lookup("123 344 2332", "testing.db"),
			 'Phone number 123 344 2332 does not exist in the db')



if __name__ == '__main__':
	unittest.main()
