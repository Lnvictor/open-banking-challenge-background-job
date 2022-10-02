import os

# NOSQL connection vars
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'admin')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'password')
MONGO_PORT = os.getenv('MONGO_PORT', '27017')
MONGO_DB = os.getenv('MONGO_DB', 'admin')


OPEN_BANKING_API_URL = os.getenv('OPEN_BANKING_API_URL', 'https://data.directory.openbankingbrasil.org.br/participants')

SCHEDULER_TIMER = int(os.getenv('SCHEDULER_TIMER', '60'))
