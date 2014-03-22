#!/usr/bin/python

import argparse
from collections import defaultdict

# import file here
# fake import 
# from visualize import lol_visualize
def parseArguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]', description='bd application')

    parser.add_argument('--debug', action='store_true', default=False)

    parser.add_argument('-m', '--min-area', dest='minArea', type=float, default=2.0, help='specify the minimum area threshold')
    parser.add_argument('-l', '--lol')
    parser.add_argument('-c', '--color', default='')
    parser.add_argument('-t', '--type', default='histogram1')
    return parser.parse_args()

if __name__ == "__main__":

    config = defaultdict(list)
    args = parseArguments()
    debug = args.debug

    if args.type == 'histogram1':
    	# plot histogram1
    	# lol_visualize.histogram1(args, ...other stuff here if needed...)
    elif args.type == 'histogram_gold':
    	# plot histogram for gold
    else:
    	print 'no known graph'

    # Or was it this..

    if args.lol == 'something1':
    	# do something one
    elif args.lol == 'something2':
    	# do something else

    if args.color == 
