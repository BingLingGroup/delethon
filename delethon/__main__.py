#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines delethon's entry point.
"""

# Import built-in modules
import sys


if __package__ is None and not hasattr(sys, "frozen"):
    # direct call of __main__.py
    # Reference: https://github.com/rg3/youtube-dl/blob/master/youtube_dl/__main__.py
    import os.path
    PATH = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(PATH)))


if __name__ == "__main__":
    import delethon
    delethon.main()
