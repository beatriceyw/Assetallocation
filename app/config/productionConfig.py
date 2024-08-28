import os
from dotenv import load_dotenv

load_dotenv(".env.product")

MONGODB_HOSTNAME = os.getenv("MONGODB_HOSTNAME")
MONGODB_PORT = int(os.getenv("MONGODB_PORT"))
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
authSource = str(os.getenv("authSource"))