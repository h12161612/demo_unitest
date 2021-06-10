import random
import re
import unittest

import requests

from util.requestutil import RequestUtil

# host = 'https://api.xdclass.net'
host = 'http://192.168.19.10:8080/woniusales'


class IndexTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()
        cls.globals = globals()

    # def setUp(self) -> None:
    #     self.session_1 = self.session_1()

    # def test_index_video(self):
    #     repost = RequestUtil()
    #     url = host + '/pub/api/v1/web/video_detail'
    #     data = {'video_id': 52}
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #
    #     response = repost.requests_make(url=url, method='get', param=data, headers=headers)
    #     # print(response)
    #     self.assertEqual(response['code'], 0, '业务状态码不正确')
    #     self.assertTrue(len(response['data']) > 0, '视频信息为空')
    #
    # def test_index_login(self):
    #     repost = RequestUtil()
    #     url = host + '/pub/api/v1/web/web_login'
    #     data = {'phone': '18380477311', 'pwd': 'martin001'}
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #
    #     response = repost.requests_make(url=url, method='post', param=data, headers=headers)
    #     # print(response)
    #     self.assertEqual(response['code'], 0, '业务状态码不正确')

    def test_login_sales(self):
        # repost = RequestUtil()
        url = host + '/user/login'
        data = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
        response = self.session.post(url=url, data=data).text
        self.assertEqual(response, 'login-pass', '返回值未符合预期')
        # print(response)

    def test_barcode(self):
        url = host + '/sell/barcode'
        data = {'barcode': '6955203662996'}
        resp = self.session.post(url=url, data=data)
        rest = resp.json()
        self.assertNotEqual(rest, [], '返回值为空')
        self.globals['barcode'] = rest[0]
        # print(resp)

    def test_query(self):
        url = host + '/customer/query'
        data = {'customerphone': '15983123450'}
        resp = self.session.post(url=url, data=data)
        rest = resp.json()
        self.assertNotEqual(rest, [], '返回值为空')
        self.globals['query'] = rest[0]
        # print(resp.text)

    def sell01(self, barcode, phone, expt, caseid, paymethod='现金'):
        # 1、请求数据准备
        # 1.1参数化 barcode,phone,paymethod
        # 1.2 代码自动产生
        tickettype = "长得帅，不需要原因"  # 优惠原因
        ticketsum = random.randint(1, 5)  # 优惠金额
        discountratio = random.randint(0, 100)  # 折扣率
        buyquantity = random.randint(1, 3)  # 购买数量
        # 1.3 接口调用
        # barcode接口 =》 尺码、商品数量、积分倍数、货号、商品名称、单价
        dic_barcode = self.globals['barcode']
        goodsserial = dic_barcode['goodsserial']  # 货号
        goodsname = dic_barcode['goodsname']  # 商品名称
        unitprice = dic_barcode['unitprice']  # 单价
        createtime = dic_barcode['createtime']
        # print(goodsserial, goodsname, unitprice, createtime, sep='\n')

        # print(type(createtime))  # 使用正则去处理
        sizes = re.findall("尺码:(.*?),剩余", createtime)
        # print(sizes)
        temp_li = createtime.split('##')

        creditratio = float(temp_li[-2])  # 积分倍数
        # discountratio = temp_li[-1]   # 折扣率

        # query接口
        credittotal = self.globals['query']['credittotal']

        # 1.4 计算
        totalprice = int((unitprice * discountratio / 100 * buyquantity) - ticketsum)  # 支付总金额
        creditsum = int((unitprice * discountratio / 100 * buyquantity - ticketsum) * creditratio)  # 本次新增积分
        goodssize = random.choice(sizes)
        discountprice = unitprice * discountratio / 100
        subtotal = unitprice * discountratio / 100 * buyquantity

        # summary接口
        url = host + '/sell/summary'
        data = {'customerphone': phone, 'paymethod': paymethod, 'totalprice': totalprice, 'creditratio': creditratio,
                'creditsum': creditsum, 'tickettype': tickettype, 'ticketsum': ticketsum, 'oldcredit': credittotal}

        resp = self.session.post(url=url, data=data)  # 会员历史积分
        sellsumid = resp.text
        print(sellsumid)

        # # detail接口
        url = host + '/sell/detail'
        data = f'sellsumid={sellsumid}&barcode={barcode}&goodsserial={goodsserial}&goodsname={goodsname}&goodssize={goodssize}' \
               f'&unitprice={unitprice}&discountratio={discountratio}&discountprice={discountprice}&buyquantity={buyquantity}&subtotal={subtotal}'
        param = get_dic_from_str(data)
        resp = self.session.post(url=url, data=param)  # 会员历史积分
        rest = resp.text
        print(rest)
        assert_equals(rest, expt, caseid)
