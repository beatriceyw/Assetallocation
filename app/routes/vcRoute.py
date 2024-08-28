from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request, Form, Body
from fastapi.templating import Jinja2Templates
from app.utils import session, log_util

templates = Jinja2Templates(directory='templates')

# 세션 미들웨어 추가
app = FastAPI()

# MongoRepo = MongoRepo()

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    dependencies=[Depends(session.get_session)],
    responses={404: {"description": "Not found"}},
)

@router.get('/vc')
def assetInfoRoute(request: Request):
    
    return templates.TemplateResponse('vc.html', 
                            context={'request':request})

