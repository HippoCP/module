import postgresql

from hippocp import database

class Permissions:
    """Class to manage permissions."""
    def __init__(self):
        """Initialize the Permissions class"""
        self.db = postgresql.open(database.getPgUrl())

    def exists(self, permissionid):
        """Check if the permission exists"""
        sql = "SELECT COUNT(id) FROM permissions"
        sql+= "    WHERE id = " + permissionid
        rows = self.db.prepare(sql)
        if rows.first() is 0:
            return False
        else:
            return True

    def list(self):
        """List permissions"""
        sql = "SELECT * FROM permissions"
        rows = self.db.prepare(sql)
        return rows()

    def last(self):
        """Check if the permission exists"""
        sql = "SELECT MAX(id) FROM permissions"
        rows = self.db.prepare(sql)
        return rows.first()

