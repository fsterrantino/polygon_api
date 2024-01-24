import requests
import time
from .url_params_and_headers import headers

def fetch_data_from_api(url, params):
    try:
        response = requests.get(url, params=params, headers=headers)
        print('Status code:', response.status_code)
        
        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            print('Retry due to rate limits.')
            
            for i in range(70,0,-1): # Rate limits: 5 requests per minute.
                print(f"Seconds to continue: {i}", end="\r", flush=True)
                time.sleep(1) 

            return fetch_data_from_api(url, params)

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None