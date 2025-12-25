#!/usr/bin/env python
import os
import sys

# ✅ FORCE PyMySQL BEFORE DJANGO LOADS
import pymysql
pymysql.install_as_MySQLdb()

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_master.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
