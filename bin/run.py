#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
# add path
sys.path.append('../pizzabot')


from twisted.internet import reactor
from twisted.web import server
from jsonrpc.server import JSON_RPC
from bot import Chat

def main(argv):

    # cmd line arguments
    try:
        opts, args = getopt.getopt(argv[1:], "hp:")
    except getopt.GetoptError as e:
        print str(e)
        print "%s -p <PORT>" % (argv[0])
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print "%s -p <PORT>" % (argv[0])
            sys.exit(0)
        elif opt == '-p':
            print "Trying to start APP at %s PORT" % arg
            # json RPC app
            root = JSON_RPC().customize(Chat)
            site = server.Site(root)
            # run application
            reactor.listenTCP(int(arg), site)
            reactor.run()
        else:
            print "No args!"
            print "%s -p <PORT>" % (argv[0])
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
