import yfinance as yf

# 올바른 티커 심볼 목록
tickers = ["IGLB", "HYG", "SPY", "MBB", "SOXX", "URA", "PAVE"]

# 각 티커에 대해 데이터 다운로드 시도
try:
    yf.download(tickers, ignore_tz=True)['Adj Close']
except Exception as e:
    print("error")