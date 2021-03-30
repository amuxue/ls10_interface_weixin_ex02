import requests


class Base:
    def __init__(self):
        corpid = "ww4dd1f1a0852a1941"
        secret = "J1OELKLGBZPsK5Sr4ghto5-bYZrerPwLPqFkjH1BGD8"
        url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}'
        r = requests.get(url)
        self.token = r.json()["access_token"]
        self.s = requests.Session()
        self.s.params = {"access_token": self.token}

    def send(self,*args,**kwargs):
        r = self.s.request(*args,**kwargs)
        return r.json()