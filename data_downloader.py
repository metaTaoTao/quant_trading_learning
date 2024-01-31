import yfinance as yf

data = yf.download('BTC-USD', start='2020-01-01', end='2024-01-30', interval='1d')

data.to_csv('BTC-USD.csv')