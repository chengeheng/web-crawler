import requests

image_url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fmeiwai.net%2Fuploads%2Fallimg%2Fc140425" \
            "%2F13b3a29DG40-14917.jpg&refer=http%3A%2F%2Fmeiwai.net&app=2002&size=f9999," \
            "10000&q=a80&n=0&g=0n&fmt=auto?sec=1667833589&t=342b53068f2edf5cefcab05253d22444 "

response = requests.get(image_url)

# 打印出来是二进制编码
print(response.content)

with open("二哈.jpg", "wb") as f:
    f.write(response.content)
