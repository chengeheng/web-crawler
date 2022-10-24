import requests

url = "https://sam.huat.edu.cn:8443/selfservice" # 任何没有ca认证网站

response = requests.get(url, verify=False)
print(response.status_code)

