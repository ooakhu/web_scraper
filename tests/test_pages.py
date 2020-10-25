from unittest import TestCase
from src.db.pages import Pages
from src.db import DB


class TestPages(TestCase):
  # Test each and every method in the Pages class
  def setUp(self):
    """Setup all the necessary class and functions"""
    self.pages = Pages()
    self.conn_server = DB.only_server()
    self.conn = self.pages.connect()
    self.cursor = self.conn.cursor()

  def test_connect(self):
    """ Test connecting to postgresql server is successful """
    connection_object = self.conn
    self.assertIsNotNone(connection_object)

  def test_select(self):
    """Test select return all data from the database"""
    data = self.pages.select()
    self.assertIsNotNone(data)

  def test_find(self):
    """Test find data returns the data with the id provided"""
    data = self.pages.find(1)
    self.assertIsNotNone(data)
    self.assertEqual(type(data), tuple)

  def test_update(self):
    """Test data is updated by id with params and returned the updated data """
    data = 'True'
    updated_data = self.pages.update(data, 1)
    self.assertIsNone(updated_data)

  def test_delete(self):
    """Test data is deleted by id and returns none """
    deleted = self.pages.delete(1)
    self.assertEqual(deleted, None)

  def tearDown(self):
    """TearDown connections and delete all data created for testing purposes"""
    self.pages.close()
