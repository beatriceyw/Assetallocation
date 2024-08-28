from app.utils import log_util
from app.dao import forgotpasswordDao
from app.dto import forgotpasswordDto

                                
def get_emailCheck(user_dto) -> dict:
    try:
        response = forgotpasswordDao.find_emailCheck(user_dto)
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
    else:
        return response
    
def set_update_password(user_dto) -> dict:
    try:
        response = forgotpasswordDao.update_password(user_dto)
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
    else:
        return response