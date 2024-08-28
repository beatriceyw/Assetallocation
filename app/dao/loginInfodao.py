from datetime import timedelta, timezone, datetime
from bson import ObjectId

from app.utils import log_util
from app.database import client
from app.dto import loginDto
from app.models import loginModels
 
collection = 'user_info'
collection_temp = 'user_info_temp'


def find_user_info(user_info: loginDto.loginRequestDto) -> dict:
    response = client[collection].find_one({"email": user_info.email})

    if response:
        return loginModels.userInfoModel(response)