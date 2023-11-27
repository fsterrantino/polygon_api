from .api_secrets import api_key

headers = {
    'Authorization': f'Bearer {api_key}'
}

params = {
    'adjusted': 'true'
    , 'sort': 'asc'
    , 'limit': 120

}

def get_url(ticker):

    url = 'https://api.polygon.io/v2/aggs/ticker/'

    url_appending_params = {
        'ticker': ticker
        , 'range': 'range'
        , 'multiplier': 1
        , 'timespam': 'hour'
        , 'from': '2023-11-23' # format: 2023-01-09
        , 'to': '2023-11-24' # format: 2023-01-10
    }

    url_appending = ''
    for key, value in url_appending_params.items():
        if key != 'to':
            url_appending = url_appending + str(value) + '/'
        else:
            url_appending = url_appending + str(value)

    final_url = url + url_appending  
    return final_url

