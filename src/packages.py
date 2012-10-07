import postgresql

from hippocp import settings

class Packages:
    """Class to manage the packages.

    Database schema:
        id       --- Autoincremente
        name     --- Nice package name (max 20 chars)
        owner    --- uid of the owner (UNIX ID), 0 for shared packages

    """
    def __init__(self):
        h = settings.get('pgsql', 'hostname')
        u = settings.get('pgsql', 'username')
        d = settings.get('pgsql', 'database')
        p = settings.get('pgsql', 'password')
        url = 'pq://' + u + ':' + p + '@' + h + '/' + d
        self.db = postgresql.open(url)

    def list(self, uid = None, system = True):
        sql = "SELECT * FROM packages"
        if all ([system, uid]):
            sql.append(' WHERE owner = 0 OR owner = ' + uid)
        else:
            if system:
                sql.append(' WHERE owner = 0')
            if uid:
                sql.append(' WHERE owner = ' + uid)

        rows = self.db.prepare("SELECT * FROM packages")
        for row in rows():
            print(row)