from datetime import timedelta, timezone, datetime
from app.utils import log_util
from app.database import client
from app.dto import registerDto
 
collection = 'user_info'
collection_temp = 'user_info_temp'

def insert_user_info(user_dto: registerDto.registerRequestDto) -> dict:
    try:
        create_dto = user_dto.dict()
        create_dto['insert_time'] = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now(timezone(timedelta(hours=9))))
        response = client[collection].insert_one(create_dto)

        if response.acknowledged:
            return {"status": 1}
        else:
            log_util.error("데이터 삽입 실패: acknowledged=False")
            raise Exception(status_code=500, detail="Internal Server Error")
        
    except Exception as e:
        log_util.error(f"insert_user_info: {str(e)}")
        raise Exception(status_code=500, detail="Internal Server Error")
    

def find_email_doubleCheck(email_info: registerDto.mail_DobleCheck_RequestDto) -> dict:
    try:
        response = client[collection].find_one({"email": email_info.email})
        if response == None:
            return {"status": 0}
        else:
            return {"status": 1}

    except Exception as e:
        log_util.error(f"find_email_doubleCheck: {str(e)}")
        raise Exception(status_code=500, detail="Internal Server Error")
