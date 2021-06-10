import requests


class RequestUtil:
    def __init__(self):
        pass

    def requests_make(self, url, method: str, headers=None, param=None, content_type=None):
        """
        通用请求工具
        :param url:传入api的url
        :param method:请求类型，如gat、post等
        :param headers:请求头
        :param param:需传入的参数
        :param content_type:post的传参数据类型，如：data、josn等
        :return:response.json()
        """
        # try:
        if method == 'get':
            result = requests.get(url=url, params=param, headers=headers).json()
            return result
        if method == 'post':
            if content_type == 'json' or content_type == 'application':
                result = requests.post(url=url, json=param, headers=headers).json()
                return result
            else:
                result = requests.post(url=url, data=param, headers=headers).json()
                return result

        else:
            print('暂不支持该类型api请求！')

        # except Exception as e:
        #     print(f'http报错:{e}')
