import json

from mitmproxy import http


def response(flow:http.HTTPFlow):

    if "quote.json" in flow.request.pretty_url and "x="in flow.request.pretty_url:
        data=json.loads(flow.response.content)

        data['data']['items'][0]['quote']['name']="刘叶-red"
        data['data']['items'][0]['quote']['percent'] = "0.01"
        data['data']['items'][1]['quote']['name'] = "刘叶-grey"
        data['data']['items'][1]['quote']['percent'] = "0.00"
        data['data']['items'][2]['quote']['name'] = "刘叶-green"
        data['data']['items'][2]['quote']['percent'] = "-0.01"

        flow.response.text = json.dumps(data)


