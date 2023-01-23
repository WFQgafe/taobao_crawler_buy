import requests
import re
import time
import datetime
import json
import urllib
import sys
from prettytable import PrettyTable
from requests.packages.urllib3 import disable_warnings
from requests.cookies import cookiejar_from_dict

def help_info():
    help = """
usage : python {0}
    --time        Buying time and format: 00:00:00:00000000.
    --interval    Buying time interval.
    --l           Buying frequency.
""".format(sys.argv[0])
    print(help)

def __init__(self, trybuy_interval=None, Seconds_kill_time=None, number=None):
        self.session = requests.Session()
        self.cookie = cookie_info()
        self.session.cookies = cookiejar_from_dict(self.cookie)
        self.trybuy_interval = float(trybuy_interval)
        self.Seconds_kill_time = Seconds_kill_time
        self.number = int(number)

def buycartinfo(self):
        url = 'https://cart.taobao.com/cart.htm'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0'
        }
        response = self.session.get(url, headers=headers)
        print(response.text)
        response_json = re.search('try{var firstData = (.*?);}catch', response.text).group(1)
        response_json = json.loads(response_json)
        user_id = re.search('\|\^taoMainUser:(.*?):\^', response.headers['s_tag']).group(1)
        return response_json, user_id

buycartinfo(self=)
