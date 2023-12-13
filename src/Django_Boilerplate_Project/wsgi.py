"""
WSGI config for Django_Boilerplate_Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import dotenv
import pathlib

from django.core.wsgi import get_wsgi_application

### env file path directory

CURRENT_DIR = pathlib.Path(__file__).resolve().parent

BASE_DIR = CURRENT_DIR.parent

ENV_FILE_PATH = BASE_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Boilerplate_Project.settings')

application = get_wsgi_application()
