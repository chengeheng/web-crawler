import requests

url = "http://www.baidu.com"

# 添加请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

print(response.content.decode())
