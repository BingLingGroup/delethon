#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines delethon's commandline entry point functionality.
"""

# Import built-in modules
import gettext
import shlex
import gc

# Import third-party modules

# Any changes to the path and your own modules
from delethon import options
from delethon import constants
from delethon import exceptions
from delethon import cmdline_utils


INIT_TEXT = gettext.translation(domain=__name__,
                                localedir=constants.LOCALE_PATH,
                                languages=[constants.CURRENT_LOCALE],
                                fallback=True)

try:
    _ = INIT_TEXT.ugettext
except AttributeError:
    # Python 3 fallback
    _ = INIT_TEXT.gettext


def main():  # pylint: disable=too-many-branches
    """
    Run delethon as a command-line program.
    """

    parser = options.get_cmd_parser()
    args = parser.parse_args()

    args_list = []

    if args.argv:
        for argv_str in args.argv:
            arguments = parser.parse_args(shlex.split(argv_str))
            args_list.append(arguments)
    else:
        args_list.append(args)

    try:
        if len(args_list) > 1:
            last_args = args_list[0]
            client = cmdline_utils.start_client(last_args)
            cmdline_utils.prcs_args(last_args, client)
            args_list = args_list[1:]

            for args in args_list:
                if not cmdline_utils.is_same_client(args, last_args):
                    del client
                    gc.collect(0)
                    client = cmdline_utils.start_client(args)
                cmdline_utils.prcs_args(args, client)
                last_args = args
        else:
            client = cmdline_utils.start_client(args_list[0])
            cmdline_utils.prcs_args(args_list[0], client)

    except exceptions.DelethonException as err_msg:
        if args.log_level > 0:
            print(err_msg)
    except KeyboardInterrupt:
        if args.log_level > 0:
            print(_("\nKeyboardInterrupt. Works stopped."))

    return 0
