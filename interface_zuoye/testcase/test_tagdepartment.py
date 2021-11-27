#测试方法
from interface_zuoye.apis.tagedepart import TageDepart


class Test_Tagdepartment:

    #注意别写反了，会找不到的 ，继承效果也是一样的
    def setup_class(self):
        self.tagD=TageDepart()

    def test_get_taglist(self):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.access_token}"
        # r=requests.get(url)

        r=self.tagD.get_taglist()
        print(r.json())
        assert r.json().get("errcode")==0