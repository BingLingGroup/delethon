#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines constants used by delethon.
"""

# Import built-in modules
import sys
import os
import locale

SUPPORTED_LOCALE = {
    "en_US",
    "zh_CN"
}
# https://www.gnu.org/software/gettext/manual/html_node/Locale-Names.html#Locale-Names

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable executable'.
    APP_PATH = os.path.dirname(sys.executable)
else:
    APP_PATH = os.path.dirname(__file__)

LOCALE_PATH = os.path.abspath(os.path.join(APP_PATH, "data/locale"))

EXT_LOCALE = os.path.abspath(os.path.join(os.getcwd(), "locale"))
if os.path.isfile(EXT_LOCALE):
    with open(EXT_LOCALE, "r") as in_file:
        LINE = in_file.readline()
        LINE_LIST = LINE.split()
        if LINE_LIST[0] in SUPPORTED_LOCALE:
            CURRENT_LOCALE = LINE_LIST[0]
        else:
            CURRENT_LOCALE = locale.getdefaultlocale()[0]
else:
    CURRENT_LOCALE = locale.getdefaultlocale()[0]
