# Delethon

<escape><a href="https://travis-ci.org/BingLingGroup/delethon"><img src="https://travis-ci.org/BingLingGroup/delethon.svg?branch=dev"></img></a></escape>

[简体中文](docs/README.zh-Hans.md)

[Changelog](CHANGELOG.md)

<escape><img src="docs/icon/delethon.png" width="64px"></escape>

Icon font: [source-han-serif](https://source.typekit.com/source-han-serif/) ([OFL 1.1](https://github.com/adobe-fonts/source-han-serif/blob/master/LICENSE.txt))

### TOC

1. [Description](#description)
2. [License](#license)
3. [Dependencies](#dependencies)
4. [Download and Installation](#download-and-installation)
   - 4.1 [Branches](#branches)
   - 4.2 [Install on Ubuntu](#install-on-ubuntu)
   - 4.3 [Install on Windows](#install-on-windows)
5. [Usage](#usage)
   - 6.1 [Typical usage](#typical-usage)
   - 6.2 [Options](#Options)
   - 6.3 [Internationalization](#internationalization)
6. [Bugs report](#bugs-report)
7. [Build](#build)

Click up arrow to go back to TOC.

### Description

Delete Telegram messages based on Telethon.

It can do:

- [x] Delete the messages of the logged in user for all members in group chats.
- [x] Delete certain types of the messages.
- [x] Print instead of deleting the messages.

It can not do:

- [ ] Delete the messages that's been cached or exported to the local storage.
- [ ] Delete the messages in group's recent actions.
- [ ] Delete other people's messages for all in group chats unless you have the admin rights of the group.

### License

[GPLv3](LICENSE)

### Dependencies

[requirements.txt](requirements.txt)

Python >= 3.5

### Download and Installation

About the git installation. If you don't want to install git to use pip [VCS](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support) support to install python package or just confused with git environment variables, you can manually click that clone and download button to download the source code and use pip to install the source code [locally](https://pip.pypa.io/en/stable/reference/pip_install/#description) by input these commands.

```batch
cd the_directory_contains_the_source_code
pip install .
```

#### Branches

[master branch](https://github.com/BingLingGroup/delethon/tree/master)

- Codes will be updated when a new version releases.

[dev branch](https://github.com/BingLingGroup/delethon/tree/dev)

- The latest codes will be pushed to this branch. It will be merged to master branch when new version released.

<escape><a href = "#TOC">&nbsp;↑&nbsp;</a></escape>

#### Install on Ubuntu

Include dependencies installation commands.

Install from `master` branch.

```bash
apt install python3 python3-pip git -y
pip3 install git+https://github.com/BingLingGroup/delethon.git@master
```

<escape><a href = "#TOC">&nbsp;↑&nbsp;</a></escape>

#### Install on Windows

You can just go to the [release page](https://github.com/BingLingGroup/delethon/releases) and download the latest release for Windows. The click-and-run batches are also in the package. You can manually edit by using Notepad++. Or add the executable files' directory to system environment variables so you can use it as a universal command everywhere in the system if permission is Ok.

Tips: `Shift - Right Click` is the keyboard shortcut for opening a Powershell on current directory. To open an exe at current directory, the format is like `.\delethon`.

Or install Python environment(if you still don't have one) from [choco](https://chocolatey.org) and then install the package.

Choco installation command is for cmd.(not Powershell)

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

Install from `master` branch.

```batch
choco install git python curl -y
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install git+https://github.com/BingLingGroup/delethon.git@master
```

<escape><a href = "#TOC">&nbsp;↑&nbsp;</a></escape>

### Usage

You need to get the `api_id` and `api_hash` from [Telegram app](https://my.telegram.org/apps) to log in. Remember not to post these codes anywhere or give them to anyone.

If the user is logged in for the first time or the session file is not ready, it will ask for a login authentication just like other Telegram clients.

Typical usages for delethon instead of other Telegram clients:

- Delete all messages of the logged in user in group chats instead of asking their admin's for help.
- Delete all messages of the group chats on schedule if the logged in user is the admin of some group chats.

Log in behind local `SOCKS5` proxy `127.0.0.1:1080`

```
delethon -pt ...(other options)
```

Delete all messages of logged in user in some chats.

```
delethon -ai api_id -ah api_hash -c "chat_1" "chat_2" -m ...(other options)
```

Delete quietly.

```
delethon -ll 0 ...(other options)
```

Delete text messages only. (But won't delete those photo messages with caption)

```
delethon -fs empty ...(other options)
```

<escape><a href = "#TOC">&nbsp;↑&nbsp;</a></escape>

#### Options

Full list of the help message.

```
$ delethon -h
usage:
  delethon [options]

Delete Telegram messages based on Telethon.

Client Options:
  Options to start a Telethon client.

  -ai API_ID, --api-id API_ID
                        Telegram app api_id. Input it or set the environment
                        variable "TELEGRAM_API_ID". You can get one from
                        https://my.telegram.org/apps (arg_num = 1) (default:
                        None)
  -ah API_HASH, --api-hash API_HASH
                        Telegram app api_hash. Input it or set the environment
                        variable "TELEGRAM_API_HASH". You can get one from
                        https://my.telegram.org/apps (arg_num = 1) (default:
                        None)
  -sf path, --session-file path
                        Telegram session file path. Ref: https://docs.telethon
                        .dev/en/latest/concepts/sessions.html (arg_num = 1)
                        (default: Telethon)

Proxy Options:
  Options to use Telethon behind a proxy.

  -pt [proxy_type], --proxy-type [proxy_type]
                        PySocks or MTProto Proxy. Available types: "SOCKS5",
                        "SOCKS4", "HTTP", "MTPROTO". When using "MTPROTO", its
                        type is "ConnectionTcpMTProxyRandomizedIntermediate".
                        If environment variable "HTTP_PROXY" exists and this
                        option is not used, it will use it. Ref:
                        https://docs.telethon.dev/en/latest/basic/signing-
                        in.html#signing-in-behind-a-proxy If arg_num is 0, use
                        const type. (arg_num = 0 or 1) (const: SOCKS5)
  -pa address, --proxy-address address
                        The IP address or DNS name of the proxy server.
                        (arg_num = 1) (default: 127.0.0.1)
  -pp port, --proxy-port port
                        The port of the proxy server. (arg_num = 1) (default:
                        1080)
  -pu username, --proxy-username username
                        Set proxy username. (arg_num = 1)
  -ps password, --proxy-password password
                        Set proxy password. When using "MTPROTO", this option
                        is "secret" instead. (arg_num = 1)

Iterate Messages Options:
  Options to control Telethon iter_messages method. Ref: https://docs.telethon.dev/en/latest/modules/client.html#telethon.client.messages.MessageMethods.iter_messages

  -c [entity_like [entity_like ...]], --chats [entity_like [entity_like ...]]
                        Get the messages in the chat entity/entities.
                        entity_like can be Telegram username, Group name and
                        so on. If failed to get one, it will use it to match
                        the entity name or id of the dialogs which the user
                        joined. Ref: https://docs.telethon.dev/en/latest/conce
                        pts/entities.html#getting-entities(arg_num >= 1)
  -u [entity_like [entity_like ...]], --users [entity_like [entity_like ...]]
                        Get the messages from the user entity/entities. If not
                        input, gets all users messages. Ref: https://docs.tele
                        thon.dev/en/latest/concepts/entities.html#getting-
                        entities(arg_num >= 1)
  -m, --me              Get messages from the current user who is logged in.
                        (arg_num = 0)
  -ac, --all-chats      Iterate over all the chat entity/entities that the
                        current user joined. (arg_num = 0)
  -l int, --limit int   Number of messages to be retrieved. Slower when more
                        than 3000. Ref: https://docs.telethon.dev/en/latest/mo
                        dules/client.html#telethon.client.messages.MessageMeth
                        ods.iter_messages (arg_num = 1) (default: unlimited)
  -ofd int, --offset-day int
                        Offset day (messages previous to this day will be
                        retrieved). Exclusive. (arg_num = 1)
  -ofi int, --offset-id int
                        Offset message ID (only messages previous to the given
                        ID will be retrieved). Exclusive. (arg_num = 1)
  -mxi int, --max-id int
                        All the messages with a higher (newer) ID or equal to
                        this will be excluded. (arg_num = 1)
  -mni int, --min-id int
                        All the messages with a lower (older) ID or equal to
                        this will be excluded. (arg_num = 1)
  -aof int, --add-offset int
                        Additional message offset (all of the specified
                        offsets + this offset = older messages). (arg_num = 1)
  -s str, --search str  The string to be used as a search query. Give the same
                        result as other Telegram official clients meaning it's
                        not optimized for some non-English languages. (arg_num
                        = 1)
  -f type, --filter type
                        The filter to use before returning messages. For
                        instance, "photos" for "InputMessagesFilterPhotos"
                        would yield only messages containing photos. When
                        using "empty" filter, you must give option "--search".
                        Available MessagesFilters: chatphotos, contacts,
                        document, empty, geo, gif, music, mentions,
                        phonecalls, photovideo, photos, roundvideo,
                        roundvoice, url, video, voice (arg_num = 1)
  -wt int, --wait-time int
                        Wait time (in seconds) between different
                        GetHistoryRequest. Use this parameter to avoid hitting
                        the FloodWaitError as needed. If left to None, it will
                        default to 1 second only if the limit is higher than
                        3000. If the ids parameter is used, this time will
                        default to 10 seconds only if the amount of IDs is
                        higher than 300. (arg_num = 1)
  -ids [int [int ...]], --ids [int [int ...]]
                        A single integer ID (or several IDs) for the message
                        that should be returned. This parameter takes
                        precedence over the rest (which will be ignored if
                        this is set). This can for instance be used to get the
                        message with ID 123 from a channel. Note that if the
                        message doesn't exist, None will appear in its place,
                        so that zipping the list of IDs with the messages can
                        match one-to-one. (arg_num >= 1)
  -r, --reverse         The messages will be returned in reverse order (from
                        oldest to newest, instead of the default newest to
                        oldest). This also means that the meaning of "--
                        offset-id" and "--offset-day" parameters is reversed,
                        although they will still be exclusive. "--min-id"
                        becomes equivalent to "--offset-id" instead of being "
                        --max-id" as well since messages are returned in
                        ascending order. (arg_num = 0)

Process Options:
  Options to determine how to process the messages after retrieving them.

  -op, --only-print     Only print message instead of deleting them. (arg_num
                        = 0)
  -fs [type [type ...]], --filters [type [type ...]]
                        The filters to use after returning the messages from
                        "iter_messages". So using it will delete equal to or
                        less amount of messages than the argument set to "--
                        limit". It run slower than option "--filter", but
                        supports multiple filters. And it support "empty" type
                        without input "--search". Available MessageMedia
                        filters: contact, document, empty, game, geo, geolive,
                        invoice, photo, poll, unsupported, venue, webpage Ref:
                        https://tl.telethon.dev/types/message_media.html(arg_n
                        um >= 1)

Information Options:
  Options to get extra information.

  -ll int, --log-level int
                        Print different kinds of messages. 0 for nothing. 1
                        for basic. 2 for more content. (arg_num = 1) (default:
                        2)
  -h, --help            Show delethon help message and exit. (arg_num = 0)
  -v, --version         Show delethon version and exit. (arg_num = 0)

Make sure the argument with space is in quotes.
The default value is used
when the option is not given at the command line.
"(arg_num)" means if the option is given,
the number of the arguments is required.
Author: Bing Ling
Email: binglinggroup@outlook.com
Bug report: https://github.com/BingLingGroup/delethon
```

<escape><a href = "#TOC">&nbsp;↑&nbsp;</a></escape>

#### Internationalization

Delethon supports multi-language command line user interface by [GNU gettext](https://www.gnu.org/software/gettext/). Now supports `zh_CN` and default `en_US`. More info about this [lang codes format](https://www.gnu.org/software/gettext/manual/gettext.html#Locale-Names). The program will automatically detect the os locale and use the one supported. For windows 10, it seems adjusting the `Region`-`Regional format` is Ok.

Of course, delethon offers a method to override the os locale. Just create a txt file without extension named `locale`, containing the lang codes at the beginning of the file, at the command line current working directory. When delethon starts, it will detect this file and read the lang code inside it and apply it if supported.

If you want to translate this program into other languages, first install the gettext utilities. Then you can run `python scripts/update_po_files.py lang_code` to create the locale files which you want to translate into. And then use [POEditor](https://poeditor.com/) to edit po files. [update_po_files.py](scripts/update_po_files.py) can also automatically merge the position info into the old po files and compile the po files into mo files which the program read them. So it's useful when the codes changed, you can merge the positional changes into the translations automatically.

<escape><a href = "#TOC">&nbsp;↑&nbsp;</a></escape>

### Bugs report

Bugs and suggestions can be reported at [issues](https://github.com/BingLingGroup/delethon/issues).

### Build

Current windows build is built by [pyinstaller script](scripts/pyinstaller_build.bat).

[create_release.py](scripts/create_release.py) is used to make the release package.
