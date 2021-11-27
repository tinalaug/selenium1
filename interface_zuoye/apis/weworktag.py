import requests


from interface_zuoye.apis.base_api import Baseapi


class WeworkTag(Baseapi):
    #此处确认不进行初始化也是可以的
    def __init__(self):
        super().__init__()
        self.access_token = self.get_token()

    #封装一个token获取方法
    def get_token(self):
        corpid = "ww7811fa156eabf97c"
        corpsecret = "n68iy0pk9BYEFfZJ38ha5u8EoN3oiXuyc06f9Py08ww"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"

        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # r = requests.get(url, params=params)
        #param参数需要注意,检查编译器报错出问题的方法  **注意不要乱用
        r=self.send("GET",url,tools="requests",params=params)

        print(r.json())
        # 如何使用 ：return回去 或定义为类变量，self.access_token去使用
        return r.json().get("access_token")


if __name__ == '__main__':

    token=WeworkTag()
    token.get_token()

    # token = WeworkTag()
    # token.get_access_token()