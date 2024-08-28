from app.utils import log_util
from app.dao import registerdao
from app.dto import registerDto

                                
def set_user_info(firstName: str, lastName: str, email: str, password_hash: str) -> dict:
    try:
        user_dto = registerDto.registerRequestDto(firstName=firstName, lastName=lastName, email=email, password=password_hash)
        response = registerdao.insert_user_info(user_dto)

    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
    else:
        return response

def get_email_doubleCheck(email) -> dict:
    try:
        user_dto = registerDto.mail_DobleCheck_RequestDto(email=email)
        response = registerdao.find_email_doubleCheck(user_dto)
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
    else:
        return response