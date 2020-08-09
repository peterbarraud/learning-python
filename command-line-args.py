"""
More help: https://docs.python.org/3/library/argparse.html
Usage:
    python command-line-args.py --foo fooval --baa baaval
    python command-line-args.py --foo=fooval --baa=baaval
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--baa', help='baa help')
    args = parser.parse_args()    
    print(args.foo)
    print(args.baa)
