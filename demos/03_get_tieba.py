import requests

# https://tieba.baidu.com/f?kw=steam&pn=0

url = "https://tieba.baidu.com/f?kw={}&pn={}"

text = input("请输入贴吧的名字：")

url_list = [url.format(text, i * 50) for i in range(5)]

print(url_list)

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

for item_url in url_list:
    response = requests.get(item_url, headers=headers)

    file_name = "贴吧_" + text + " 第{}页".format(url_list.index(item_url) + 1) + ".html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.content.decode())
