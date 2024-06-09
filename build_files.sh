# #!/bin/bash

# # Exit immediately if a command exits with a non-zero status
# set -e

# # Install dependencies
# pip3 install -r requirements.txt

# # Collect static files
# # python3.9 manage.py collectstatic --noinput
# # python manage.py collectstatic --noinput

pip install -r requirements.txt 
python3.9 manage.py collectstatic