import crypt
import os
import postgresql

from pwd import getpwnam

from hippocp import database

class User:
    """User model the users."""

    def __init__(self, uid):
        """Initialize the User model"""
        self.db = postgresql.open(database.getPgUrl())
        self.id = uid

    def roles(self):
        """List all roles of the user"""
        sql = "SELECT roles.id, roles.name FROM roles"
        sql+= "    JOIN role_user ON role_user.role_id = roles.id"
        sql+= "    WHERE role_user.user_id = " + self.id
        rows = self.db.prepare(sql)
        return rows()

    def checkRole(self, role):
        """Check if the user has a particular role"""
        sql = "SELECT COUNT(role_id) FROM role_user"
        sql+= "    WHERE role_id = " + role
        sql+= "        AND user_id = " + self.id
        rows = self.db.prepare(sql)
        if rows.first() is 0:
            return False
        else:
            return True