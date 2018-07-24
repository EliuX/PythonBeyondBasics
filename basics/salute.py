#! /usr/bin/env python3
"""Prints a salute on console

Usage:
   python3 salute.py <who>
"""
import sys


def say_hi(who):
    """This is a simple function meant for testing documentation
    Args:
        who: Subject who is going to be saluted
    Returns:
        A string containing a salute
    """
    return "Hi {}".format(who)

if __name__ == '__main__':
    if len(sys.argv) > 1:
     print(say_hi(sys.argv[1]))
    else:
        print(say_hi("people"))
