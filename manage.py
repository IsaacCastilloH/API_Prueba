import os
import sys
from wait_for_db import wait_for_db


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
    try:
        wait_for_db()
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
