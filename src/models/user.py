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

    def addRole(self, role):
        """Check if the user is in a role.
        If the user has already the role True is returned.
        If the user has not the role yet, the role is assigned and True is returned"""
        if self.checkRole(role) is True:
            return True
        self.db.execute("INSERT INTO role_user VALUES (" + role + "," + self.id + ")")
        if self.checkRole(role) is True:
            return True
        else:
            return False

    def removeRole(self, role):
        """Remove the role if it exists"""
        if self.checkRole(role) is False:
            return True
        self.db.execute("DELETE FROM role_user WHERE role_id = " + role + " AND user_id = " + self.id)
        if self.checkRole(role) is False:
            return True
        else:
            return False

    def permissions(self):
        """List all permissions of the user"""
        sql = "SELECT permissions.id, permissions.name FROM permissions"
        sql+= "    JOIN permission_user ON permission_user.permission_id = permissions.id"
        sql+= "    WHERE permission_user.user_id = " + self.id
        rows = self.db.prepare(sql)
        return rows()

    def checkPermission(self, permission):
        """Check if the user has a particular permission"""
        sql = "SELECT COUNT(permission_id) FROM permission_user"
        sql+= "    WHERE permission_id = " + permission
        sql+= "        AND permission_id = " + self.id
        rows = self.db.prepare(sql)
        if rows.first() is 0:
            return False
        else:
            return True

    def addPermission(self, permission):
        """Check if the user has a permission
        If the user has already the permission True is returned.
        If the user has not the permission yet, it is assigned and True is returned"""
        if self.checkPermission(permission) is True:
            return True
        self.db.execute("INSERT INTO permission_user VALUES (" + permission + "," + self.id + ")")
        if self.checkPermission(permission) is True:
            return True
        else:
            return False

    def removePermission(self, permission):
        """Remove the permission to this user if is granted"""
        if self.checkPermission(permission) is False:
            return True
        self.db.execute("DELETE FROM permission_user WHERE permission_id = " + permission + " AND user_id = " + self.id)
        if self.checkPermission(permission) is False:
            return True
        else:
            return False