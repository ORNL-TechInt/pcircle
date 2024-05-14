#!/bin/env python
import random
import string
import argparse
import os
import os.path
import sys
import re

args = None
MAGIC = '8888'
PREFIX = 'f.'


def rand_str(size=1024 * 1024, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def parse_args():
    parser = argparse.ArgumentParser(description="Generate fake files")
    parser.add_argument('-s', '--fsize', default="1g", help="total file size")
    parser.add_argument('-c', '--fcount', type=int, default=1, help="total # of files")
    parser.add_argument('-o', '--output', required=True, help="output directory")
    parser.add_argument('-v', '--verbose', default=False, action="store_true", help="debug output")

    myargs = parser.parse_args()
    return myargs


def conv_mb(size):
    # need pattern of xxx [g,t,m]
    patt = re.compile(r'(\d+|\s+)')
    _, num, unit = patt.split(size)
    if num == '' or unit == '':
        print("parse error: %s" % size)
        sys.exit(1)
    if unit[0].upper() == 'K':
        return int(num)
    elif unit[0].upper() == 'M':
        return int(num)
    elif unit[0].upper() == 'G':
        return int(num) * 1024
    elif unit[0].upper() == 'T':
        return int(num) * 1024 * 1024
    else:
        print("Unknown size: %s" % size)
        sys.exit(1)


def main():
    global args
    args = parse_args()

    if args.verbose:
        print(args)

    # check path
    outdir = os.path.abspath(args.output)
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    buf = rand_str()

    for fount in range(args.fcount):
        fname = outdir + "/" + PREFIX + str(fount).zfill(8)
        if args.verbose:
            print("Writing out %s" % fname)
        chunks = conv_mb(args.fsize)
        with open(fname, "w") as f:
            for _ in range(chunks):
                f.write(buf)

    print("Okay.")


if __name__ == "__main__":
    main()
