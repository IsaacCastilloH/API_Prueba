import time
from django.db import connections
from django.db.utils import OperationalError

def wait_for_db():
    """Espera a que la base de datos esté disponible."""
    db_conn = None
    while not db_conn:
        try:
            db_conn = connections['default']
        except OperationalError:
            print("Base de datos no disponible, intentando de nuevo en 1 segundo...")
            time.sleep(1)
    print("Base de datos disponible.")