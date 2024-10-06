import numpy as np
import pandas as pd
import yfinance as yf
import math

from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint

# model 포플 riskgauge == 상
def mp_set_max_sharpe(tickers):

    np.set_printoptions(suppress=True, precision=2)
    
    # 다운로드할 데이터프레임 초기화
    df1 = pd.DataFrame()

    # 주가 데이터 다운로드
    for t in tickers:
        df1[t] = yf.download(t, ignore_tz=True)['Adj Close']

    # 일일 수익률 계산
    df2 = df1.pct_change(fill_method=None)

    # 첫 번째 행의 NaN 값 제거
    df = df2.iloc[1:, :]

    # Calculate CAGR and years dynamically for each ticker
    cagr = {}
    years = {}
    
    for t in tickers:
        data = df1[t].dropna()
        num_years = math.trunc((data.index[-1] - data.index[0]).days / 365.25)
        years[t] = num_years
        cagr[t] = (data.iloc[-1] / abs(data.iloc[0])) ** (1 / num_years) - 1
    
    cagr = pd.Series(cagr)
    years = pd.Series(years)

    # 연간 변동성 계산
    annual_volatility = df.std() * np.sqrt(252)

    # 공분산 행렬 계산
    covar = df.cov() * 252  # 연간 공분산 행렬로 변환

    # 포트폴리오의 기대수익률과 변동성 계산 함수
    def portfolio_return(cagr, weights):
        return np.dot(cagr, weights)

    def portfolio_volatility(weights, covar):
        return np.sqrt(np.dot(weights.T, np.dot(covar, weights)))

    # 가중치 제약 설정
    min_weight = 0.05
    max_weight = 0.5
    bounds = Bounds([min_weight] * len(tickers), [max_weight] * len(tickers))
    linear_constraint = LinearConstraint(np.ones(len(tickers)), [1], [1])

    # 초기 가중치 설정
    initial_weights = np.ones(len(tickers)) / len(tickers)

    # 최대 샤프 비율 포트폴리오 찾기
    risk_free_rate = 0.03
    max_sharpe = lambda weights: -(portfolio_return(cagr, weights) - risk_free_rate) / portfolio_volatility(weights, covar)
    opt_result_max_sharpe = minimize(max_sharpe, initial_weights, method='trust-constr', constraints=[linear_constraint], bounds=bounds)
    # Maximum Sharpe Ratio Portfolio Weights
    w_max_sharpe = opt_result_max_sharpe.x

    # 결과 출력
    max_sharpe_port_return = portfolio_return(cagr, w_max_sharpe)
    max_sharpe_port_volatility = portfolio_volatility(w_max_sharpe, covar)
    max_sharpe_ratio = (max_sharpe_port_return - risk_free_rate) / max_sharpe_port_volatility

    data = {
        "weights": np.round(w_max_sharpe, 2),
        "cagr_returns": np.round(cagr, 2),
        "cagr_vol": round(annual_volatility, 2),
        "sharpe_ratio": round(max_sharpe_ratio, 2),
        "port_ret":round(max_sharpe_port_return,2),
        "port_vol": round(max_sharpe_port_volatility, 2),
    }

    return data
# model 포플 riskgauge == 하
def mp_set_min_volatility(tickers):

    np.set_printoptions(suppress=True, precision=2)
    
    # 다운로드할 데이터프레임 초기화
    df1 = pd.DataFrame()

    # 주가 데이터 다운로드
    for t in tickers:
        df1[t] = yf.download(t, ignore_tz=True)['Adj Close']

    # 일일 수익률 계산
    df2 = df1.pct_change(fill_method=None)

    # 첫 번째 행의 NaN 값 제거
    df = df2.iloc[1:, :]

    # Calculate CAGR and years dynamically for each ticker
    cagr = {}
    years = {}
    for t in tickers:
        data = df1[t].dropna()
        num_years = math.trunc((data.index[-1] - data.index[0]).days / 365.25)
        years[t] = num_years
        cagr[t] = (data.iloc[-1] / abs(data.iloc[0])) ** (1 / num_years) - 1
    
    cagr = pd.Series(cagr)
    years = pd.Series(years)

    # 연간 변동성 계산
    annual_volatility = df.std() * np.sqrt(252)

    # 공분산 행렬 계산
    covar = df.cov() * 252  # 연간 공분산 행렬로 변환

    # 포트폴리오의 기대수익률과 변동성 계산 함수
    def portfolio_return(cagr, weights):
        return np.dot(cagr, weights)

    def portfolio_volatility(weights, covar):
        return np.sqrt(np.dot(weights.T, np.dot(covar, weights)))

    # 가중치 제약 설정
    min_weight = 0.05
    max_weight = 0.5
    bounds = Bounds([min_weight] * len(tickers), [max_weight] * len(tickers))
    linear_constraint = LinearConstraint(np.ones(len(tickers)), [1], [1])

    # 초기 가중치 설정
    initial_weights = np.ones(len(tickers)) / len(tickers)

    # 최소 변동성 포트폴리오 찾기
    min_volatility = lambda weights: portfolio_volatility(weights, covar)
    opt_result_min_vol = minimize(min_volatility, initial_weights, method='trust-constr', constraints=[linear_constraint], bounds=bounds)
    # Minimum Volatility Portfolio Weights
    w_min_vol = opt_result_min_vol.x

    # 최대 샤프 비율 포트폴리오 찾기
    risk_free_rate = 0.03
    max_sharpe = lambda weights: -(portfolio_return(cagr, weights) - risk_free_rate) / portfolio_volatility(weights, covar)
    opt_result_max_sharpe = minimize(max_sharpe, initial_weights, method='trust-constr', constraints=[linear_constraint], bounds=bounds)
    # Maximum Sharpe Ratio Portfolio Weights
    w_max_sharpe = opt_result_max_sharpe.x

    # 결과 출력
    min_vol_port_return = portfolio_return(cagr, w_min_vol)
    min_vol_port_volatility = portfolio_volatility(w_min_vol, covar)
    min_sharpe_ratio = (min_vol_port_return - risk_free_rate) / min_vol_port_volatility

    data = {
        "weights": np.round(w_max_sharpe, 2),
        "cagr_returns": np.round(cagr, 2),
        "cagr_vol": round(annual_volatility, 2),
        "sharpe_ratio": round(min_sharpe_ratio, 2),
        "port_ret":round(min_vol_port_return,2),
        "port_vol": round(min_vol_port_volatility, 2),
    }
    
    return data
