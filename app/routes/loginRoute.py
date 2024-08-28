from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from app.service import loginService
from app.utils import session, hash, log_util
from app.dto import loginDto

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    responses={404: {"description": "Not found"}},
)

@router.get('/login')
def loginRoute(request: Request):
    
    return templates.TemplateResponse('login.html', 
                            context={'request':request})
    
@router.post('/login')
def loginRoute(request: Request, email: Annotated[str, Form()], password: Annotated[str, Form()]):
    try:
        user_info = loginDto.loginRequestDto(email=email)
        response = loginService.get_user_info(user_info)
        if response:
            verify_password = hash.verify_password(password, response.password)
            if verify_password:
                session.create_session(request, email=response.email)
                return templates.TemplateResponse('dashboard.html', 
                                    context={'request':request})
            else:
                data = {
                    "result": 0, 
                    "message": "password"
                }
                return JSONResponse(content=data, status_code=200)
        else:
            data = {
                "result": 0, 
                "message": "Login"
            }
            return JSONResponse(content=data, status_code=200)
            
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
@router.get('/logout')
def loginRoute(request: Request):
    try:
        session.clear_session(request)
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
    else:
        return templates.TemplateResponse('login.html', 
                                context={'request':request})
    
    
