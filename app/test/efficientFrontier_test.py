# 연간(252-x)
# return 값은 이미 구했고

import numpy as np
import pandas as pd
import yfinance as yf

from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint

# 김찬호
kim_info = [
    {"종목": "NVIDIA", "비율": 10, "티커": "NVDA"},
    {"종목": "AFRICA TV", "비율": 10, "티커": "067160.KQ"},
    {"종목": "대한항공", "비율": 10, "티커": "003490.KS"},
    {"종목": "테슬라", "비율": 10, "티커": "TSLA"},
    {"종목": "SK 하이닉스", "비율": 10, "티커": "000660.KS"},
    {"종목": "신한지주", "비율": 10, "티커": "055550.KS"},
    {"종목": "코웨이", "비율": 10, "티커": "021240.KS"},
    {"종목": "마이크로소프트", "비율": 10, "티커": "MSFT"},
    {"종목": "에코프로 BM", "비율": 10, "티커": "247540.KQ"}]

# 전정재
jeon_info1 = [
    {"종목": "Apple Inc.", "비율": 15, "티커": "AAPL"},
    {"종목": "Lockheed Martin Corporation", "비율": 10, "티커": "LMT"},
    {"종목": "Microsoft Corporation", "비율": 10, "티커": "MSFT"},
    {"종목": "Vanguard Index Funds", "비율": 20, "티커": "VOO"},
    {"종목": "SK하이닉스", "비율": 10, "티커": "000660.KS"},
    {"종목": "레인보우로보틱스", "비율": 10, "티커": "277810.KQ"},
    {"종목": "HD현대일렉트릭", "비율": 10, "티커": "267260.KS"},
    {"종목": "한화에어로스페이스", "비율": 10, "티커": "012450.KS"},
    {"종목": "한화에어로스페이스", "비율": 10, "티커": "012450.KS"},
    {"종목": "한화에어로스페이스", "비율": 10, "티커": "012450.KS"}]
    
# 전정재
jeon_info = [
    {"종목": "Apple Inc.", "비율": 15, "티커": "AAPL"},
    {"종목": "Lockheed Martin Corporation", "비율": 10, "티커": "LMT"},
    {"종목": "Microsoft Corporation", "비율": 10, "티커": "MSFT"},
    {"종목": "Vanguard Index Funds", "비율": 20, "티커": "VOO"},
    {"종목": "SK하이닉스", "비율": 10, "티커": "000660.KS"},
    {"종목": "레인보우로보틱스", "비율": 10, "티커": "277810.KQ"},
    {"종목": "HD현대일렉트릭", "비율": 10, "티커": "267260.KS"},
    {"종목": "한화에어로스페이스", "비율": 10, "티커": "012450.KS"},
    {"종목": "제룡전기", "비율": 2.5, "티커": "033100.KQ"},
    {"종목": "풍산", "비율": 2.5, "티커": "103140.KS"}]


# 김태연
kim_t_info = [
    {"종목": "NVIDIA", "비율": 20, "티커": "NVDA"},
    {"종목": "ARM", "비율": 10, "티커": "ARM"},
    {"종목": "인텔", "비율": 10, "티커": "INTC"},
    {"종목": "노보 노디스크", "비율": 20, "티커": "NVO"},
    {"종목": "일라이 릴리", "비율": 20, "티커": "LLY"},
    {"종목": "KODEX 유럽명품 TOP10", "비율": 10, "티커": "456250.KS"},
    {"종목": "KODEX 인도 Nifty 50", "비율": 10, "티커": "453810.KS"}]

# 황인수
hwang_info = [
    {"종목": "NVDA", "비율": 20, "티커": "NVDA"},
    {"종목": "LMT", "비율": 15, "티커": "LMT"},
    {"종목": "OXY", "비율": 14, "티커": "OXY"},
    {"종목": "PSK", "비율": 12.75, "티커": "PSK"},
    {"종목": "ASML", "비율": 12.75, "티커": "ASML"},
    {"종목": "CRM", "비율": 12.75, "티커": "CRM"},
    {"종목": "한미반도체", "비율": 12.75, "티커": "042700.KS"}]

# 이지영
lee_info = [
    {"종목": "AMD", "비율": 11.2, "티커": "AMD"},
    {"종목": "ARM", "비율": 11.1, "티커": "ARM"},
    {"종목": "엔비디아", "비율": 11.1, "티커": "NVDA"},
    {"종목": "ASML", "비율": 11.1, "티커": "ASML"},
    {"종목": "TSMC", "비율": 11.1, "티커": "TSM"},
    {"종목": "코인베이스", "비율": 11.1, "티커": "COIN"},
    {"종목": "하이닉스", "비율": 11.1, "티커": "000660.KS"},
    {"종목": "한미반도체", "비율": 11.1, "티커": "042700.KS"},
    {"종목": "모비스", "비율": 11.1, "티커": "250060.KQ"}]

# 옥준용
ok_info = [
    {"종목": "SK하이닉스", "비율": 8, "티커": "000660.KS"},
    {"종목": "아마존", "비율": 20, "티커": "AMZN"},
    {"종목": "S&P500 ETF", "비율": 20, "티커": "360750.KS"},
    {"종목": "ARIRANG 글로벌 D램반도체 ETF", "비율": 20, "티커": "442580.KS"},
    {"종목": "퀄컴", "비율": 8, "티커": "QCOM"},
    {"종목": "YINN", "비율": 25.9, "티커": "YINN"}]

