#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
from jsonrpc.server import ServerEvents
import traceback
from maps_api import Places


# logging
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
# console handler
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s \
[ %(filename)s : %(lineno)s ] - %(message)s")
console.setFormatter(formatter)
logger.addHandler(console)

class Chat(ServerEvents):

    def log(self, responses, txrequest, error):

        if isinstance(responses, list):
            for response in responses:
                msg = self._get_msg(response)
                logger.debug("%d %s > %s" % (txrequest.code, txrequest, msg))
        else:
            msg = self._get_msg(responses)
            logger.debug("CODE: %d %s" % (txrequest.code, txrequest))
            logger.debug("TXT: " + msg)

    def findmethod(self, method, args=None, kwargs=None):
        logger.debug('Got method: ' + repr(method))

        if method in self.methods:
            return getattr(self, method)
        else:
            return None

    # helper
    methods = set(['hello', 'echo', 'want_pizza', 'server_methods'])

    def _get_msg(self, resp):
        logger.debug("%s -> %s" % (resp, dir(resp)))
        return ' '.join(str(x) for x in [resp.id, resp.result or resp.error])

    def hello(self):
        return "Hi, I am Pizza-Bot. Can I help you?"

    def echo(self, args):
        if isinstance(args, list):
            return ">> %s" % (' '.join(args))
        else:
            return ">> {0}".format(args)

    def want_pizza(self, kwargs):
        args = []
        pizza_place = Places()
        for k,v in kwargs.items():
            args.append(pizza_place.find_pizza(v))
        return args


    def server_methods(self):
        return { 'methods': self.methods }
