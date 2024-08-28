from fastapi import APIRouter, Depends, HTTPException, Request, Form, Body
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from app.utils import session, hash, log_util
from app.service import forgotpasswordService
from app.dto import forgotpasswordDto

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    responses={404: {"description": "Not found"}},
)

@router.get('/forgot_password')
def forgotPasswordRoute(request: Request):
    
    return templates.TemplateResponse('forgot_password.html', 
                            context={'request':request})

@router.post('/forgot_password/emailCheck')
def emailCheckRoute(email: str = Body(embed=True)):
    try:
        user_dto = forgotpasswordDto.mailCheck_RequestDto(email=email)
        response = forgotpasswordService.get_emailCheck(user_dto)
        if response:
            data = {
                "status": response["status"]
            }
            return JSONResponse(content=data, status_code=200)
        else:
            raise HTTPException(status_code=400, detail="emailCheck get failed")

    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
@router.post('/forgot_password/passwordUpdate')
def passwordUpdateRoute(email: str = Body(embed=True), password: str = Body(embed=True)):
    try:
        password_hash = hash.get_password_hash(password)
        user_dto = forgotpasswordDto.updatePassword_RequestDto(email=email, password=password_hash)
        response = forgotpasswordService.set_update_password(user_dto)
        if response:
            data = {
                "status": response["status"]
            }
            return JSONResponse(content=data, status_code=200)
        
        else:
            raise HTTPException(status_code=400, detail="Password update failed")
    
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    