# 장혜성
jang_info = [
    {"종목": "TIGER S&P500", "비율": 10, "티커": "360750.KS"},
    {"종목": "Direxion Daily 20+ Year Treasury Bull 3X Shares", "비율": 10, "티커": "TMF"},
    {"종목": "iShares Semiconductor ETF", "비율": 10, "티커": "SOXX"},
    {"종목": "한미반도체", "비율": 10, "티커": "042700.KS"},
    {"종목": "HPSP", "비율": 10, "티커": "403870.KQ"},
    {"종목": "ISC", "비율": 10, "티커": "095340.KQ"},
    {"종목": "원익QnC", "비율": 10, "티커": "074600.KQ"},
    {"종목": "유비케어", "비율": 10, "티커": "032620.KQ"},
    {"종목": "기업은행", "비율": 10, "티커": "024110.KS"},
    {"종목": "하나금융지주", "비율": 10, "티커": "086790.KS"}]

# 장혜성
jang_info = [
    {"종목": "TIGER S&P500", "비율": 10, "티커": "360750.KS"},
    {"종목": "iShares Semiconductor ETF", "비율": 10, "티커": "SOXX"},
    {"종목": "한미반도체", "비율": 10, "티커": "042700.KS"},
    {"종목": "코스맥스", "비율": 10, "티커": "192820.KS"},
    {"종목": "ISC", "비율": 10, "티커": "095340.KQ"},
    {"종목": "유비케어", "비율": 10, "티커": "032620.KQ"},
    {"종목": "원익QnC", "비율": 10, "티커": "074600.KQ"},
    {"종목": "알테오젠", "비율": 12, "티커": "196170.KQ"},
    {"종목": "리노공업", "비율": 12.32, "티커": "058470.KQ"}
]

def download_data(ticker, start_date, end_date="2024-06-15"):
    return yf.download(ticker, start=start_date, end=end_date)["Close"]

def calculate_individual_variance(portfolio):
    variances = {}
    for item in portfolio:
        ticker = item["티커"]
        if portfolio == jeon_info:
            if ticker == "012450.KS":
                data = download_data(ticker, "2024-03-22")
            elif ticker == "033100.KQ" or ticker == "103140.KS":
                data = download_data(ticker, "2024-05-02")
            else:
                data = download_data(ticker, "2024-03-08")
        elif portfolio == jang_info:
            if ticker == "058470.KQ" or ticker == "196170.KQ" or ticker == "192820.KS":
                data = download_data(ticker, "2024-04-12")
            else:
                data = download_data(ticker, "2024-03-08")
        elif portfolio == ok_info:
            if ticker == "YINN":
                data = download_data(ticker, "2024-05-03")
            else:
                data = download_data(ticker, "2024-03-08")
        else:
            data = download_data(ticker, "2024-03-08")

        daily_returns = data.pct_change().dropna()
        variances[ticker] = daily_returns.var()
    return variances

def calculate_common_covariance(portfolio):
    returns_data = []
    tickers = [item["티커"] for item in portfolio]

    for item in portfolio:
        ticker = item["티커"]
        data = download_data(ticker, "2024-03-08")
        daily_returns = data.pct_change().dropna()
        returns_data.append(daily_returns)

    combined_returns = pd.concat(returns_data, axis=1, join="inner").dropna()
    combined_returns.columns = tickers

    cov_matrix = combined_returns.cov()
    return cov_matrix

def calculate_portfolio_volatility(portfolio):
    variances = calculate_individual_variance(portfolio)
    cov_matrix = calculate_common_covariance(portfolio)

    weights = np.array([item["비율"] / 100 for item in portfolio])
    tickers = [item["티커"] for item in portfolio]
    
    portfolio_variance = 0

    for i, ticker_i in enumerate(tickers):
        for j, ticker_j in enumerate(tickers):
            if i == j:
                portfolio_variance += weights[i] ** 2 * variances[ticker_i]
            else:
                portfolio_variance += weights[i] * weights[j] * cov_matrix.loc[ticker_i, ticker_j]

    portfolio_volatility = np.sqrt(portfolio_variance)
    return portfolio_volatility



# Calculate the volatility for each portfolio (new function)
kim_volatility = calculate_portfolio_volatility(kim_info)
jeon_volatility = calculate_portfolio_volatility(jeon_info)
kim_t_volatility = calculate_portfolio_volatility(kim_t_info)
hwang_volatility = calculate_portfolio_volatility(hwang_info)
lee_volatility = calculate_portfolio_volatility(lee_info)
ok_volatility = calculate_portfolio_volatility(ok_info)
jang_volatility = calculate_portfolio_volatility(jang_info)

# Print the returns and volatilities
print("김찬호의 포트폴리오 수익률: {:.2f}%".format(kim_return))
print("김찬호의 포트폴리오 변동성: {:.2f}%".format(kim_volatility * 100))

print("Horizon crafter의 포트폴리오 수익률: {:.2f}%".format(jeon_return))
print("Horizon crafter의 포트폴리오 변동성: {:.2f}%".format(jeon_volatility * 100))

print("김태연의 포트폴리오 수익률: {:.2f}%".format(kim_t_return))
print("김태연의 포트폴리오 변동성: {:.2f}%".format(kim_t_volatility * 100))

print("황인수의 포트폴리오 수익률: {:.2f}%".format(hwang_return))
print("황인수의 포트폴리오 변동성: {:.2f}%".format(hwang_volatility * 100))

print("이지영의 포트폴리오 수익률: {:.2f}%".format(lee_return))
print("이지영의 포트폴리오 변동성: {:.2f}%".format(lee_volatility * 100))

print("옥준용의 포트폴리오 수익률: {:.2f}%".format(ok_return))
print("옥준용의 포트폴리오 변동성: {:.2f}%".format(ok_volatility * 100))

print("장혜성의 포트폴리오 수익률: {:.2f}%".format(jang_return))
print("장혜성의 포트폴리오 변동성: {:.2f}%".format(jang_volatility * 100))

