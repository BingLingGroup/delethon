#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import built-in modules
import os
import sys
import subprocess

name = "delethon"


def run_cmd(cmd):
    print(cmd)
    cmd_prcs = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    while True:
        line_ = cmd_prcs.stdout.readline()
        if not line_:
            break
        print(line_)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        locale_name = sys.argv[1]
    else:
        locale_name = "zh_CN"

    os.chdir(os.pardir)

    locale_dir = "{name}/data/locale/{ln}/LC_MESSAGES/".format(
        name=name,
        ln=locale_name)
    if not os.path.exists(locale_dir):
        os.makedirs(locale_dir)

    locale_codes = []

    for item in os.listdir(name):
        filename = os.path.splitext(item)
        if filename[-1] == ".py":
            locale_codes.append(filename[0])

    for python_code in locale_codes:
        code = "{name}/{py}.py".format(
            name=name,
            py=python_code)

        if python_code != "__init__":
            old_po = "{ld}{name}.{py}.po".format(
                ld=locale_dir,
                name=name,
                py=python_code)
            new_mo = "{ld}{name}.{py}.mo".format(
                ld=locale_dir,
                name=name,
                py=python_code)
            if os.path.exists(old_po):
                new_po = "{ld}{name}.{py}.new.po".format(
                    ld=locale_dir,
                    name=name,
                    py=python_code)
                new_po_name = "{name}.{py}.new".format(
                    name=name,
                    py=python_code)
                xgt_cmd = "xgettext \"{code}\" -L Python -d \"{new_po_name}\" -p \"{ld}\"".format(
                    code=code,
                    new_po_name=new_po_name,
                    ld=locale_dir)
                msgmerge_cmd = "msgmerge \"{old_po}\" \"{new_po}\" -U".format(
                    old_po=old_po,
                    new_po=new_po
                )
                run_cmd(xgt_cmd)
                run_cmd(msgmerge_cmd)
                os.remove(new_po)

            else:
                old_po = "{name}.{py}".format(
                    name=name,
                    py=python_code)
                xgt_cmd = "xgettext \"{code}\" -L Python -d \"{old_po}\" -p \"{ld}\"".format(
                    code=code,
                    old_po=old_po,
                    ld=locale_dir)
                run_cmd(xgt_cmd)

        else:
            old_po = "{ld}{name}.po".format(
                ld=locale_dir,
                name=name)

            new_mo = "{ld}{name}.mo".format(
                ld=locale_dir,
                name=name)

            if os.path.exists(old_po):
                new_po = "{ld}{name}.new.po".format(
                    ld=locale_dir,
                    name=name)
                new_po_name = "{name}.new".format(
                    name=name)
                xgt_cmd = "xgettext \"{code}\" -L Python -d \"{new_po_name}\" -p \"{ld}\"".format(
                    code=code,
                    new_po_name=new_po_name,
                    ld=locale_dir)
                msgmerge_cmd = "msgmerge \"{old_po}\" \"{new_po}\" -U".format(
                    old_po=old_po,
                    new_po=new_po
                )
                run_cmd(xgt_cmd)
                run_cmd(msgmerge_cmd)
                os.remove(new_po)

            else:
                old_po = "{name}".format(
                     name=name)
                xgt_cmd = "xgettext \"{code}\" -L Python -d \"{old_po}\" -p \"{ld}\"".format(
                    code=code,
                    old_po=old_po,
                    ld=locale_dir)
                run_cmd(xgt_cmd)

        msgfmt_cmd = "msgfmt \"{old_po}\" -o \"{new_mo}\"".format(
            old_po=old_po,
            new_mo=new_mo
        )
        run_cmd(msgfmt_cmd)
