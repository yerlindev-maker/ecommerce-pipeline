import requests
import os
import psycopg2
import json

# Configuración de la base de datos
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT', '5432')

