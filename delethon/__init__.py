#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines delethon's commandline entry point functionality.
"""

# Import built-in modules
import os
import datetime
import gettext

# Import third-party modules
import telethon
import socks
import pytz


# Any changes to the path and your own modules
from delethon import options
from delethon import constants


INIT_TEXT = gettext.translation(domain=__name__,
                                localedir=constants.LOCALE_PATH,
                                languages=[constants.CURRENT_LOCALE],
                                fallback=True)

try:
    _ = INIT_TEXT.ugettext
except AttributeError:
    # Python 3 fallback
    _ = INIT_TEXT.gettext


async def iter_users_msg(  # pylint: disable=too-many-arguments, too-many-branches
        # pylint: disable=unidiomatic-typecheck, too-many-statements
        args,
        chat_entity,
        client,
        msg_filter=None,
        media_filters=None,
        user=None):
    """
    Get or delete the message from iter_messages.
    Ref: https://docs.telethon.dev/en/latest/modules/custom.html#module-telethon.tl.custom.message
    """
    msg_count = 0
    id_user_dict = {}
    if not user:
        async for message in client.iter_messages(
                chat_entity,
                limit=args.limit,
                offset_date=args.offset_day,
                offset_id=args.offset_id,
                max_id=args.max_id,
                min_id=args.min_id,
                add_offset=args.add_offset,
                search=args.search,
                filter=msg_filter,
                wait_time=args.wait_time,
                ids=args.ids,
                reverse=args.reverse):
            if media_filters:
                if message.media:
                    # https://docs.telethon.dev/en/latest/modules/custom.html#module-telethon.tl.custom.message
                    # None for "convenience"
                    if type(message.media) not in media_filters:
                        continue
                else:
                    if telethon.types.MessageMediaEmpty not in media_filters:
                        continue
            if args.log_level == 0:
                await client.delete_messages(chat_entity, message.id)
                continue
            if args.log_level == 1:
                print("id: {user_id} {date}".format(
                    user_id=message.from_id,
                    date=message.date))
            elif args.log_level == 2:
                user_entity = id_user_dict.get(message.from_id)
                if user_entity:
                    print("{first_name} {last_name}(@{username})"
                          "(uid: {user_id}) {date} (mid: {msg_id})".format(
                              first_name=user_entity.first_name,
                              last_name=user_entity.last_name,
                              username=user_entity.username,
                              user_id=message.from_id,
                              date=message.date,
                              msg_id=message.id))
                else:
                    id_user_dict[message.from_id] = await client.get_entity(message.from_id)
                    print("{first_name} {last_name}(@{username})"
                          "(uid: {user_id}) {date} (mid: {msg_id})".format(
                              first_name=id_user_dict[message.from_id].first_name,
                              last_name=id_user_dict[message.from_id].last_name,
                              username=id_user_dict[message.from_id].username,
                              user_id=message.from_id,
                              date=message.date,
                              msg_id=message.id))
            print(message.message)
            print()
            msg_count = msg_count + 1
            if not args.only_print:
                await client.delete_messages(chat_entity, message.id)
    else:
        user_entity = await client.get_entity(user)
        async for message in client.iter_messages(
                chat_entity,
                limit=args.limit,
                offset_date=args.offset_day,
                offset_id=args.offset_id,
                max_id=args.max_id,
                min_id=args.min_id,
                add_offset=args.add_offset,
                search=args.search,
                filter=msg_filter,
                wait_time=args.wait_time,
                ids=args.ids,
                reverse=args.reverse,
                from_user=user):
            if media_filters:
                if message.media:
                    # https://docs.telethon.dev/en/latest/modules/custom.html#module-telethon.tl.custom.message
                    # None for "convenience"
                    if type(message.media) not in media_filters:
                        continue
                else:
                    if telethon.types.MessageMediaEmpty not in media_filters:
                        continue
            if args.log_level == 0:
                await client.delete_messages(chat_entity, message.id)
                continue
            if args.log_level == 1:
                print("uid: {user_id} {date} (mid: {msg_id})".format(
                    user_id=message.from_id,
                    date=message.date,
                    msg_id=message.id))
            elif args.log_level == 2:
                print("{first_name} {last_name}(@{username})"
                      "(uid: {user_id}) {date} (mid: {msg_id})".format(
                          first_name=user_entity.first_name,
                          last_name=user_entity.last_name,
                          username=user_entity.username,
                          user_id=message.from_id,
                          date=message.date,
                          msg_id=message.id))
            print(message.message)
            print()
            msg_count = msg_count + 1
            if not args.only_print:
                await client.delete_messages(chat_entity, message.id)
    if args.log_level == 0:
        return 0

    chat = await client.get_entity(chat_entity)

    if isinstance(chat, telethon.types.User):
        title = chat.username
    else:
        title = chat.title

    if not args.only_print:
        print(_("\nDelete {msg_count} messages in chat \"{chat}\"(id: {chat_id}).").format(
            msg_count=msg_count,
            chat=title,
            chat_id=chat.id))
    else:
        print(_("\nPrint {msg_count} messages in chat \"{chat}\"(id: {chat_id}).").format(
            msg_count=msg_count,
            chat=title,
            chat_id=chat.id))
    return msg_count


async def iter_dialog(  # pylint: disable=too-many-branches, too-many-statements
        args,
        client,
        msg_filter,
        media_filters=None):
    """
    Get or delete the message from client.
    """
    user_list = []

    total = 0

    if args.me:
        user_list.append(await client.get_me())

    if not args.users and not user_list:
        if args.all_chats:
            async for chat_entity in client.iter_dialogs(limit=None):
                total = total + await iter_users_msg(
                    args,
                    chat_entity=chat_entity,
                    client=client,
                    msg_filter=msg_filter,
                    media_filters=media_filters)
        else:
            if not args.chats:
                if args.log_level > 0:
                    print("Error: No chats input.")
                    return 1
            for chat in args.chats:
                try:
                    chat_entity = await client.get_input_entity(chat)
                except ValueError as error:
                    chat_entity = None
                    try:
                        chat_id = int(chat)
                        async for dialog in client.iter_dialogs(limit=None):
                            if dialog.id == chat_id:
                                chat_entity = dialog
                    except ValueError:
                        async for dialog in client.iter_dialogs(limit=None):
                            if dialog.name == chat:
                                chat_entity = dialog
                    if not chat_entity:
                        raise error
                total = total + await iter_users_msg(
                    args,
                    chat_entity=chat_entity,
                    client=client,
                    msg_filter=msg_filter,
                    media_filters=media_filters)

        if not args.only_print:
            if args.log_level > 0:
                print(_("Delete {msg_count} messages in total.").format(
                    msg_count=total))
        else:
            print(_("Print {msg_count} messages in total.").format(
                msg_count=total))

    else:
        if args.users:
            for user in args.users:
                user_entity = await client.get_input_entity(user)
                user_list.append(user_entity)

        if args.all_chats:
            async for chat_entity in client.iter_dialogs(limit=None):
                for user in user_list:
                    total = total + await iter_users_msg(
                        args,
                        chat_entity=chat_entity,
                        client=client,
                        user=user,
                        msg_filter=msg_filter,
                        media_filters=media_filters)
        else:
            for chat in args.chats:
                try:
                    chat_entity = await client.get_input_entity(chat)
                except ValueError as error:
                    chat_entity = None
                    try:
                        chat_id = int(chat)
                        async for dialog in client.iter_dialogs(limit=None):
                            if dialog.id == chat_id:
                                chat_entity = dialog
                    except ValueError:
                        async for dialog in client.iter_dialogs(limit=None):
                            if dialog.name == chat:
                                chat_entity = dialog
                    if not chat_entity:
                        raise error
                for user in user_list:
                    total = total + await iter_users_msg(
                        args,
                        chat_entity=chat_entity,
                        client=client,
                        user=user,
                        msg_filter=msg_filter,
                        media_filters=media_filters)


def str_to_msg_filter(filter_str):  # pylint: disable=too-many-branches
    """
    Get types.InputMessagesFilter from filter_str
    """
    if filter_str.lower() == "chatphotos":
        msg_filter = \
            telethon.types.InputMessagesFilterChatPhotos
    elif filter_str.lower() == "contacts":
        msg_filter = \
            telethon.types.InputMessagesFilterContacts
    elif filter_str.lower() == "document":
        msg_filter = \
            telethon.types.InputMessagesFilterDocument
    elif filter_str.lower() == "empty":
        msg_filter = \
            telethon.types.InputMessagesFilterEmpty
    elif filter_str.lower() == "geo":
        msg_filter = \
            telethon.types.InputMessagesFilterGeo
    elif filter_str.lower() == "gif":
        msg_filter = \
            telethon.types.InputMessagesFilterGif
    elif filter_str.lower() == "music":
        msg_filter = \
            telethon.types.InputMessagesFilterMusic
    elif filter_str.lower() == "mentions":
        msg_filter = \
            telethon.types.InputMessagesFilterMyMentions
    elif filter_str.lower() == "phonecalls":
        msg_filter = \
            telethon.types.InputMessagesFilterPhoneCalls
    elif filter_str.lower() == "photovideo":
        msg_filter = \
            telethon.types.InputMessagesFilterPhotoVideo
    elif filter_str.lower() == "photos":
        msg_filter = \
            telethon.types.InputMessagesFilterPhotos
    elif filter_str.lower() == "roundvideo":
        msg_filter = \
            telethon.types.InputMessagesFilterRoundVideo
    elif filter_str.lower() == "roundvoice":
        msg_filter = \
            telethon.types.InputMessagesFilterRoundVoice
    elif filter_str.lower() == "url":
        msg_filter = \
            telethon.types.InputMessagesFilterUrl
    elif filter_str.lower() == "video":
        msg_filter = \
            telethon.types.InputMessagesFilterVideo
    elif filter_str.lower() == "voice":
        msg_filter = \
            telethon.types.InputMessagesFilterVoice
    else:
        msg_filter = None

    return msg_filter


def str_to_media_filter(filter_str):  # pylint: disable=too-many-branches
    """
    Get types.TypeMessageMedia from filter_str
    """
    if filter_str.lower() == "contact":
        media_filter = \
            telethon.types.MessageMediaContact
    elif filter_str.lower() == "document":
        media_filter = \
            telethon.types.MessageMediaDocument
    elif filter_str.lower() == "empty":
        media_filter = \
            telethon.types.MessageMediaEmpty
    elif filter_str.lower() == "game":
        media_filter = \
            telethon.types.MessageMediaGame
    elif filter_str.lower() == "geo":
        media_filter = \
            telethon.types.MessageMediaGeo
    elif filter_str.lower() == "geolive":
        media_filter = \
            telethon.types.MessageMediaGeoLive
    elif filter_str.lower() == "invoice":
        media_filter = \
            telethon.types.MessageMediaInvoice
    elif filter_str.lower() == "photo":
        media_filter = \
            telethon.types.MessageMediaPhoto
    elif filter_str.lower() == "poll":
        media_filter = \
            telethon.types.MessageMediaPoll
    elif filter_str.lower() == "unsupported":
        media_filter = \
            telethon.types.MessageMediaUnsupported
    elif filter_str.lower() == "venue":
        media_filter = \
            telethon.types.MessageMediaVenue
    elif filter_str.lower() == "webpage":
        media_filter = \
            telethon.types.MessageMediaWebPage
    else:
        media_filter = None

    return media_filter


def main():  # pylint: disable=too-many-branches
    """
    Run delethon as a command-line program.
    """
    args = options.get_cmd_args()

    if not args.api_id:
        if args.log_level > 0:
            print("Error: No api_id input.")
            return 1

    if not args.api_hash:
        if args.log_level > 0:
            print("Error: No api_hash input.")
            return 1

    if args.log_level == 0 and args.only_print:
        return 1

    if args.proxy_type == "SOCKS5":
        client = telethon.TelegramClient(
            args.session_file,
            args.api_id,
            args.api_hash,
            proxy=(socks.SOCKS5,
                   args.proxy_address,
                   args.proxy_port,
                   args.proxy_username,
                   args.proxy_password))
    elif args.proxy_type == "SOCKS4":
        client = telethon.TelegramClient(
            args.session_file,
            args.api_id,
            args.api_hash,
            proxy=(socks.SOCKS4,
                   args.proxy_address,
                   args.proxy_port,
                   args.proxy_username,
                   args.proxy_password))
    elif args.proxy_type == "HTTP":
        client = telethon.TelegramClient(
            args.session_file,
            args.api_id,
            args.api_hash,
            proxy=(socks.HTTP,
                   args.proxy_address,
                   args.proxy_port,
                   args.proxy_username,
                   args.proxy_password))
    elif args.proxy_type == "MTPROTO":
        client = telethon.TelegramClient(
            args.session_file,
            args.api_id,
            args.api_hash,
            connection=
            telethon.connection.ConnectionTcpMTProxyRandomizedIntermediate,
            proxy=(args.proxy_address,
                   args.proxy_port,
                   args.proxy_password))
    elif os.environ.get("HTTP_PROXY"):
        http_proxy_list = os.environ["HTTP_PROXY"].split(":")
        client = telethon.TelegramClient(
            args.session_file,
            args.api_id,
            args.api_hash,
            proxy=(socks.HTTP,
                   http_proxy_list[1][2:],
                   int(http_proxy_list[2]),
                   args.proxy_username,
                   args.proxy_password))
    else:
        client = telethon.TelegramClient(
            args.session_file,
            args.api_id,
            args.api_hash)

    client.start()

    if args.offset_day:
        utc = pytz.UTC()
        args.offset_day = utc.localize(
            datetime.datetime.today() - datetime.timedelta(days=args.offset_day))

    if args.filter:
        msg_filter = str_to_msg_filter(args.filter)
    else:
        msg_filter = None

    if args.filters:
        media_filters = []
        for filter_str in args.filters:
            media_filter = str_to_media_filter(filter_str)
            if media_filter:
                media_filters.append(media_filter)
    else:
        media_filters = None

    with client:
        client.loop.run_until_complete(iter_dialog(
            args,
            client,
            msg_filter,
            media_filters))

    return 0
