
class Pages:
    def __init__(self, conn):
      self.cursor = conn.cursor()

    def select(self):
      self.cursor.execute('SELECT * FROM pages')
      return self.cursor.fetchall()

    def find(self, id):
      self.cursor.execute('SELECT * FROM pages WHERE id=%s', (id,))
      return self.cursor.fetchone()

    def fetch(self, id):
      self.cursor.execute('SELECT url FROM pages WHERE id =%s', (id,))
      content = self.cursor.fetchone()
      return content

    def update(self, id, params):
      query_update = 'UPDATE pages SET is_scraping = %s WHERE id =%s'
      self.cursor.execute(query_update, (id, params))

    def delete(self, id):
      self.cursor.execute('DELETE FROM pages WHERE id = %s', (id,))
