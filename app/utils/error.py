from app.utils import log_util

from fastapi import Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

templates = Jinja2Templates(directory='templates')


async def validation_exception_handler(request: Request, exc: ValidationError):
    log_util.error(f"Validation error: {exc.errors()}")
    
    data = {
        "status_code" : 422,
        "detail" : exc.errors()
    }
    
    return templates.TemplateResponse('error.html', 
                            context={'request':request, 'data': data})


async def http_exception_handler(request: Request, exc: HTTPException):
    log_util.error(f"HTTP error: {exc.detail}")
    
    data = {
        "status_code" : exc.status_code,
        "detail" : exc.detail
    }
    
    return templates.TemplateResponse('error.html', 
                            context={'request':request, 'data': data})

async def global_exception_handler(request: Request, exc: Exception):
    log_util.error(f"Unexpected error: {str(exc)}")
    
    data = {
        "status_code" : 500,
        "detail" : "Internal Server Error"
    }
    
    return templates.TemplateResponse('error.html', 
                            context={'request':request, 'data': data})