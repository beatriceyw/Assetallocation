from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi import APIRouter, Depends, HTTPException, Request

def create_session(request: Request, email: str) -> None:
    dict_value = {'email': email}
    
    request.session['email'] = dict_value
    
def get_session(request: Request) -> object:
    session = request.session.get('email')
    
    if not session:
        raise HTTPException(status_code=403, detail="세션이 만료되었습니다. 로그인을 다시 해주세요.")
    else:
        update_session(request, email=session)

def update_session(request: Request, email: str) -> None:
    request.session['email'] = email

def clear_session(request: Request) -> None:
    if request.session:
        request.session.clear()