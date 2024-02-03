import sys


def rough():
    if not sys.stdin.isatty():
        print(sys.stdin.read())


rough()
