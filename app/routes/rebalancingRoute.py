import ast

from fastapi import APIRouter, Depends, HTTPException, Request, Form, Body
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

@router.get('/rebalancing')
def getRebalancing(request: Request):
    
    return templates.TemplateResponse('rebalancing.html', 
                            context={'request':request})
    
@router.post('/rebalancing')
def postRebalancing(mp_ver: str = Body(embed=True), risk_gauge: str = Body(embed=True), tickers: str = Body(embed=True), start_date: str = Body(embed=True), end_date: str = Body(embed=True)):
    try:
        tickers = ast.literal_eval(tickers)
        index_data = ['NDAQ', 'SPY', '^KS11']
        
        if mp_ver == "MP1":
            if risk_gauge == "low":
                mp_data = mp_util.mp_set_min_volatility(tickers, start_date, end_date)
                index_data = mp_util.mp_set_min_volatility(index_data, start_date, end_date)
            elif risk_gauge == "medium":
                mp_data = mp_util.mp_set_medium(tickers, start_date, end_date)  
                index_data = mp_util.mp_set_medium(index_data, start_date, end_date)
            elif risk_gauge == "high":
                mp_data = mp_util.mp_set_max_sharpe(tickers, start_date, end_date)
                index_data = mp_util.mp_set_max_sharpe(index_data, start_date, end_date)
                
        elif mp_ver == "MP2":
            if risk_gauge == "low":
                mp_data = mp_util.mp_set_min_volatility(tickers, start_date, end_date)
                index_data = mp_util.mp_set_min_volatility(index_data, start_date, end_date)
            elif risk_gauge == "medium":
                mp_data = mp_util.mp_set_medium(tickers, start_date, end_date)  
                index_data = mp_util.mp_set_medium(index_data, start_date, end_date)
            elif risk_gauge == "high":
                mp_data = mp_util.mp_set_max_sharpe(tickers,start_date, end_date)
                index_data = mp_util.mp_set_max_sharpe(index_data, start_date, end_date)
                
        elif mp_ver == "MP3":
            if risk_gauge == "low":
                mp_data = mp_util.mp_set_min_volatility(tickers, start_date, end_date)
                index_data = mp_util.mp_set_min_volatility(index_data, start_date, end_date)
            elif risk_gauge == "medium":
                mp_data = mp_util.mp_set_medium(tickers, start_date, end_date)   
                index_data = mp_util.mp_set_medium(index_data, start_date, end_date)
            elif risk_gauge == "high":
                mp_data = mp_util.mp_set_max_sharpe(tickers, start_date, end_date)
                index_data = mp_util.mp_set_max_sharpe(index_data, start_date, end_date)

        if mp_data or index_data:
            data = {
                "weights": mp_data.get('weights').tolist(),
                "cagr_returns": mp_data.get('cagr_returns').tolist(),
                "cagr_vol": mp_data.get('cagr_vol').tolist(),
                "sharpe_ratio": mp_data.get('sharpe_ratio'),
                "port_ret":mp_data.get('port_ret'),
                "port_vol": mp_data.get('port_vol'),
                "index_port_ret":index_data.get('cagr_returns').tolist(),
                "index_port_vol": index_data.get('cagr_vol').tolist(),
            }
            return JSONResponse(content=data, status_code=200)
        
        else:
            raise HTTPException(status_code=400, detail="ETF details not found")
    
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")

