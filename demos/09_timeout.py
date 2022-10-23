import requests
from retrying import retry


@retry(stop_max_attempt_number=3)  # 装饰器
def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    print("start get")
    response = requests.get(url, headers=headers, timeout=3)
    print(response.status_code)  # 时间过长
    return response


def test(url):
    response = get_data(url)
    return response


if __name__ == '__main__':
    url = "https://www.google.com"
    test(url)
