from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)

"""
Ran into trouble with the .env . Worked together on this code as a group while following along with a video.
"""