import postgresql

from hippocp import settings

class Packages:
    def __init__(self):
        h = settings.get('pgsql', 'hostname')
        u = settings.get('pgsql', 'username')
        d = settings.get('pgsql', 'database')
        p = settings.get('pgsql', 'password')
        url = 'pq://' + u + ':' + p + '@' + h + '/' + d
        self.db = postgresql.open(url)

    def list(self):
        rows = self.db.prepare("SELECT * FROM packages")
        for row in rows():
            print(row)