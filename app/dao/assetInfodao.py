from datetime import timedelta, timezone, datetime
from bson import ObjectId

from app.utils import log_util
from app.database import client
from app.dto import assetInfoDto
from app.models import assetInfoModels
 
collection = 'asset_info'
collection_temp = 'asset_info_temp'


# def find_kepco_list():
#     log_util.info(f"find_kepco_list START --------------------------------------")

#     # Mongo 쿼리는 이런 식으로 활용하면 됨
#     yesterday = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now(timezone(timedelta(hours=9))) - timedelta(days=1))
#     search_pipeline = [
#         {"$sort": {"_id": -1}},
#         {'$match': {'F_AP_QT_ALL': {"$gt": 10}}},
#         {"$limit": 10}
#     ]
#     cursor = client[collection].aggregate(search_pipeline)
#     if not cursor:
#         return None
#     result_list = [KepcoBillingDaily(result) for result in cursor]
#     log_util.info(f"result_list: {result_list}")
#     return result_list

def find_etf_detail(stock_name: str):
    response = client[collection].find_one({"NAME": stock_name})
    
    if response:
        return response
    