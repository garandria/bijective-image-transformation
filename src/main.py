"""
"""

import sys
import argparse
from imageT import *
from transformation import *

def usage():
    print("Usage:")
    print("python3 main.py")
    print("python3 src/main.py -t <transformation> -s <nb steps> <path/to/file>")
    print("python3 main.py -h for help")
    
    
if __name__ == '__main__':
    try:
        args = sys.argv
        length = len(args)
        if length >= 4:
            transfo = args[args.index("-t") + 1]
            nb = int(args[args.index("-s") + 1])
            img_name = args[-1]
            if transfo == "boustrophedon":
                transfo = boustrophedon
            elif transfo == "concentrique":
                transfo == concentrique
            elif transfo == "photomaton":
                transfo = photomaton
            elif transfo == "boulanger":
                transfo = boulanger
            img = imageT(img_name, transfo)
            img.draw(nb)
            exit(1)
        else:
            usage()
    except FileNotFoundError:
        print("File « {} » does not exist".format(args[-1]))
            
