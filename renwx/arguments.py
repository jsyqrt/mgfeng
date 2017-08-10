# coding: utf-8

import random
from cookielib import CookieJar
from cookielib import Cookie

class headers(object):

    headers = [
        {
            'Accept':['text/html'],
            'Accept-Encoding':['gzip', 'deflate', 'br'],
            'Accept-Language':['en'],
            'Cache-Control':['no-cache'],
            'Connection':['keep-alive'],
            'Host':['api.deezer.com'],
            'Pragma':['no-cache'],
            'Upgrade-Insecure-Requests':['1'],
            'User-Agent':['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'],
        },
    ]

    @staticmethod
    def header():
        return random.choice(headers.headers)

class cookies(object):

    cookies =[
        {
        },
    ]
    
    @staticmethod
    def domain():
        return '.deezer.com'
    
    @staticmethod
    def cookie():
        cc = random.choice(cookies.cookies)
        cookie=CookieJar()
        for c in cc:
            ck = Cookie(version=1, name=c, value=cc[c],
                        port=None, port_specified=False, domain=cookies.domain(), 
                        domain_specified=True, 
                        domain_initial_dot=True, path='/', 
                        path_specified=True, secure=False, 
                        expires=None, discard=True, 
                        comment=None, comment_url=None, 
                        rest=None, rfc2109=True)
            cookie.set_cookie(ck)
        
        return cookie
