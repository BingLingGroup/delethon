# Delethon

<escape><a href="https://travis-ci.org/BingLingGroup/delethon"><img src="https://travis-ci.org/BingLingGroup/delethon.svg?branch=dev"></img></a></escape>

[English](../README.md)

[更新日志](../CHANGELOG.md)

<escape><img src="icon/delethon.png" width="64px"></escape>

图标字体: [source-han-serif](https://source.typekit.com/source-han-serif/) ([OFL 1.1](https://github.com/adobe-fonts/source-han-serif/blob/master/LICENSE.txt))

### 目录

1. [介绍](#介绍)
2. [证书](#证书)
3. [依赖](#依赖)
4. [下载和安装](#下载和安装)
   - 4.1 [分支](#分支)
   - 4.2 [在Ubuntu安装](#在ubuntu安装)
   - 4.3 [在Windows安装](#在windows安装)
5. [用法](#用法)
   - 6.1 [典型用法](#典型用法)
   - 6.2 [选项](#选项)
   - 6.3 [国际化](#国际化)
6. [问题报告](#问题报告)
7. [构建](#构建)

点击上箭头以返回目录。

### 介绍

基于Telethon删除Telegram消息。

它能做到:

- [x] 删除登录用户在群聊的消息，删除后所有人不可见。
- [x] 删除特定种类的消息。
- [x] 打印而不是删除消息。

它不能做到：

- [ ] 删除已被缓存或者导出到本地的消息。
- [ ] 删除群组最近活动中的消息。
- [ ] 删除群组中其他人的消息，除非你有群组管理员权限。

### 证书

[GPLv3](../LICENSE)

### 依赖

[requirements.txt](../requirements.txt)

Python >= 3.5

### 下载和安装

至于git的安装，如果你不想通过pip的[VCS](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support)支持来安装python包或者只是不想碰git的环境变量这些东西，你可以手动点击clone and download来下载源码并在[本地](https://pip.pypa.io/en/stable/reference/pip_install/#description)进行安装。指令如下。

```batch
cd the_directory_contains_the_source_code
pip install .
```

#### 分支

[master分支](https://github.com/BingLingGroup/delethon/tree/master)

- 代码会在新版本发布时更新。

[dev分支](https://github.com/BingLingGroup/delethon/tree/dev)

- 最新的代码会推送到这个分支。如果有新版本发布，会被合并到master分支。

<escape><a href = "#目录">&nbsp;↑&nbsp;</a></escape>

#### 在Ubuntu安装

包括依赖安装指令。

从`master`分支安装。

```bash
apt install python3 python-pip3 git -y
pip3 install git+https://github.com/BingLingGroup/delethon.git@master
```

<escape><a href = "#目录">&nbsp;↑&nbsp;</a></escape>

#### 在Windows安装

你可以直接去[发布页](https://github.com/BingLingGroup/delethon/releases)下载Windows的最新发布版。包内自带懒人批处理。你可以使用Notepad++对其进行手动修改。或者把含有exe的目录放到系统环境变量里，这样你就可以在别的目录也使用delethon了，前提是那个目录没有权限限制。

建议：`Shift - 右键`是打开当前目录Powershell的快捷键。Powershell打开当前目录的exe需要输入这样的格式`.\delethon`。

或者通过[choco](https://chocolatey.org)来安装Python环境（如果你还没有），然后安装这个包。

命令行安装choco的指令如下。（不是Powershell）

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

从`master`分支安装。

```batch
choco install git python curl -y
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install git+https://github.com/BingLingGroup/delethon.git@master
```

<escape><a href = "#目录">&nbsp;↑&nbsp;</a></escape>

### Usage

你需要从[Telegram app](https://my.telegram.org/apps)中获得`api_id`和`api_hash`来登录。记得不要把这些编号发出去或者透露给任何人。

如果用户是第一次登录，或者会话文件尚不存在，程序会请求登录验证，和其他Telegram客户端一样。

不使用其他Telegram客户端，而使用delethon的几个典型场景：

- 删除已登录用户在群组中的所有记录，而不是要求群组管理员协助删除。
- 如果已登录用户是群组管理员，可以让其定时删除所有群组聊天记录。

使用本地`SOCKS5`代理`127.0.0.1:1080`登录。

```
delethon -pt ...(其他选项)
```

删除某些聊天中已登录用户的消息。

```
delethon -ai api_id -ah api_hash -c "聊天1" "聊天2" -m ...(其他选项)
```

安静地删除。

```
delethon -ll 0 ...(其他选项)
```

只删除文字消息。（但不包括含文字的照片消息）

```
delethon -fs empty ...(其他选项)
```

<escape><a href = "#目录">&nbsp;↑&nbsp;</a></escape>

#### 选项

帮助信息的完整清单。

```
$ delethon -h
usage:
  用法：delethon [选项]

基于Telethon删除Telegram消息。

客户端选项:
  用于启动Telethon客户端的选项。

  -ai API_ID, --api-id API_ID
                        Telegram应用api_id。输入它或者设置环境变量“TELEGRAM_API_ID”。你能从https
                        ://my.telegram.org/apps中获得一个。（参数个数为1）（默认参数为None）
  -ah API_HASH, --api-hash API_HASH
                        Telegram应用api_hash。输入它或者设置环境变量“TELEGRAM_API_HASH”。你能从h
                        ttps://my.telegram.org/apps中获得一个。（参数个数为1）（默认参数为None）
  -sf 路径, --session-file 路径
                        Telegram会话文件路径。参考：https://docs.telethon.dev/en/latest/
                        concepts/sessions.html（参数个数为1）（默认参数为Telethon）

代理选项:
  让Telethon使用代理服务器的选项。

  -pt [代理类型], --proxy-type [代理类型]
                        PySocks或者MTProto代理。可用类型："SOCKS5", "SOCKS4", "HTTP", "M
                        TPROTO"。使用"MTPROTO"时，其类型为"ConnectionTcpMTProxyRandomiz
                        edIntermediate"。如果环境变量"HTTP_PROXY"存在，而这个选项没有使用，程序就会用它。
                        参考：https://docs.telethon.dev/en/latest/basic/signing-
                        in.html#signing-in-behind-a-proxy
                        如果参数个数是0，使用const类型。（参数个数为0或1）（const为SOCKS5）
  -pa 地址, --proxy-address 地址
                        IP地址或者代理服务器的DNS名称。（参数个数为1）（默认参数为127.0.0.1）
  -pp 端口, --proxy-port 端口
                        代理服务器的端口。（参数个数为1）（默认参数为1080）
  -pu 用户名, --proxy-username 用户名
                        设置代理用户名。（参数个数为1）
  -ps 密码, --proxy-password 密码
                        设置代理密码。如果使用"MTPROTO"，这个参数则会代表"secret"。（参数个数为1）

迭代消息选项:
  用于控制Telethon iter_messages方法的选项。参考：https://docs.telethon.dev/en/latest/modules/client.html#telethon.client.messages.MessageMethods.iter_messages

  -c [实体类 [实体类 ...]], --chats [实体类 [实体类 ...]]
                        从单个对话实体或多个对话实体中获取消息。实体类可以是Telegram用户名，群名等等。如果无法得到，程序会使
                        用此选项去匹配用户已经加入的对话的实体名称或者id。参考：https://docs.telethon.dev
                        /en/latest/concepts/entities.html#getting-
                        entities（参数个数大于等于1）
  -u [实体类 [实体类 ...]], --users [实体类 [实体类 ...]]
                        从单个用户实体或多个用户实体获得消息。如果没有输入，会获取所有用户的消息。参考https://docs.te
                        lethon.dev/en/latest/concepts/entities.html#getting-
                        entities（参数个数大于等于1）
  -m, --me              获取当前登录用户发送的消息。（参数个数为0）
  -ac, --all-chats      获得当前登录用户参加的所有对话实体。（参数个数为0）
  -l 整数, --limit 整数     需要取回的消息数量。超过3000时会变慢。参考：https://docs.telethon.dev/en/l
                        atest/modules/client.html#telethon.client.messages.Mes
                        sageMethods.iter_messages （参数个数为1）（默认不限制数量）
  -ofd 整数, --offset-day 整数
                        偏移日期（比这天早的消息会被取回）。独占性。（参数个数为1）
  -ofi 整数, --offset-id 整数
                        偏移消息ID（只有比这个ID更早的消息才会被取回）。独占性。（参数个数为1）
  -mxi 整数, --max-id 整数  所有比这个ID数值更高也就是更新的消息会被排除。（参数个数为1）
  -mni 整数, --min-id 整数  所有比这个ID数值更小也就是更旧的消息会被排除。（参数个数为1）
  -aof 整数, --add-offset 整数
                        额外消息偏移（所有制ID那个的偏移加上这个偏移=更旧的消息）。（参数个数为1）
  -s 字符串, --search 字符串  用来搜索的字符串。和其他Telegram官方客户端得到的搜索结果一样，意味着对部分非英语语言未做优化。（参数
                        个数为1）
  -f 类型, --filter 类型    在取回消息前进行筛选的分类器。譬如，输入"photos"等同于"InputMessagesFilterPho
                        tos"将会只产生含图片的消息。使用"empty"筛选时，你必须提供"-s"选项。可用消息筛选类型：chat
                        photos, contacts, document, empty, geo, gif, music,
                        mentions, phonecalls, photovideo, photos, roundvideo,
                        roundvoice, url, video, voice（参数个数为1）
  -wt 整数, --wait-time 整数
                        在不同的GetHistoryRequest之间的等待时间（单位为秒）。使用这个选项来避免达到FloodWai
                        tError。如果不输入，超过3000个消息时的等待默认为1秒。如果id参数使用了，id超过300时，这个时
                        间将被设置为10秒。（参数个数为1）
  -ids [整数 [整数 ...]], --ids [整数 [整数 ...]]
                        会被取回的单个或多个消息ID。这个参数优先于其他参数。譬如可用于取得频道里第123条消息。注意如果消 息不存在
                        ，会返回None，所以将包含ID的列表压缩在一起能得到一对一的结果。（参数个数大于等于1）
  -r, --reverse         消息会倒序返回（从最旧的到最新的，而不是默认最新的到最旧的）。这也意味着选项"--offset-id"和"
                        --offset-day"中的参数也被反转了，尽管他们仍然是独占性的。 同样地，"--min-id"等效于"
                        --offset-id"而非"--max-id"因为消息会按照升序返回。（参数个数为0）

处理选项:
  在取回消息后决定如何处理消息的选项。

  -op, --only-print     只在屏幕上输出消息而非删除他们。（参数个数为0）
  -fs [类型 [类型 ...]], --filters [类型 [类型 ...]]
                        在从"iter_message"方法取回消息后进行筛选的分类器。所以使用它会删除小于等于"--
                        limit"选项提供的消息数量。会比选项"--
                        filter"更慢，但支持多个分类同时输入。同时在输入"empty"类时不需要输入"--
                        search"选项。可用的MessageMedia分类器：contact, document, empty,
                        game, geo, geolive, invoice, photo, poll, unsupported,
                        venue, webpage 参考：https://tl.telethon.dev/types/messag
                        e_media.html（参数个数大于等于1）

信息选项:
  用于获取额外信息的选项。

  -ll 整数, --log-level 整数
                        在屏幕上输出不同类别的消息。0为不输出。1为基本信息。2则是更多的信息。（参数个数为1）（默认参数为2）
  -h, --help            显示delethon的帮助信息并退出。（参数个数为0）
  -v, --version         显示delethon的版本信息并退出。（参数个数为0）

确保有空格的参数被引号包围。
默认参数指的是，
如果选项没有在命令行中提供时会使用的参数。
"参数个数"指的是如果提供了选项，
该选项所需要的参数个数。
作者: Bing Ling
Email: binglinggroup@outlook.com
问题反馈: https://github.com/BingLingGroup/delethon
```

<escape><a href = "#目录">&nbsp;↑&nbsp;</a></escape>

#### 国际化

Delethon通过[GNU gettext](https://www.gnu.org/software/gettext/)支持多语言命令行界面。现在支持`zh_CN`和`en_US`。关于这种语言代码的格式可见[此文档](https://www.gnu.org/software/gettext/manual/gettext.html#Locale-Names)。程序会自动检测操作系统的语言，并选择其支持的语言。对于windows 10而言，只要修改`区域`-`区域格式`即可。

当然，delethon提供了不依靠操作系统语言来加载语言的方法。只要创建一个txt文件，去掉它的文件扩展名，命名为`locale`，在文件开头的位置输入语言代码，同时该文件放在运行delethon命令行的目录，delethon就会自动检测并读取这个文件里的语言代码，如果支持就会自动加载该语言。

如果你想把这个程序翻译成别的语言，首先安装gettext工具。然后你可以运行`python scripts/update_po_files.py lang_code`来创建你要翻译的语言文件。然后使用[POEditor](https://poeditor.com/)来编辑po文件。[update_po_files.py](../scripts/update_po_files.py)也可以自动合并位置信息到旧的po文件，并将po文件编译成程序使用的mo文件。所以如果代码改变时，你可以通过这个脚本，自动地将位置信息变化合并到翻译中。

<escape><a href = "#目录">&nbsp;↑&nbsp;</a></escape>

### 问题反馈

问题和建议可以反馈在[issues](https://github.com/BingLingGroup/delethon/issues)。

### 构建

当前的windows构建由[pyinstaller脚本](../scripts/pyinstaller_build.bat)制作。

[create_release.py](../scripts/create_release.py)被用于制作发布包。
