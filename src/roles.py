import postgresql

from hippocp import database

class Roles:
    """Class to manage roles."""
    def __init__(self):
        """Initialize the Roles class"""
        self.db = postgresql.open(database.getPgUrl())

    def add(self, name):
        """Add a role"""
        if self.db.execute('INSERT INTO roles (name) VALUES (\''+name+'\')') is None:
            return True
        else:
            return False

    def list(self):
        """List roles"""
        sql = "SELECT * FROM roles"
        rows = self.db.prepare(sql)
        return rows()