import hashlib
import random
import time

import requests


def send_varify_code(phone):
    url = 'https://api.netease.im/sms/sendcode.action'
    nonce = hashlib.new("sha512", str(time.time).encode("utf-8")).hexdigest()
    curtime = str(int(time.time()))

    # 太长了封装一下sha1
    # checksum = hashlib.new("sha1", ("adf4ec551229"+nonce+curtime).encode("utf-8")).hexdigest()
    secrect = 'adf4ec551229'
    sha1 = hashlib.sha1()
    sha1.update((secrect+nonce+curtime).encode("utf-8"))
    checksum = sha1.hexdigest()


    headers = {
        'AppKey': '14e7051e8bd6ffb532ea31a8738174a3',
        'Nonce': nonce,
        'CurTime': curtime,
        'CheckSum': checksum,
    }

    data = {
        'mobile': phone,
        'codeLen': 10,
    }

    response = requests.post(url, data=data, headers=headers)

    return response

# if __name__ == '__main__':
#     send_code()

