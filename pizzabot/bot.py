#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
from jsonrpc.server import ServerEvents
import traceback


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
    methods = set(['echo'])

    def _get_msg(self, resp):
        logger.debug("%s -> %s" % (resp, dir(resp)))
        return ' '.join(str(x) for x in [resp.id, resp.result or resp.error])

    def echo(self):
        return "Hi, what's your name?"

