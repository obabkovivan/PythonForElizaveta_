import requests

article_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

try:
    response = requests.get(article_url, timeout=10)

    if response.status_code == 200:
        print("Запрос успешен!")
        print("Первые 500 символов статьи:")
        print(response.text[:500])
    else:
        print(f"Ошибка: {response.status_code}. Проверьте URL или сайт.")
except requests.exceptions.ConnectionError:
    print("Ошибка подключения. Проверьте интернет-соединение или адрес сайта.")
except requests.exceptions.Timeout:
    print("Превышено время ожидания ответа.")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при выполнении запроса: {e}")
