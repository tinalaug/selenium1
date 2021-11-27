import random
import time

import requests

import uuid



class TestTag:

    def setup_class(self):


        corpid = "ww7811fa156eabf97c"
        corpsecret = "n68iy0pk9BYEFfZJ38ha5u8EoN3oiXuyc06f9Py08ww"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        r = requests.get(url, params=params)
        self.access_token = r.json().get("access_token")
        print(self.access_token)

    def test_create_tag(self):
        uid=str(uuid.uuid1()).split("-")[0]
        tim = int(time.time())
        tid = random.randint(0, 1000)

        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.access_token}"
        data = {
            "tagname": f"UI_{uid}",
            "tagid": tid
        }
        r = requests.post(url,json=data)
        print(r.json())
        assert r.json().get("errcode") == 0

    def create_tag(self):
        uid = str(uuid.uuid1()).split("-")[0]
        tim=int(time.time())
        tid = random.randint(0, 1000)

        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.access_token}"
        data={
            "tagname": f"UI_{uid}",
            "tagid": tid
        }
        r = requests.post(url,json=data)
        return r

    def test_dele_tag(self):
        r = self.create_tag()
        assert r.json().get("errcode") == 0

        ID=r.json().get("tagid")
        print(ID)
        url= f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.access_token}&tagid={ID}"
        r=requests.get(url)
        # assert r.json().get("errcode")==0

    def test_update(self):
        uid = str(uuid.uuid1()).split("-")[0]
        tname=random.randint(0,1000)
        cr=self.create_tag()
        assert cr.json().get("errcode") == 0
        ID=cr.json().get("tagid")

        url=f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.access_token}"
        data={
           "tagid": ID,
           "tagname": f"UI_{uid}"
        }
        r=requests.post(url,json=data)
        assert r.json().get("errcode") == 0

    #不需要调用create
    def test_get_taglist(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.access_token}"
        r=requests.get(url)
        print(r.json())
        assert r.json().get("errcode")==0

