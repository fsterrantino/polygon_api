import requests
import time

def fetch_data_from_api(url, params, headers):
    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        if response.status_code == 429:
            print('Consulta reintentada por rate limits.')
            
            for i in range(60,0,-1): # Rate limits: 5 requests per minute.
                print(f"Seconds to continue: {i}", end="\r", flush=True)
                time.sleep(1) 

            fetch_data_from_api(url, params, headers)
        else:
            response.raise_for_status()

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None