# model 포플 riskgauge == 중
def mp_set_medium(tickers):
    
    np.set_printoptions(suppress=True, precision=2)
    
    # 다운로드할 데이터프레임 초기화
    df1 = pd.DataFrame()

    # 주가 데이터 다운로드
    for t in tickers:
        df1[t] = yf.download(t, ignore_tz=True)['Adj Close']

    # 일일 수익률 계산
    df2 = df1.pct_change(fill_method=None)

    # 첫 번째 행의 NaN 값 제거
    df = df2.iloc[1:, :]

    # Calculate CAGR and years dynamically for each ticker
    cagr = {}
    years = {}
    for t in tickers:
        data = df1[t].dropna()
        num_years = math.trunc((data.index[-1] - data.index[0]).days / 365.25)
        years[t] = num_years
        cagr[t] = (data.iloc[-1] / abs(data.iloc[0])) ** (1 / num_years) - 1
    
    cagr = pd.Series(cagr)
    years = pd.Series(years)

    # 연간 변동성 계산
    annual_volatility = df.std() * np.sqrt(252)

    # 공분산 행렬 계산
    covar = df.cov() * 252  # 연간 공분산 행렬로 변환

    # 포트폴리오의 기대수익률과 변동성 계산 함수
    def portfolio_return(cagr, weights):
        return np.dot(cagr, weights)

    def portfolio_volatility(weights, covar):
        return np.sqrt(np.dot(weights.T, np.dot(covar, weights)))

    # 가중치 제약 설정
    min_weight = 0.05
    max_weight = 0.5
    bounds = Bounds([min_weight] * len(tickers), [max_weight] * len(tickers))
    linear_constraint = LinearConstraint(np.ones(len(tickers)), [1], [1])

    # 초기 가중치 설정
    initial_weights = np.ones(len(tickers)) / len(tickers)

    # 최소 변동성 포트폴리오 찾기
    min_volatility = lambda weights: portfolio_volatility(weights, covar)
    opt_result_min_vol = minimize(min_volatility, initial_weights, method='trust-constr', constraints=[linear_constraint], bounds=bounds)
    # Minimum Volatility Portfolio Weights
    w_min_vol = opt_result_min_vol.x

    # 최대 샤프 비율 포트폴리오 찾기
    risk_free_rate = 0.03
    max_sharpe = lambda weights: -(portfolio_return(cagr, weights) - risk_free_rate) / portfolio_volatility(weights, covar)
    opt_result_max_sharpe = minimize(max_sharpe, initial_weights, method='trust-constr', constraints=[linear_constraint], bounds=bounds)
    # Maximum Sharpe Ratio Portfolio Weights
    w_max_sharpe = opt_result_max_sharpe.x

    # 결과 출력
    min_vol_port_return = portfolio_return(cagr, w_min_vol)
    min_vol_port_volatility = portfolio_volatility(w_min_vol, covar)
    min_sharpe_ratio = (min_vol_port_return - risk_free_rate) / min_vol_port_volatility
    max_sharpe_port_return = portfolio_return(cagr, w_max_sharpe)
    max_sharpe_port_volatility = portfolio_volatility(w_max_sharpe, covar)
    max_sharpe_ratio = (max_sharpe_port_return - risk_free_rate) / max_sharpe_port_volatility

    # Calculate the midpoint of returns
    midpoint_weight = (w_min_vol + w_max_sharpe) / 2
    midpoint_return = (min_vol_port_return + max_sharpe_port_return) / 2
    midpoint_volatility = (min_vol_port_volatility + max_sharpe_port_volatility) / 2
    midpoint_sharpe_ratio = (min_sharpe_ratio + max_sharpe_ratio) / 2
    

    data = {
        "weights": np.round(midpoint_weight, 2),
        "cagr_returns": np.round(cagr, 2),
        "cagr_vol": round(annual_volatility, 2),
        "sharpe_ratio": round(midpoint_sharpe_ratio, 2),
        "port_ret":round(midpoint_return,2),
        "port_vol": round(midpoint_volatility, 2),
    }

    return data
