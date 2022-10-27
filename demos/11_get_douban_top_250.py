import requests
import re
from parsel import Selector


class MovieSpider(object):
    def __init__(self):
        self.url = "https://movie.douban.com/top250?start={}&filter="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/106.0.0.0 Safari/537.36 "
        }
        self.data_list = []

    def get_url_list(self):
        url_list = []
        for i in range(10):
            url_list.append(self.url.format(i))
        return url_list

    def get_data_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            html_content = response.content.decode()
            selector = Selector(text=html_content)
            items = selector.css(".grid_view").xpath("./li")
            for item in items:
                span_len = len(item.xpath(".//span[@class='title']"))
                self.data_list.append({
                    "link": item.xpath(".//a[@href]/@href").get(),
                    "img_url": item.xpath(".//img[@class='']/@src").get(),
                    "name": item.xpath(".//span[@class='title']")[0].get(),
                    "name_en": item.xpath(".//span[@class='title']//text()")[1].get().replace("/", "").strip() if span_len >= 2 else None,
                })

    def save_data(self):
        pass

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            self.get_data_from_url(url)
        print(len(self.data_list))


if __name__ == '__main__':
    movie = MovieSpider()
    movie.run()
