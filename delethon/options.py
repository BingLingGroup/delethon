#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines delethon's options.
"""

# Import built-in modules
import argparse
import gettext
import os

# Import third-party modules


# Any changes to the path and your own modules
from delethon import metadata
from delethon import constants


OPTIONS_TEXT = gettext.translation(domain=__name__,
                                   localedir=constants.LOCALE_PATH,
                                   languages=[constants.CURRENT_LOCALE],
                                   fallback=True)

META_TEXT = gettext.translation(domain=metadata.__name__,
                                localedir=constants.LOCALE_PATH,
                                languages=[constants.CURRENT_LOCALE],
                                fallback=True)

_ = OPTIONS_TEXT.gettext
M_ = META_TEXT.gettext


def get_cmd_args():
    """
    Get command-line arguments.
    """
    parser = argparse.ArgumentParser(
        prog=metadata.NAME,
        usage=_('\n  %(prog)s [options]'),
        description=M_(metadata.DESCRIPTION),
        epilog=_("Make sure the argument with space is in quotes.\n"
                 "The default value is used\n"
                 "when the option is not given at the command line.\n"
                 "\"(arg_num)\" means if the option is given,\n"
                 "the number of the arguments is required.\n"
                 "Author: {author}\n"
                 "Email: {email}\n"
                 "Bug report: {homepage}\n").format(
                     author=metadata.AUTHOR,
                     email=metadata.AUTHOR_EMAIL,
                     homepage=metadata.HOMEPAGE),
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    client_group = parser.add_argument_group(
        _('Client Options'),
        _('Options to start a Telethon client.'))

    proxy_group = parser.add_argument_group(
        _('Proxy Options'),
        _('Options to use Telethon behind a proxy.')
    )

    iter_messages_group = parser.add_argument_group(
        _('Iterate Messages Options'),
        _('Options to control Telethon iter_messages method. '
          'Ref: https://docs.telethon.dev/en/latest/modules'
          '/client.html#telethon.client.messages.MessageMethods.iter_messages')
    )

    operation_group = parser.add_argument_group(
        _('Process Options'),
        _('Options to determine how to process the messages after retrieving them.')
    )

    info_group = parser.add_argument_group(
        _('Information Options'),
        _('Options to get extra information.')
    )

    client_group.add_argument(
        '-ai', '--api-id',
        metavar='API_ID',
        type=int,
        default=os.environ.get('TELEGRAM_API_ID'),
        help=_("Telegram app api_id. Input it or set the environment variable "
               "\"TELEGRAM_API_ID\". "
               "You can get one from https://my.telegram.org/apps "
               "(arg_num = 1) (default: %(default)s)")
    )

    client_group.add_argument(
        '-ah', '--api-hash',
        metavar='API_HASH',
        default=os.environ.get('TELEGRAM_API_HASH'),
        help=_("Telegram app api_hash. Input it or set the environment variable "
               "\"TELEGRAM_API_HASH\". "
               "You can get one from https://my.telegram.org/apps "
               "(arg_num = 1) (default: %(default)s)")
    )

    client_group.add_argument(
        '-sf', '--session-file',
        metavar=_('path'),
        default='Telethon',
        help=_("Telegram session file path. "
               "Ref: https://docs.telethon.dev/en/latest/concepts/sessions.html "
               "(arg_num = 1) (default: %(default)s)")
    )

    proxy_group.add_argument(
        '-pt', '--proxy-type',
        metavar=_('proxy_type'),
        nargs='?',
        const='SOCKS5',
        help=_("PySocks or MTProto Proxy. "
               "Available types: \"SOCKS5\", \"SOCKS4\", "
               "\"HTTP\", \"MTPROTO\". "
               "When using \"MTPROTO\", its type is "
               "\"ConnectionTcpMTProxyRandomizedIntermediate\". "
               "If environment variable \"HTTP_PROXY\" exists "
               "and this option is not used, "
               "it will use it. "
               "Ref: https://docs.telethon.dev/en/latest/basic"
               "/signing-in.html#signing-in-behind-a-proxy "
               "If arg_num is 0, use const type. "
               "(arg_num = 0 or 1) (const: %(const)s)")
    )

    proxy_group.add_argument(
        '-pa', '--proxy-address',
        metavar=_('address'),
        default='127.0.0.1',
        help=_("The IP address or DNS name of the proxy server. "
               "(arg_num = 1) (default: %(default)s)")
    )

    proxy_group.add_argument(
        '-pp', '--proxy-port',
        metavar=_('port'),
        default=1080,
        type=int,
        help=_("The port of the proxy server. "
               "(arg_num = 1) (default: %(default)s)")
    )

    proxy_group.add_argument(
        '-pu', '--proxy-username',
        metavar=_('username'),
        help=_("Set proxy username. "
               "(arg_num = 1)")
    )

    proxy_group.add_argument(
        '-ps', '--proxy-password',
        metavar=_('password'),
        help=_("Set proxy password. "
               "When using \"MTPROTO\", this option is \"secret\" instead. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-c', '--chats',
        nargs='*',
        metavar=_('entity_like'),
        help=_("Get the messages in the chat entity/entities. "
               "entity_like can be Telegram username, Group name and so on. "
               "If failed to get one, it will use it to match the entity name or id "
               "of the dialogs which the user joined. "
               "Ref: https://docs.telethon.dev/en/"
               "latest/concepts/entities.html#getting-entities"
               "(arg_num >= 1)")
    )

    iter_messages_group.add_argument(
        '-u', '--users',
        nargs='*',
        metavar=_('entity_like'),
        help=_("Get the messages from the user entity/entities. "
               "If not input, gets all users messages. "
               "Ref: https://docs.telethon.dev/en/"
               "latest/concepts/entities.html#getting-entities"
               "(arg_num >= 1)")
    )

    iter_messages_group.add_argument(
        '-m', '--me',
        action='store_true',
        help=_("Get messages from the current user who is logged in. "
               "(arg_num = 0)"))

    iter_messages_group.add_argument(
        '-ac', '--all-chats',
        action='store_true',
        help=_("Iterate over all the chat entity/entities "
               "that the current user joined. "
               "(arg_num = 0)"))

    iter_messages_group.add_argument(
        '-l', '--limit',
        metavar=_('int'),
        type=int,
        help=_("Number of messages to be retrieved. "
               "Slower when more than 3000. "
               "Ref: https://docs.telethon.dev/en/latest/modules"
               "/client.html#telethon.client.messages.MessageMethods.iter_messages "
               "(arg_num = 1) (default: unlimited)")
    )

    iter_messages_group.add_argument(
        '-ofd', '--offset-day',
        metavar=_('int'),
        type=int,
        help=_("Offset day (messages previous to this day will be retrieved). "
               "Exclusive. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-ofi', '--offset-id',
        metavar=_('int'),
        type=int,
        default=0,
        help=_("Offset message ID (only messages previous to the given ID "
               "will be retrieved). "
               "Exclusive. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-mxi', '--max-id',
        metavar=_('int'),
        type=int,
        default=0,
        help=_("All the messages with a higher (newer) ID "
               "or equal to this will be excluded. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-mni', '--min-id',
        metavar=_('int'),
        type=int,
        default=0,
        help=_("All the messages with a lower (older) ID "
               "or equal to this will be excluded. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-aof', '--add-offset',
        metavar=_('int'),
        type=int,
        default=0,
        help=_("Additional message offset "
               "(all of the specified offsets + this offset = older messages). "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-s', '--search',
        metavar=_('str'),
        help=_("The string to be used as a search query. "
               "Give the same result as other Telegram official clients "
               "meaning it's not optimized for some non-English languages. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-f', '--filter',
        metavar=_('type'),
        help=_("The filter to use before returning messages. "
               "For instance, \"photos\" for \"InputMessagesFilterPhotos\" "
               "would yield only messages containing photos. "
               "When using \"empty\" filter, you must give option \"--search\". "
               "Available MessagesFilters: chatphotos, contacts, document, "
               "empty, geo, gif, music, mentions, phonecalls, photovideo, "
               "photos, roundvideo, roundvoice, url, video, voice "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-wt', '--wait-time',
        metavar=_('int'),
        type=int,
        help=_("Wait time (in seconds) between different GetHistoryRequest. "
               "Use this parameter to avoid hitting the FloodWaitError as needed. "
               "If left to None, it will default to 1 second "
               "only if the limit is higher than 3000. "
               "If the ids parameter is used, "
               "this time will default to 10 seconds only "
               "if the amount of IDs is higher than 300. "
               "(arg_num = 1)")
    )

    iter_messages_group.add_argument(
        '-ids', '--ids',
        metavar=_('int'),
        type=int,
        nargs='*',
        help=_("A single integer ID (or several IDs) for the message "
               "that should be returned. This parameter takes precedence "
               "over the rest (which will be ignored if this is set). "
               "This can for instance be used to get the message "
               "with ID 123 from a channel. Note that if the message "
               "doesn't exist, None will appear in its place, "
               "so that zipping the list of IDs with the messages "
               "can match one-to-one. "
               "(arg_num >= 1)")
    )

    iter_messages_group.add_argument(
        '-r', '--reverse',
        action='store_true',
        help=_("The messages will be returned in reverse order"
               " (from oldest to newest, instead of the default newest to oldest). "
               "This also means that the meaning of \"--offset-id\" and \"--offset-day\" "
               "parameters is reversed, although they will still be exclusive. "
               "\"--min-id\" becomes equivalent to \"--offset-id\" "
               "instead of being \"--max-id\" as "
               "well since messages are returned in ascending order. "
               "(arg_num = 0)"))

    operation_group.add_argument(
        '-op', '--only-print',
        action='store_true',
        help=_("Only print message instead of deleting them. "
               "(arg_num = 0)"))

    operation_group.add_argument(
        '-fs', '--filters',
        nargs='*',
        metavar=_('type'),
        help=_("The filters to use after returning the messages from \"iter_messages\". "
               "It run slower than option \"--filter\", but supports multiple filters. "
               "And it support \"empty\" type without input \"--search\". "
               "Available MessageMedia filters: contact, document, empty, "
               "game, geo, geolive, invoice, photo, poll, unsupported, "
               "venue, webpage "
               "Ref: https://tl.telethon.dev/types/message_media.html"
               "(arg_num >= 1)")
    )

    info_group.add_argument(
        '-ll', '--log-level',
        metavar=_('int'),
        type=int,
        default=2,
        choices=range(1, 3),
        help=_("Print different kinds of messages. "
               "0 for nothing. 1 for basic. 2 for more content. (arg_num = 1)"))

    info_group.add_argument(
        '-h', '--help',
        action='help',
        help=_("Show %(prog)s help message and exit. (arg_num = 0)"))

    return parser.parse_args()
