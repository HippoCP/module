import postgresql

from hippocp import database

class Permissions:
    """Class to manage permissions."""
    def __init__(self):
        """Initialize the Permissions class"""
        self.db = postgresql.open(database.getPgUrl())