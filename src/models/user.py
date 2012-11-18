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
        sql = "SELECT * FROM roles"
        sql+= "    JOIN role_user ON role_user.user_id = " + self.id
        rows = self.db.prepare(sql)
        return rows()