import yfinance as yf
import pandas as pd


def find_crossovers():
    t = []
    data = yf.download('BTC-USD', start='2024-01-01', progress=False)
    print(data.loc['2024-01-01'])
    data['50-day'] = data['Close'].rolling(window=50).mean()
    data['200-day'] = data['Close'].rolling(window=200).mean()
    print(len(data))
    data_200 = data[data.index >= '2024-07-19']
    data_200.head(5)
    data['Golden_Cross'] = (data['50-day'] > data['200-day']) & (data['50-day'].shift(1) < data['200-day'].shift(1))
    data['Death_Cross'] = (data['50-day'] < data['200-day']) & (data['50-day'].shift(1) >= data['200-day'].shift(1))
    golden_cross_days = data['Golden_Cross'].loc[data['Golden_Cross'] == True]
    death = data['Death_Cross'].loc[data['Death_Cross'] == True]
    result = pd.concat([golden_cross_days, death]).sort_index()
    print(result)
    for i in result.index:
        t.append(str(i).split()[0])
        print(str(i).split()[0])
    return t


def calculate_total_btc_traded():
    max_btc = yf.download('BTC-USD', start='2024-01-01', end='2024-12-31', progress=False)
    max_btc.head()
    max_btc['Max_Price'] = max_btc['Volume'] / max_btc['Close']
    max_btc.head()
    max_index = max_btc['Max_Price'].idxmax()
    max_price = int(max_btc.loc[max_index, 'Max_Price'].iloc[0])
    return max_price


if __name__ == '__main__':
    # Wywołanie funkcji i uzyskanie wyników
    crossover_dates = find_crossovers()
    total_traded = calculate_total_btc_traded()
    # Drukowaniego wyników w żądanym formacie
    print(" ".join(crossover_dates))
    print(total_traded)
    tickers = ['BTC-USD']
    data = yf.download(tickers, start='2022-01-01')
    data.head(10)
