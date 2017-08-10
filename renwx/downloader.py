
from __future__ import print_function

import zlib

from twisted.python import log
from twisted.internet.defer import Deferred
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.web.iweb import UNKNOWN_LENGTH
from twisted.web.http_headers import Headers
from twisted.web.client import Agent, ResponseDone, CookieAgent, readBody
from twisted.python.util import println
from twisted.python import log
from twisted.internet import defer, task

from arguments import cookies, headers
#from customs import tackler


def getResponse(url='http://api.deezer.com/artist/100000', headers=headers.header(), cookies=cookies.cookie(), method='GET', timeout=10, *args, **kw):

    agent = CookieAgent(Agent(reactor), cookies)
    d = agent.request(method, url, Headers(headers))
    d.addTimeout(timeout, reactor)
    d.addCallback(dealResponse)
    d.addErrback(log.err)
    #d.addBoth(lambda ign: reactor.callWhenRunning(reactor.stop))
    #reactor.run()
    return d 

def dealResponse(response):
    response_info = vars(response)
    d = readBody(response)
    d.addCallback(dealBody, response_info)
    d.addErrback(log.err)

def dealBody(data, response_info):
    #tackler.tackle_response(data, response_info)
    data = zlib.decompress(data, 16+zlib.MAX_WBITS)
    print(data, response_info)

def parallel(iterable, count, func):
    coop = task.Cooperator()
    work = (func(elem) for elem in iterable)
    return defer.DeferredList([coop.coiterate(work) for i in xrange(count)])

def downloader(reactor, *args):
    urls=list(args)
    return parallel(urls, len(urls), getResponse)

#getResponse('http://api.deezer.com/artist/100000', headers.header(), cookies.cookie())
#reactor.run()
#task.react(getResponse)
task.react(downloader, ['http://api.deezer.com/artist/'+str(i) for i in xrange(100000, 100020)]) # Can pass a list of urls