# model 포플 상관계수(공분산)
def mp_coveriance(start_date, end_date, tickers):
    np.set_printoptions(suppress=True, precision=2)
    
    # 다운로드할 데이터프레임 초기화
    df1 = pd.DataFrame()

    # 주가 데이터 다운로드
    for t in tickers:
        df1[t] = yf.download(t, start=start_date, end=end_date, ignore_tz=True)['Adj Close']

    # 일일 수익률 계산
    df2 = df1.pct_change(fill_method=None)

    # 첫 번째 행의 NaN 값 제거
    df = df2.iloc[1:, :]

    # 공분산 행렬 계산
    covar = df.cov() * 252  # 연간 공분산 행렬로 변환

    # 결과 출력
    covar_html = covar.to_html()
    start_thead = covar_html.find('<thead>')
    end_thead = covar_html.find('</thead>') + len('</thead>')
    start_tbody = covar_html.find('<tbody>')
    end_tbody = covar_html.find('</tbody>') + len('</tbody>')
    covar_thead = covar_html[start_thead:end_thead]
    covar_tbody = covar_html[start_tbody:end_tbody]

    data = {
        "covar_html_thead" : covar_thead,
        "covar_html_tbody" : covar_tbody
    }

    return data
# Efficient Frontier
def efficientFrontier(start_date, end_date, tickers): 
    
    # 각 티커별 수익률을 직접 입력
    returns = [0.046, 0.046, 0.13, 0.02, 0.18, 0.16, 0.012]  # 예시 수익률
    
    df = pd.DataFrame(data=[returns], columns=tickers)

    # 연간화된 수익률 계산
    r = df.iloc[0] * 100

    # yfinance를 사용하여 과거 데이터 가져오기 (최근 1년치 데이터)
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

    # 일간 수익률 계산
    historical_returns = data.pct_change(fill_method=None).dropna()

    # 공분산 행렬 계산
    covar = historical_returns.cov()

    # 포트폴리오의 수익률과 변동성 계산 함수
    def ret(r, w):
        return r.dot(w)

    def vol(w, covar):
        return np.sqrt(np.dot(w, np.dot(covar, w)))

    # HHI 계산 함수
    def hhi(w):
        return np.sum(np.square(w)) * 10000  # HHI 계산 (0~10000 범위)

    # 개별 자산의 최소 5%, 최대 50% 가중치 제약 설정
    min_weight = 0.05
    max_weight = 0.5
    bounds = Bounds([min_weight] * len(tickers), [max_weight] * len(tickers))

    linear_constraint = LinearConstraint(np.ones((len(tickers),)), [1], [1])
    weights = np.ones(len(tickers)) / len(tickers)  # 초기 가중치를 동등하게 설정
    x0 = weights

    # 최소 변동성 포트폴리오 찾기
    fun1 = lambda w: vol(w, covar)
    res = minimize(fun1, x0, method='trust-constr', constraints=linear_constraint, bounds=bounds)
    w_min = res.x

    np.set_printoptions(suppress=True, precision=2)

    # 최대 샤프 비율 포트폴리오 찾기
    fun2 = lambda w: -ret(r, w) / vol(w, covar)
    res_sharpe = minimize(fun2, x0, method='trust-constr', constraints=linear_constraint, bounds=bounds)
    w_sharpe = res_sharpe.x

    w = w_min
    num_ports = 200
    gap = (ret(r, w_sharpe) - ret(r, w_min)) / (num_ports - 1)

    all_weights = np.zeros((num_ports, len(df.columns)))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    
    for i in range(num_ports):
        port_ret = ret(r, w_min) + i * gap
        double_constraint = LinearConstraint([np.ones(len(tickers)), r], [1, port_ret], [1, port_ret])
        
        x0 = w_min
        fun = lambda w: vol(w, covar)
        a = minimize(fun, x0, method='trust-constr', constraints=double_constraint, bounds=bounds)
        
        if a.success and hhi(a.x) <= 4000:  # HHI 4000 이하 필터링
            all_weights[i, :] = a.x
            ret_arr[i] = port_ret
            vol_arr[i] = vol(a.x, covar)
        else:
            print(f"Optimization failed at portfolio {i}")

    data = {
        "vol_arr": vol_arr.tolist(),
        "ret_arr": np.round(ret_arr, 2).tolist(),
        "all_weights": np.round(all_weights, 2).tolist(),
        "returns": returns
    }
    
    print(len(vol_arr.tolist()))
    
    return data
    