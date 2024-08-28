from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from app.utils import session, log_util

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    dependencies=[Depends(session.get_session)],
    responses={404: {"description": "Not found"}},
)

@router.get('/dashboard')
def indexRoute(request: Request):

    return templates.TemplateResponse('dashboard.html', 
                            context={'request':request})
