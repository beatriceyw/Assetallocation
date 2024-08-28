import ast
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
    
        
# @router.get('/expectedReturn')
# def expectedReturnRoute(request: Request):
    
#     return templates.TemplateResponse('expectedReturn.html', 
#                             context={'request':request})
    
# @router.post('/expectedReturn/efficientFrontier')
# def expectedReturnRoute(request: Request):

#     # 티커 리스트
#     # tickers = ['IGLB', 'HYG', 'SPY', 'MBB', 'SOXX', 'URA', 'PAVE', 'KR10YT=RR']
#     tickers = ['IGLB', 'HYG', 'SPY', 'MBB', 'SOXX', 'URA', 'PAVE']

#     # 각 티커별 수익률을 직접 입력
#     returns = [0.046, 0.046, 0.13, 0.02, 0.18, 0.16, 0.012]  # 예시 수익률
    
#     df = pd.DataFrame(data=[returns], columns=tickers)

#     # 연간화된 수익률 계산
#     r = df.iloc[0] * 100

#     # yfinance를 사용하여 과거 데이터 가져오기 (최근 1년치 데이터)
#     data = yf.download(tickers, start="2014-01-01")['Adj Close']

#     # 일간 수익률 계산
#     historical_returns = data.pct_change(fill_method=None).dropna()

#     # 공분산 행렬 계산
#     covar = historical_returns.cov()

#     # 포트폴리오의 수익률과 변동성 계산 함수
#     def ret(r, w):
#         return r.dot(w)

#     def vol(w, covar):
#         return np.sqrt(np.dot(w, np.dot(covar, w)))

#     # 개별 자산의 최소 5%, 최대 50% 가중치 제약 설정
#     min_weight = 0.05
#     max_weight = 0.5
#     bounds = Bounds([min_weight] * len(tickers), [max_weight] * len(tickers))

#     linear_constraint = LinearConstraint(np.ones((len(tickers),)), [1], [1])
#     weights = np.ones(len(tickers)) / len(tickers)  # 초기 가중치를 동등하게 설정
#     x0 = weights

#     # 최소 변동성 포트폴리오 찾기
#     fun1 = lambda w: vol(w, covar)
#     res = minimize(fun1, x0, method='trust-constr', constraints=linear_constraint, bounds=bounds)
#     w_min = res.x

#     np.set_printoptions(suppress=True, precision=2)

#     # 최대 샤프 비율 포트폴리오 찾기
#     fun2 = lambda w: -ret(r, w) / vol(w, covar)
#     res_sharpe = minimize(fun2, x0, method='trust-constr', constraints=linear_constraint, bounds=bounds)
#     w_sharpe = res_sharpe.x

#     w = w_min
#     num_ports = 100
#     gap = (ret(r, w_sharpe) - ret(r, w_min)) / (num_ports - 1)

#     all_weights = np.zeros((num_ports, len(df.columns)))
#     ret_arr = np.zeros(num_ports)
#     vol_arr = np.zeros(num_ports)
    
#     for i in range(num_ports):
#         port_ret = ret(r, w_min) + i * gap
#         double_constraint = LinearConstraint([np.ones(len(tickers)), r], [1, port_ret], [1, port_ret])
        
#         x0 = w_min
#         fun = lambda w: vol(w, covar)
#         a = minimize(fun, x0, method='trust-constr', constraints=double_constraint, bounds=bounds)
        
#         all_weights[i, :] = a.x
#         ret_arr[i] = port_ret
#         vol_arr[i] = vol(a.x, covar)

#     json_object = {
#         "vol_arr": vol_arr.tolist(),
#         "ret_arr": ret_arr.tolist(),
#         "all_weights": all_weights.tolist(),
#         "returns": returns
#     }

#     json_string = json.dumps(json_object)
    
#     return JSONResponse(data={"result": 1, "data": json_string}, status_code=200)
