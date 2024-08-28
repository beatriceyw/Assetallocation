from datetime import timedelta, timezone, datetime
from app.utils import log_util
from app.database import client
from app.dto import forgotpasswordDto
 
collection = 'user_info'
collection_temp = 'user_info_temp'

def find_emailCheck(email_info: forgotpasswordDto.mailCheck_RequestDto) -> dict:
    try:
        response = client[collection].find_one({"email": email_info.email})
        if response == None:
            return {"status": 0}
        else:
            return {"status": 1}

    except Exception as e:
        log_util.error(f"find_email_doubleCheck: {str(e)}")
        raise Exception(status_code=500, detail="Internal Server Error")

def update_password(user_dto: forgotpasswordDto.updatePassword_RequestDto) -> dict:
    try:
        update_time = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now(timezone(timedelta(hours=9))))
        response = client[collection].update_many({"email": user_dto.email}, {"$set": {"password": user_dto.password, "update_time": update_time}})
        if response == None:
            return {"status": 0}
        else:
            return {"status": 1}

    except Exception as e:
        log_util.error(f"update_password: {str(e)}")
        raise Exception(status_code=500, detail="Internal Server Error")
    