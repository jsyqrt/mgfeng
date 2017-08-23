# coding: utf-8

import re
import urllib
from urllib import quote

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from tornado.escape import utf8, to_unicode

class FreeProxyListSpider(scrapy.Spider):
    name = "fpl"

    __base_url = "https://www.free-proxy-list.net"
    __headers = {"Host": "www.free-proxy-list.net", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "deflate, br", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Pragma": "no-cache", "Cache-Control": "no-cache"}

    def start_requests(self):

        yield Request(
            url=self.__base_url,
            headers=self.__headers,
            meta={
                'dont_merge_cookies': True,
                'proxy': 'http://192.168.0.120:1080',
                },
            )

    def parse(self, response):
        items = zip(*[response.xpath('//tr/td[' + str(i) +']/text()').extract() for i in xrange(1, 9)])
        titles = ('ip', 'port', 'code', 'country', 'anonymity', 'google', 'https', 'last_checked')
        yield {
                'proxys': [{titles[i]: value[i] for i in xrange(8)} for value in items], 
                'numbers': len(items),
              }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(FreeProxyListSpider)
    process.start()
