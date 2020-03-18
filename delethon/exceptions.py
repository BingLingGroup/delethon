#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines exceptions used by delethon.
"""

# Import built-in modules
import sys


class DelethonException(Exception):
    """
    Raised when something need to print
    and works need to be stopped.
    """

    def __init__(self, msg):
        super(DelethonException, self).__init__(msg)
        try:
            self.msg = str(msg)
        except UnicodeEncodeError:
            self.msg = msg.encode(sys.stdout.encoding)

    def __str__(self):
        return self.msg
