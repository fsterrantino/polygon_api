import pandas as pd

def json_dict_to_dataframe(json_dicts_list):
    tickers_data = []

    for json_dict in json_dicts_list:
        for result in range(json_dict['resultsCount']):
            ticker = json_dict['results'][result]
            ticker_data = {
                'ticker': json_dict['ticker']
                , 'volume': ticker['v']
                , 'volume_weighted_avg_price': ticker['vw']
                , 'open_price': ticker['o']
                , 'close_price': ticker['c']
                , 'highest_price': ticker['h']
                , 'lowest_price': ticker['l']
                , 'datetime': ticker['t']
                , 'transactions_number': ticker['n']
            }

            tickers_data.append(ticker_data)

    df = pd.DataFrame.from_dict(tickers_data)
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')

    return df