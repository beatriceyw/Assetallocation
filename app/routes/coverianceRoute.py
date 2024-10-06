import ast
import pandas as pd
import yfinance as yf

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from app.utils import session, log_util, mp_util

import numpy as np
import json
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/assetAllocation",
    tags=[""],
    dependencies=[Depends(session.get_session)],
    responses={404: {"description": "Not found"}},
)

@router.get('/coveriance')
def get_coveriance(request: Request):
    try:
        start_date = "2002-02-22"
        end_date = "2024-06-20"
        
        # IGLB(장기투자채권), HYG(고수익채권), SPY(S&P500), MBB(모기지), SOXX(반도체), URA(핵), PAVE(인프라) 
        mp1 = mp_util.mp_coveriance(start_date, end_date, ['IGLB', 'HYG', 'SPY', 'MBB', 'SOXX', 'URA', 'PAVE'])
        #sp500 반도체 나스닥 삼성전자 LG전자 현대차 삼성SDI
        mp2 = mp_util.mp_coveriance(start_date, end_date, ['SPY', 'SOXX', 'NDAQ', '005930.KS', '066570.KS', '005380.KS', '006400.KS'])
        # 나스닥 sp500 코스피
        mp3 = mp_util.mp_coveriance(start_date, end_date, ['NDAQ', 'SPY', '^KS11'])
        
        if mp1 and mp2 and mp3:
            data = {
                "mp1" : mp1,
                "mp2" : mp2,
                "mp3" : mp3
            }
            
            return templates.TemplateResponse('coveriance.html', 
                                    context={'request':request, "data": data})
        else:
            raise HTTPException(status_code=400, detail="get_coveriance error")
    
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")

    
@router.post('/coveriance')
def post_coveriance(mp_ver: Annotated[str, Form()], start_date: Annotated[str, Form()], end_date: Annotated[str, Form()], tickers: Annotated[str, Form()]):
    try:
        tickers = ast.literal_eval(tickers)
        if mp_ver == "MP1":
            # IGLB(장기투자채권), HYG(고수익채권), SPY(S&P500), MBB(모기지), SOXX(반도체), URA(핵), PAVE(인프라) 
            mp_data = mp_util.mp_coveriance(start_date, end_date, tickers)
        elif mp_ver == "MP2":
            #sp500 반도체 나스닥 삼성전자 LG전자 현대차 삼성SDI
            mp_data = mp_util.mp_coveriance(start_date, end_date, tickers)
        elif mp_ver == "MP3":
            # 나스닥 sp500 코스피
            mp_data = mp_util.mp_coveriance(start_date, end_date, tickers)
        
        if mp_data:
            data = {
                "result": 1, 
                "covar_html_thead": mp_data.get("covar_html_thead"),
                "covar_html_tbody": mp_data.get("covar_html_tbody")
            }
            return JSONResponse(content=data, status_code=200)
        else:
            raise HTTPException(status_code=400, detail="post_coveriance error")
        
    except Exception as e:
        log_util.error(f"500 Internal Server Error: {e}")
        raise Exception(status_code=500, detail="Internal Server Error")