
class Links:
  def __init__(self, conn):
    self.cursor = conn.cursor()

  def select(self):
    self.cursor.execute('SELECT * FROM links')
    return self.cursor.fetchall()

  def insert(self, url, id):
    self.cursor.execute(f'INSERT INTO links (url, page_id) VALUES (%s, %s)', (url, id))

  def find(self, id):
    self.cursor.execute('SELECT * FROM links WHERE id=%s', (id,))
    print(self.cursor.fetchone())

  def fetch(self, id):
    self.cursor.execute('SELECT url FROM links WHERE id =%s', (id,))
    content = self.cursor.fetchone()
    return content

  def update(self, id, params):
    query_update = 'UPDATE links SET is_scraping = %s WHERE id =%s'
    self.cursor.execute(query_update, (id, params))

  def delete(self, id):
    self.cursor.execute('DELETE FROM links WHERE page_id = %s', (id,))
