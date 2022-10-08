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