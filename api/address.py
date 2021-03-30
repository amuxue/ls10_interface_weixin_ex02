import json

import requests

from api.Base import Base


class Address(Base):

    # def __init__(self):
    #     corpid = "ww4dd1f1a0852a1941"
    #     secret = "J1OELKLGBZPsK5Sr4ghto5-bYZrerPwLPqFkjH1BGD8"
    #     url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}'
    #     r = requests.get(url)
    #     self.token = r.json()["access_token"]


    def add_member(self,userid:str,name:str,mobile:str,department:list,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        # 新增
        data_add = {
            "access_token": self.token,
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data_add.update(**kwargs)
        r = self.send("post",url,json=data_add)
        return r

    def get_member(self,userid:str):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        r = self.send("get",url)
        return r

    def update_member(self,userid:str,name:str):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data_update = {
            "access_token": self.token,
            "userid": userid,
            "name": name,
        }
        r = self.send("post",url,data=json.dumps(data_update))
        return r

    def delete_member(self,userid:str):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        r = self.send("get",url)
        return r
