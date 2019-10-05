import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

headers = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
}


def get_xsrf():
    # 获取xsrf code
    response = requests.get("https://www.zhihu.com", headers=headers)
    match_xsrf = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_xsrf:
        return match_xsrf.group((1))
    else:
        return ""


def zhihu_login(account, password):
    # 知乎登录
    if re.match("^1\d{10}", account):
        print('login with phone')
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": "",
            "phone_num": account,
            "password": password
        }


text = get_xsrf()
print(text)
