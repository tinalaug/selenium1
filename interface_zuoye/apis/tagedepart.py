#对每个接口进行描述
from interface_zuoye.apis.base_api import Baseapi
from interface_zuoye.apis.weworktag import WeworkTag


class TageDepart(WeworkTag):
    def get_taglist(self):
        #需要用到 token 加了self，确认一下区别,应该没区别
        self.access_token=self.get_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.access_token}"
        #send方法weworktag中也继承了，可以直接用
        r=self.send("GET",url,tools="requests")
        #返回r,在test用例中断言时再取具体内容
        return r
