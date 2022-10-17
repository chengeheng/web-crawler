import requests


class TiebaSpider(object):

    def __init__(self, t):
        self.text = t
        self.url = "https://tieba.baidu.com/f?kw=" + text + "&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }

    def get_url_list(self):
        """生成url_list"""
        url_list = [self.url.format(i * 50) for i in range(5)]
        return url_list

    def get_data_form_url(self, url):
        """从服务器获取数据 并解码返回"""
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, num):
        """保存到本地"""
        file_name = "贴吧_" + self.text + " 第{}页".format(num) + ".html"
        """指定打开文件的编码格式"""
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for item_url in url_list:
            html_str = self.get_data_form_url(item_url)
            # 保存到本地
            self.save_html(html_str, url_list.index(item_url) + 1)


if __name__ == "__main__":
    text = input("请输入贴吧的名字：")
    spider = TiebaSpider(text)
    spider.run()

