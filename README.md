# web-crawler
使用python进行网络爬虫练习

## 安装运行

创建requirements.txt
- 使用命令 pip freeze > requirements.txt
- 手动创建
- 安装pipreqs
```commandline
安装pipreqs
pip3 install pipreqs 
生成requirements.txt文件
pipreqs ./
```

利用requirement.txt安装项目运行环境所需依赖
```commandline
pip3 install -r requirements.txt 
```

## requests

底层实现就是`urllib`，能够自动帮助我们解压（gzip压缩的等）响应内容

### 使用

```python
import requests

r = requests.get("url")
print(r.content.decode())
```

打印图片需要操作文件指令
```python
import requests

response = requests.get("url")

with open("二哈.jpg", "wb") as f:
    f.write(response.content)

```

## 请求

- get请求
```python
response_get = requests.get(url, headers=headers)
```
- post请求
```python
response_post = requests.post(url, headers=headers, data=data)
```


## 代理

主要分为三类：

- 透明代理
- 匿名代理
- 高匿代理

**使用**

```python
proxies = {
    "http": "代理地址",
    "https": "代理地址"
}

responst = requests.get(url, proxies=proxies)
```