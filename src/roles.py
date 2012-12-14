import postgresql

from hippocp import database

class Roles:
    """Class to manage roles."""
    def __init__(self):
        """Initialize the Roles class"""
        self.db = postgresql.open(database.getPgUrl())

    def add(self, name):
        """Add a role"""
        next = str(self.last() + 1)
        if self.db.execute('INSERT INTO roles (id, name) VALUES (\''+next+'\', \''+name+'\')') is None:
            return True
        else:
            return False

    def remove(self, roleid):
        """Remove the role with matching ID"""
        if self.exists(roleid) is False:
            return True
        self.db.execute("DELETE FROM roles WHERE id = " + roleid)
        if self.exists(roleid) is False:
            return True

    def exists(self, roleid):
        """Check if the role exists"""
        sql = "SELECT COUNT(id) FROM roles"
        sql+= "    WHERE id = " + roleid
        rows = self.db.prepare(sql)
        if rows.first() is 0:
            return False
        else:
            return True

    def last(self):
        """Check if the role exists"""
        sql = "SELECT MAX(id) FROM roles"
        rows = self.db.prepare(sql)
        return rows.first()

    def list(self):
        """List roles"""
        sql = "SELECT * FROM roles"
        rows = self.db.prepare(sql)
        return rows()