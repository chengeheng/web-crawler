import requests

url = "http://www.baodu.com"

proxies = {
    "http": "http://58.20.184.187:9091",
    # "https": "代理地址"
}

response = requests.get(url, proxies=proxies)
print(response.status_code)
