from extract_aux.url_params_and_headers import get_url
from extract_aux.fetch_data import fetch_data_from_api
from extract_aux.parse_response import json_dict_to_dataframe
from extract_aux.url_params_and_headers import params
from extract_aux.obtain_yesterday_date import obtain_yesterday_date
import configparser

def extract_data(params, **kwargs):
    config = configparser.ConfigParser()
    config.sections()
    config.read('/opt/config.ini')

    execution_date = kwargs.get('execution_date')
    formatted_yesterday_date = obtain_yesterday_date(execution_date)

    responses_list = []
    tickers_to_query_list = config['API_PARAMETERS']['tickers_to_query_list']
    tickers_to_query_list = tickers_to_query_list.split(', ')
    start_date = formatted_yesterday_date
    end_date = formatted_yesterday_date
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

    path = '/opt/archives/'
    formatted_yesterday_date = formatted_yesterday_date.replace('-', '.')
    archive_name = 'stocks_bars - ' + formatted_yesterday_date + '.csv'

    df.to_csv(path + archive_name, sep=';', index=False)