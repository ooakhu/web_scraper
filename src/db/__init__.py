import psycopg2
from decouple import config
from src.db.links import Links
from src.db.pages import Pages

class DB:

  @classmethod
  def only_server(cls):
    conn = psycopg2.connect(host=config('DB_HOST'),
                                   user=config('DB_USER'),
                                   database= None,
                                   port=config('DB_PORT'),
                                   password=config('DB_PASSWORD'))

    curr = conn.cursor()
    conn.autocommit = True
    curr.execute(
      "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'tester'")
    curr.execute('DROP DATABASE IF EXISTS tester;')
    curr.execute('CREATE DATABASE tester;')

  @classmethod
  def connect(cls):
    try:
      conn2 = psycopg2.connect(host=config('DB_HOST'),
                              user=config('DB_USER'),
                              database=config('DB_NAME'),
                              port=config('DB_PORT'),
                              password=config('DB_PASSWORD'))

      conn2.autocommit = True
      return conn2
    except psycopg2.Error as error:
      return error

  @classmethod
  def setup(cls):
    cls.only_server()
    cursor = cls.connect().cursor()
    with open('src/schemas/structure.sql', 'r') as file:
      l1 = file.readline()
      cursor.execute(l1)
      l2 = file.readline()
      cursor.execute(l2)
      l3 = file.readline()
      cursor.execute(l3)
      l4 = file.readline()
      cursor.execute(l4)

  @classmethod
  def seed(cls):
    cls.only_server()
    cls.setup()
    cursor = cls.connect().cursor()

    with open('src/schemas/seed.sql') as file:
      l1 = file.readline()
      cursor.execute(l1)
      l2 = file.readline()
      cursor.execute(l2)
    print('All done')

  @classmethod
  def links(cls):
    conn = cls.connect()
    return Links(conn)

  @classmethod
  def pages(cls):
    conn = cls.connect()
    return Pages(conn)

