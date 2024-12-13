import pandas as pd
import time
import requests
from datetime import datetime

currency_df = pd.DataFrame(columns=['Время', 'USD/EUR'])

url = "https://api.exchangerate-api.com/v4/latest/USD"

def fetch_currency_rate():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            usd_to_eur = data['rates']['EUR']
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            global currency_df
            currency_df = pd.concat([currency_df, pd.DataFrame({'Время': [current_time], 'USD/EUR': [usd_to_eur]})],
                                    ignore_index=True)
            print(f"{current_time} - Курс USD к EUR: {usd_to_eur}")
        else:
            print(f"Ошибка при запросе данных: Код ответа {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения: {e}")


while True:
    fetch_currency_rate()
    time.sleep(1800)
