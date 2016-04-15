#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
# add path
sys.path.append('../pizzabot')


from twisted.internet import reactor
from bot import ChatFactory

def main():

    # cmd line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:", ["port="])
    except getopt.GetoptError:
        print "%s -p <PORT>" % (sys.argv[0])
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-h':
            print "%s -p <PORT>" % (sys.argv[0])
            sys.exit(0)
        elif opt == '-p':
            reactor.listenTCP(int(arg), ChatFactory())
            reactor.run()
        else:
            print "No args!"
            print "%s -p <PORT>" % (sys.argv[0])
            sys.exit(1)


if __name__ == "__main__":
    main()
