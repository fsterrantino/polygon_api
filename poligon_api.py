from scripts.url_params_and_headers import params, headers, get_url
from scripts.fetch_data import fetch_data_from_api
from scripts.parse_response import json_dict_to_dataframe

responses_list = []
# tickers_to_query_list = ['AAPL']
tickers_to_query_list = ['AAPL', 'AMZN']
start_date = '2023-11-27'
end_date = '2023-11-27'
time_frame = 'hour'
frame_multiplier = 1

for ticker in tickers_to_query_list:

    while True:
        url = None
        if not url:
            url = get_url(ticker, start_date, end_date, time_frame, frame_multiplier)

        response = fetch_data_from_api(url, params, headers)

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
df.to_csv('stocks_bars.csv', sep=';')