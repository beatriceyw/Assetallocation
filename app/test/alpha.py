import yfinance as yf
import pandas as pd
from pyetfdb_scraper.etf import ETF, load_etfs

pd.set_option('display.max_rows', None)  # 모든 행 출력
pd.set_option('display.max_columns', None)  # 모든 열 출력
pd.set_option('display.expand_frame_repr', False)  # 가로로 잘리지 않고 한 줄에 출력
pd.set_option('display.max_colwidth', None)  # 열 너비 제한 없애기

# 전고점 대비 하락율을 계산하는 함수
def get_drawdown_percentage(ticker):
    data = yf.Ticker(ticker)
    hist = data.history(period="max")
    
    if data and not hist.empty:
        longName = data.info.get('longName', 'N/A')
        max_price = hist['Close'].max()
        current_price = hist['Close'].iloc[-1]
        drawdown_percentage = ((max_price - current_price) / max_price) * 100
        return drawdown_percentage, longName

# 50% 이상 하락한 ETF 찾기
def find_etf_with_drawdown():
    etfs = load_etfs()
    result = []
    for ticker in etfs:
        try:
            drawdown, longName = get_drawdown_percentage(ticker)
            if drawdown and drawdown >= 50:
                print(ticker)
                result.append({'Ticker': ticker, 'Name': longName, 'Drawdown (%)': drawdown})
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
    
    # 결과를 DataFrame으로 변환
    df_result = pd.DataFrame(result)
    return df_result

df_result = find_etf_with_drawdown()
df_result.to_csv('etf_drawdown_results.csv', index=False)
# 결과 출력

