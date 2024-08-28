from fastapi import APIRouter, Depends, HTTPException, Request, Form, Body
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from app.utils import session, log_util
from app.service import assetInfoService

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    dependencies=[Depends(session.get_session)],
    responses={404: {"description": "Not found"}},
)

@router.get('/assetInfo')
def assetInfoRoute(request: Request):
    
    return templates.TemplateResponse('assetInfo.html', 
                            context={'request':request})

@router.post('/assetInfo/etf_detail')
def post_etf_detail(stock_name: str = Body(embed=True)):
    try:
        response = assetInfoService.get_etf_detail(stock_name)
        
        if response:
            data = {
                "NAME" : response.get('NAME'),
                "RIC" : response.get('RIC'),
                "BLOOMBERG_CODE_EX" : response.get('BLOOMBERG_CODE_EX'),
                "TICKER" : response.get('TICKER'),
                "ID_ISIN" : response.get('ID_ISIN'),
                "FUND_ASSET_CLASS_FOCUS" : response.get('FUND_ASSET_CLASS_FOCUS'),
                "Issue_Market_Cap" : response.get('Issue_Market_Cap'),
                "CUSIP_Code" : response.get('CUSIP_Code')
            }
            return JSONResponse(content=data, status_code=200)
        
        else:
            raise HTTPException(status_code=400, detail="ETF details not found")
    
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")