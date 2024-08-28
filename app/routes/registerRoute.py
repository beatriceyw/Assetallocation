from typing import Annotated
from fastapi import APIRouter, HTTPException, Request, Form, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.service import registerService
from app.utils import hash, log_util

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    responses={404: {"description": "Not found"}},
)

@router.get('/register')
def registerRoute(request: Request):
    
    return templates.TemplateResponse('register.html', 
                            context={'request':request})

@router.post('/register')
def registerRoute(request: Request, firstName: Annotated[str, Form()], lastName: Annotated[str, Form()],
                  email: Annotated[str, Form()], password: Annotated[str, Form()]):
    try:
        password_hash = hash.get_password_hash(password)
        response = registerService.set_user_info(firstName, lastName, email, password_hash)
        if response:
            return templates.TemplateResponse('login_success.html', 
                            context={'request':request})
        else:
            raise HTTPException(status_code=400, detail="email_doubleCheck get failed")
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
@router.post('/register/emailDoubleCheck')
def assetInfoRoute(email: str = Body(embed=True)):
    try:
        response = registerService.get_email_doubleCheck(email)
        if response:
            data = {
                "status": response["status"]
            }
            return JSONResponse(content=data, status_code=200)
        else:
            raise HTTPException(status_code=400, detail="email_doubleCheck get failed")
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    