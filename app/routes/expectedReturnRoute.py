import ast
import json

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from app.utils import session, log_util, mp_util

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    dependencies=[Depends(session.get_session)],
    responses={404: {"description": "Not found"}},
)
  
@router.get('/expectedReturn')
def get_expectedReturnRoute(request: Request):
    
    return templates.TemplateResponse('expectedReturn.html', 
                            context={'request':request})
    
@router.post('/expectedReturn/efficientFrontier')
def post_expectedReturn(start_date: Annotated[str, Form()], end_date: Annotated[str, Form()], tickers: Annotated[str, Form()]):
    try:
        tickers = ast.literal_eval(tickers)
        
        efficientFrontier_data = mp_util.efficientFrontier(start_date, end_date, tickers)
    
        if efficientFrontier_data:
            
            data = {
                "result": 1,
                "vol_arr": efficientFrontier_data.get("vol_arr"),
                "ret_arr": efficientFrontier_data.get("ret_arr"),
                "all_weights": efficientFrontier_data.get("all_weights"),
                "returns": efficientFrontier_data.get("returns")
            }
            
            json_object = json.dumps(data)
            
            return JSONResponse(content=json_object, status_code=200)
        
        else:
            raise HTTPException(status_code=400, detail="post_expectedReturn error")
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")
    
