from .api_secrets import api_key

headers = {
    'Authorization': f'Bearer {api_key}'
}

params = {
    'adjusted': 'true'
    , 'sort': 'asc'
    , 'limit': 24

}

def get_url(ticker, start_date, end_date, time_frame, frame_multiplier):

    url = 'https://api.polygon.io/v2/aggs/ticker/'

    url_appending_params = {
        'ticker': ticker
        , 'range': 'range'
        , 'multiplier': frame_multiplier
        , 'timespam': time_frame
        , 'from': start_date # format: 2023-01-09
        , 'to': end_date # format: 2023-01-10
    }

    url_appending = ''
    for key, value in url_appending_params.items():
        if key != 'to':
            url_appending = url_appending + str(value) + '/'
        else:
            url_appending = url_appending + str(value)

    final_url = url + url_appending  
    return final_url

