import requests
from config import config

class Memeber:
    def __init__(self):
        self.urls = config.url_list
        self.resp = dict()

    def get_cur_member(self):

        urls = list(map(lambda x:x+"api", self.urls))
        
        for url in urls:
            resp = requests.post(url)
            name = url[7:url.find(".")]
            self.resp[name] = resp.content 
        
member = Memeber()
