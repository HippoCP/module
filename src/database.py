import postgresql
from hippocp import settings

def getPgUrl():
    """Provide the PostgreSQL connection url"""
    h = settings.get('pgsql', 'hostname')
    u = settings.get('pgsql', 'username')
    d = settings.get('pgsql', 'database')
    p = settings.get('pgsql', 'password')
    o = settings.get('pgsql', 'port')
    return 'pq://' + u + ':' + p + '@' + h + ':' + o + '/' + d