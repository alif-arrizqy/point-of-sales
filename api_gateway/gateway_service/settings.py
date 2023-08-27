import os
from dotenv import load_dotenv

load_dotenv()

HOST_USER = os.getenv('HOST_USER')
HOST_ITEM = os.getenv('HOST_ITEM')
HOST_TRANSACTION = os.getenv('HOST_TRANSACTION')

print(HOST_USER)