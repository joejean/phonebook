import unittest
import phonebook
class TestPhoneBook(unittest.TestCase):
	def setUp(self):
		self.conn = sqlite3.connect("testDB.db")
		self.c = conn.cursor()

	def test_create(self):
		phonebook.create
		self.conn.commit()
		pass

	def test_add(slef):
		self.conn.commit()
		pass

	def test_change(self):
		self.conn.commit()
		pass

	def test_remove(self):
		self.conn.commit()
		pass

	def test_lookup(self):
		pass

	def test_reverse_lookup(self):
		pass


if __name__ == __main__:
	unittest.main()
