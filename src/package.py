import postgresql

from hippocp import settings

class Package:
    """Class to manage the packages.

    Database schema:
        id       --- Autoincremente
        name     --- Nice package name (max 20 chars)
        owner    --- uid of the owner (UNIX ID), 0 for shared packages

    """
    def __init__(self):
        """Initialize the Packages class"""
        h = settings.get('pgsql', 'hostname')
        u = settings.get('pgsql', 'username')
        d = settings.get('pgsql', 'database')
        p = settings.get('pgsql', 'password')
        url = 'pq://' + u + ':' + p + '@' + h + '/' + d
        self.db = postgresql.open(url)

    def list(self, uid = None, system = True):
        """Retrive a list of packages.
        If no argument is passed only the system packages will be returned.

        If the UID (Unix User ID) is passed as first parameter system and User
        packages will be returned.

        Arguments:
        uid --- Add packages of a specific UNIX User ID to the returned list
        system --- Add system packages to the returned list (default behaviour)
        """
        sql = "SELECT * FROM packages"
        if all ([system, uid]):
            sql += ' WHERE owner = 0 OR owner = ' + uid
        else:
            if system:
                sql += ' WHERE owner = 0'
            if uid:
                sql += ' WHERE owner = ' + uid

        rows = self.db.prepare(sql)
        return rows()