from scripts.url_params_and_headers import get_url
from scripts.fetch_data import fetch_data_from_api
from scripts.parse_response import json_dict_to_dataframe
from scripts.url_params_and_headers import params
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

responses_list = []
# tickers_to_query_list = ['AAPL']
tickers_to_query_list = config['API_PARAMETERS']['tickers_to_query_list']
tickers_to_query_list = tickers_to_query_list.split(', ')
start_date = config['API_PARAMETERS']['start_date']
end_date = config['API_PARAMETERS']['end_date']
time_frame = config['API_PARAMETERS']['time_frame']
frame_multiplier = config['API_PARAMETERS']['frame_multiplier']

for ticker in tickers_to_query_list:
    url = None
    while True:
        if not url:
            url = get_url(ticker, start_date, end_date, time_frame, frame_multiplier)
            print(url)
        response = fetch_data_from_api(url, params)
        print(response)

        if response is not None:
            print("Data fetched successfully!")
        else:
            print("Failed to fetch data.")
            break

        if response['resultsCount'] == 0:
            print("No results for this period.")

        responses_list.append(response)
        next_url = response.get('next_url', None)

        if next_url:
            url = next_url
            params = None      
            next_url = None
        else:
            break

df = json_dict_to_dataframe(responses_list)
print(df)
df.to_csv('stocks_bars.csv', sep=';', index=False)