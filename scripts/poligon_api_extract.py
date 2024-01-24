from extract_aux.url_params_and_headers import get_url
from extract_aux.fetch_data import fetch_data_from_api
from extract_aux.parse_response import json_dict_to_dataframe
from extract_aux.url_params_and_headers import params
from extract_aux.obtain_yesterday_date import obtain_yesterday_date
from common_aux.config_read import config_read

def extract_data(params, **kwargs):

    print('Starting extraction.')
    config = config_read()

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
        cycle_flag = True

        while cycle_flag == True:
            if not url:
                url = get_url(ticker, start_date, end_date, time_frame, frame_multiplier)

            print('Url:', url)
            response = fetch_data_from_api(url, params)
            print('Response:', response)

            if response is not None:
                print("Data fetched successfully!")

                if response['resultsCount'] > 0:
                    responses_list.append(response)

                    next_url = response.get('next_url', None)
                    print('Next url:', next_url)
                    if next_url:
                        url = next_url
                        params = None      
                        next_url = None
                    else:
                        cycle_flag = False
                        
                else:    
                    print("No results for this period.")
                    cycle_flag = False    

            else:
                print("Failed to fetch data.")
                break

    if responses_list:        
        df = json_dict_to_dataframe(responses_list)
        path = '/opt/archives/'
        formatted_yesterday_date = formatted_yesterday_date.replace('-', '.')
        archive_name = 'stocks_bars - ' + formatted_yesterday_date + '.csv'

        df.to_csv(path + archive_name, sep=';', index=False)

    else:
        print('No results for all tickers for this period.')