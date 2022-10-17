"""金山词霸翻译爬虫"""
import hashlib
import json

import requests


class TranslateSpider(object):

    def __init__(self, query_str):
        self.query_str = query_str
        # 动态获取sign
        # r = c()("6key_web_fanyi".concat(s.y2).concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16)
        sign = (hashlib.md5(("6key_web_fanyiifanyiweb8hc9s98e" + self.query_str).encode("utf-8")).hexdigest())[0:16]
        url = "http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi"
        self.url = url + "&sign=" + sign
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        # 获取请求体数据
        self.data = self.get_data()

    def get_data(self):
        """获取请求体数据"""
        data = {
            "form": "auto",
            "to": "auto",
            "q": self.query_str
        }
        return data

    def get_data_form_url(self):
        """从服务器获取数据 并解码返回"""
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content.decode()

    def get_data(self):
        """获取请求体数据"""
        data = {
            "form": "auto",
            "to": "auto",
            "q": self.query_str
        }
        return data

    def parse_data(self, json_str):
        dict_data = json.loads(json_str)
        result = dict_data["content"]["out"]
        print("{}翻译后的结果是：{}".format(self.query_str, result))

    def run(self):
        # 1. 获取url 请求头 请求体
        # 2. 发起请求获取响应数据
        json_str = self.get_data_form_url()
        # 3. 提取数据
        self.parse_data(json_str)


if __name__ == "__main__":
    text = input("请输入翻译的内容：")
    spider = TranslateSpider(text)
    spider.run()


