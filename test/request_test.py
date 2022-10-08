import requests

r = requests.get("http://www.baidu.com")

print(r)
print(r.status_code)

# 指定编码格式
# 通常为gbk或者utf-8
r.encoding = "utf-8"
print(r.text)
# 另一种解码格式
print(r.content.decode())
