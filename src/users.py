import crypt
import os
import postgresql

from pwd import getpwnam

from hippocp import database

class Users:
    """Class to manage the users.

    Database schema:
        uid     --- UNIX User ID
        name    --- Nice user name (max 20 chars)
        package --- Package ID
        father  --- User's reseller/admin
    """
    def __init__(self):
        """Initialize the Packages class"""
        self.db = postgresql.open(database.getPgUrl())

    def add(self, name, package, father, password):
        """Add a user"""
        encPass = crypt.crypt(password,"22")
        os.system("useradd -p " + encPass + " " + name)
        uid = str(getpwnam(name).pw_uid)
        if self.db.execute('INSERT INTO users (uid, name, package, father) VALUES (\''+uid+'\', \''+name+'\', \''+package+'\', \''+father+'\')') is None:
            return True
        else:
            return False

    def list(self, father = None):
        """List users.
        If no arguments are passed, all users on the system will be showed
        otherwise only that user childs will be passed."""
        sql = "SELECT * FROM users"
        if father:
            sql += " WHERE father = " + father
        rows = self.db.prepare(sql)
        return rows()