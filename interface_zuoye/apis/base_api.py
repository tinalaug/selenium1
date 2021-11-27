
#封装底层request获取方法
import requests


class Baseapi:
    def send(self,method,url,tools,**kwargs):

        if tools == "requests":
            data={
                "method":method,
                "url":url
            }
            #还需要更新的内容用update ,此处参数传递出错了，查了好久才查出来
            data.update(kwargs)
            #request时需要明确method、url
            res=requests.request(**data)
            #请求的结果需要返回
            print(res)
            return res
        else:
            return True