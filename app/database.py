from pymongo.mongo_client import MongoClient
from app.config import developmentConfig
from app.utils import log_util

host = developmentConfig.MONGODB_HOSTNAME
query_param = 'authMechanism=SCRAM-SHA-256'
port = developmentConfig.MONGODB_PORT
username = developmentConfig.MONGODB_USER
password = developmentConfig.MONGODB_PASSWORD
authSource = developmentConfig.authSource
uri = f"mongodb://{username}:{password}@{host}:{port}/?{query_param}&authSource={authSource}"
dbname = str(developmentConfig.authSource)
client = MongoClient(uri)[dbname]
client.command('ping')
log_util.info("You successfully greenos connected to MongoDB!")
