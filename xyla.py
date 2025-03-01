from dotenv import load_dotenv
import os

load_dotenv()

print(client_id) 
client_id = os.getenv(client_id)
client_secret = os.getenv(client_secret)

print(client_id, client_secret)