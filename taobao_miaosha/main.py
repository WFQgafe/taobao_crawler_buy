from urllib import request
from bs4 import BeautifulSoup
import json
import requests
import re
import time
import traceback

cart_url = ""

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://world.taobao.com/cart/cart.htm?spm=a1z0d.7625083.1998302264.7.5c5f4e69VujS8b",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "bx-v": "2.2.3",
        "Content-Length": "596",
        "Origin": "https://world.taobao.com",
        "Connection": "keep-alive",
        "Cookie": "miid=676930729674609559; cna=bl4uG2cWJ2YCAY62jjqXy+zG; isg=BC4ucvYLwX03bTWef29u9XPwfITwL_Ip29PvrFj2pjG1O82VwL5YOU998zfX-OpB; l=eBSbca6uTJVN64PhBO5Churza77TyIOV1kPzaNbMiInca6sO6U5-XNCU2ufDJdtf3tfv7etP0srNudEW-yaLRxZGphim1Vj4ikv6-; thw=ca; _m_h5_tk=029f16837184d7949e52b654042f1124_1667506461609; _m_h5_tk_enc=8412362e1f02b86e26965d674d6372d4; t=5ad80089be3238e61655b4046907e60f; sgcookie=E1005GFieZ5NTvS0xI%2FTFvu19YLNTjt9m%2BkVA1baptFe3pfOIdTsK4fJQd333cOuCfdNxSZBC9%2BAI7XgyjGBnj4XOr4a7KhsDSlWC6%2BC4WM3ekY%3D; uc3=id2=UUphw21oJC2eUHFxCA%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=F5RCYR%2F1Ae048u0I&vt3=F8dCvjXn%2BAjHrSeSKn4%3D; lgc=tb7441364320; uc4=id4=0%40U2grGNIxaZwNPO09nFLEnwiGACRRn1Id&nk4=0%40FY4Jj1B%2FspfrY9f0n29rZOGE%2BP89YVU%3D; tracknick=tb7441364320; _cc_=Vq8l%2BKCLiw%3D%3D; arms_uid=f44f538a-548d-486b-88d4-7549fbd26394; dropBannerHasShow=true; enc=VctW%2FR69wbCvMJJyXmYdGMphxm9B%2BHN9j1rq%2BdeUJjIUAnPxWxmlM0GLqoQWskGg4qg%2FiBXJebubQnZmHFNlPgQsqNEPynOMKnJ0WbnDA9A%3D; ariaDefaultTheme=undefined; ariaStatus=false; mt=ci=2_1; ucn=center; cookie2=184c9d6b6cc636aec35a64490cee86ae; uc1=cookie14=UoeyCUVOQmf10w%3D%3D&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie21=VFC%2FuZ9aj3yE&pas=0&cart_m=0&cookie15=UIHiLt3xD8xYTw%3D%3D; _tb_token_=f3ee8fe737563; _samesite_flag_=true; um=GCFFE399DE9C031ADBAE0A2E368E38381BC7417; unb=2209844833729; csg=a4af293e; cancelledSubSites=empty; cookie17=UUphw21oJC2eUHFxCA%3D%3D; dnk=tb7441364320; skt=bd699e59b3d5e9d4; existShop=MTY2NzQ5NTcwNw%3D%3D; _l_g_=Ug%3D%3D; sg=09d; _nk_=tb7441364320; cookie1=VWw3%2FQ9znJZHLme6iWbn6ky6OAnx7fNaZPbHmEM1zfs%3D; v=0; tfstk=cC1OBPwCgkqMf4p68CeHu9_C9yrlZcH90x-jM_QVZTG-C3hRiFflwwIbuExyXyC..",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
        }


def submitOrder(result):
    global trackID
    html = result.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    riskControl = soup.find(id='riskControl')['value']
    #?????????????????????????????? ????????????????????? url????????? 'https://trade.jd.com/shopping/order/submitOrder.action'
    #?????????????????????????????????????????????????????? ?????????param???:
    #submitOrderParam.sopNotPutInvoice, submitOrderParam.TrackID, submitOrderParam.btSupport, riskControl
    url = 'https://trade.jd.com/shopping/order/submitOrder.action'
    # trackID ??????cookie????????????
    # '1tpdF8meXyz3q6lwHczWCmquOsUzEqNkVxi4ZNTwpzi93w0df-iIPnlKQHXeMn_L3oXKG2yjOpye-tJAeoc7yiDVHgF0oD026uhJIhebUCDNGMpm7TBd6gwvjTQ20AMpQHtM8nRe5jelg6Xf9kzgWfg',
    data = {
        'submitOrderParam.sopNotPutInvoic': False,
        'submitOrderParam.TrackID': trackID,
        'submitOrderParam.btSupport': 0,
        'riskControl': riskControl
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)
    print('??????????????????')


def init_header():
    global headers
    global cookie
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    accept_language = 'en-US,en;q=0.5'
    accept_ecoding = 'gzip, deflate'
    connect = 'keep-alive'
    headers = {'User-Agent': user_agent, 'Accept': accept, 'Accept-Language': accept_language,
               'Accept-Encoding': accept_language, 'Cookie': cookie, 'Connection': connect}


def Order_set():
    result = request.urlopen("")
    html = result.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    rid = soup.find(id='currentTime')
    url = 'https://trade.jd.com/shopping/order/getOrderInfo.action?rid=' + str(rid['value'])
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as result:
        print('????????????????????????')
        submitOrder(result)


