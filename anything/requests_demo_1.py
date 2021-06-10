import json

import requests

# data = {'video_id': 52}
# response = requests.get('https://api.xdclass.net/pub/api/v1/web/video_detail', data)
#
# response = requests.get(
#     'https://media-cache.huaweicloud.com/video/hwplayer/1.0.0/lib/plugins/css/videojs-allPlugins.css')
# data = {'phone': '18380477311', 'pwd': 'martin001'}
# response = requests.post('https://api.xdclass.net/pub/api/v1/web/web_login', data=data)

# headers = {'Content-Type': 'application/x-www-form-urlencoded',
#            "token": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTguanBlZyIsImlkIjo2Nzg3Nzg4LCJuYW1lIjoiaDEyMTYxNjEyIiwiaWF0IjoxNjIwMzU3MjYwLCJleHAiOjE2MjA5NjIwNjB9.aAahVrvSamf14OwyTeoXGlby-UyTO4Nf0jyIJupmnso"}
# # response = requests.get('https://api.xdclass.net/pub/api/v1/web/user_info', headers=headers)
# response = requests.post('https://api.xdclass.net/user/api/v1/favorite/save', data={'video_id': 38}, headers=headers)
#
# print(response.text)
# print(response.json())
# print(response.content)
# print(response.status_code)
# host = 'http://192.168.19.10:8080/woniusales'
# host = 'http://127.0.0.1:8000/api'


# def login_sales():
#     # repost = RequestUtil()
#     url = host + '/user/login'
#     data = {'username': 'admin', 'password': 'admin', 'verifycode': '0000'}
#     response = requests.session().post(url=url, data=data)
#     print(response)

# def fabuhui():
#     url = host + '/get_event_list'
#     data = {'eid': '1'}
#     header = {'Content-Type': 'application/json'}
#     response = requests.get(url=url, params=data,headers=header)
#     result = response.json()
#     print (result)

def fabuhui_2():
    url = 'https://web-api.okjike.com/api/graphql'
    data = {
            'operationName': 'GetSmsCode',
            'query': "mutation GetSmsCode($mobilePhoneNumber: String!, $areaCode: String!)"
                     "{getSmsCode(action: PHONE_MIX_LOGIN, mobilePhoneNumber: $mobilePhoneNumber, areaCode: $areaCode) "
                     "{action __typename}}",
            'variables': {'mobilePhoneNumber': '18380477311', 'areaCode': '+86'},
            'areaCode': '+86',
            'mobilePhoneNumber': '18380477311'
            }
    data2 = json.dumps(data)
    header = {'Content-Type': 'application/json'}
    print(data2)
    response = requests.post(url=url, data=data2, headers=header, verify=False)
    # result = response.json()
    print(response.text)


if __name__ == '__main__':
    fabuhui_2()
