#!/bin/bash
# Force upgrade all requirements to match versions in requirements.txt
echo "Upgrading all dependencies..."
pip install --upgrade --force-reinstall -r requirements.txt

# Verify mysqlclient version
echo "Installed mysqlclient version:"
python -m pip show mysqlclient
