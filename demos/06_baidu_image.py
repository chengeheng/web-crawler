import requests
import time


class Image(object):

    def __init__(self):
        self.url = "https://image.baidu.com/search/acjson?"
        self.headers = {
            "Cookie": "BDqhfp=%E6%80%AA%E7%89%A9%E7%8C%8E%E4%BA%BA%26%26-10-1undefined%26%260%26%261; PSTM=1647408632; BAIDUID=266EA5A7DAB7386CFC5E8D1D91E1C16A:FG=1; BIDUPSID=25055FC246F7BB73B013EA551F0DDC2D; BAIDUID_BFESS=266EA5A7DAB7386CFC5E8D1D91E1C16A:FG=1; BAIDU_WISE_UID=wapp_1665329201942_161; ZFY=HZd28e806zWE1l:BMLBA8V3BCGrxHJLKMrzUrhhdNOFg:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; indexPageSugList=%5B%22%E6%80%AA%E7%89%A9%E7%8C%8E%E4%BA%BA%22%2C%22%E5%93%88%E5%A3%AB%E5%A5%87%22%2C%22%E9%85%B7%E7%82%AB%20%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF%22%2C%22%E5%B8%85%E6%B0%94%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF%22%2C%22%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF%20%E6%B8%B8%E6%88%8F%20%22%2C%22%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF%20%E6%B8%B8%E6%88%8F%20%E5%9C%B0%E5%B9%B3%E7%BA%BF4%22%2C%22%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF%20%E6%B8%B8%E6%88%8F%22%2C%22%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF%22%2C%22mac%E8%83%8C%E6%99%AF%22%5D; BA_HECTOR=a585048l0h2g05ag0l0g8qmv1hkth5l1a; userFrom=null; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_ZDAyMTJhZTk0Zjk2YTU2NzA1ODlkYzU2MGFiZTViOTkxZTJmNjI2N2RjMjI3MjZlNWI3MzExMWVlYTdkMjE4NmUzNmMxMjY3YzNjMWJjY2Q5NTA1YWUwZmU3YzM0MzYzMDdlNmQwNjJlYTlkM2YxNjVjNDUxNTZhNjI1OTU3ZjMzZjNlNjk3ZDgxMGM5MWNiZmQ5MTc1NzIxMGM0OTdmNg==; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
        self.params = {
            "tn": "resultjson_com",
            "logid": 9055086486630376210,
            "ipn": "rj",
            "ct": 201326592,
            "is": "",
            "fp": "result",
            "fr": "",
            "word": "怪物猎人",
            "queryWord": "怪物猎人",
            "cl": 2,
            "lm": -1,
            "ie": "utf-8",
            "oe": "utf-8",
            "adpicid": "",
            "st": -1,
            "z": "",
            "ic": "",
            "hd": "",
            "latest": "",
            "copyright": "",
            "s": "",
            "se": "",
            "tab": "",
            "width": "",
            "height": "",
            "face": 0,
            "istype": 2,
            "qc": "",
            "nc": 1,
            "expermode": "",
            "nojc": "",
            "isAsync": "",
            "pn": 60,
            "rn": 30,
            "time": ""
        }
        self.image_list = []

    def get_image(self, num):
        print(self.url)
        for i in range(0, num):
            self.params["time"] = int(time.time() * 1000)
            self.params["pn"] = i * 30
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            for j in range(0, len(response.json()["data"]) - 1):
                self.image_list.append(response.json()["data"][j]["thumbURL"])

    def save_image(self):
        n = 1
        for i in self.image_list:
            image_content = requests.get(url=i)
            with open("./图片/{}.jpg".format(n), "wb") as f:
                f.write(image_content.content)
            n += 1


if __name__ == '__main__':
    image = Image()
    image.get_image(3)
    image.save_image()
