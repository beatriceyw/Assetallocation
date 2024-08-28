import os
from dotenv import load_dotenv

load_dotenv(".env.develope")

MONGODB_HOSTNAME = os.getenv("MONGODB_HOSTNAME")
MONGODB_PORT = os.getenv("MONGODB_PORT")
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
authSource = os.getenv("authSource")
    