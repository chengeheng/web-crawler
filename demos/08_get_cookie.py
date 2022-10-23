import requests

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(type(response.cookies))

# 使用方法从cookieJar中提取数据
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)

