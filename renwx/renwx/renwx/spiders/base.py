# coding: utf-8

import json
import urllib

import scrapy
from scrapy import Request
from tornado.escape import utf8, to_unicode

class Base_Spider(scrapy.Spider):
    

