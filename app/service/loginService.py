from app.utils import log_util
from app.dto import loginDto
from app.dao import loginInfodao


def get_user_info(user_info: loginDto.loginRequestDto) -> dict:
    try:
        response = loginInfodao.find_user_info(user_info)
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
    else:
        return response
    
