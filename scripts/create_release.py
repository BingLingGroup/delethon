#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines release creation scripts.
"""

# Import built-in modules
import os
import sys
import shlex
import shutil
import subprocess

# Import third-party modules


# Any changes to the path and your own modules


def copytree(src,
             dst,
             symlinks=False,
             ignore=None,
             exts=None,
             is_recursive=False):
    if not exts:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                if is_recursive:
                    shutil.copytree(s, d, symlinks, ignore)
                else:
                    os.makedirs(os.path.join(dst, s))
            else:
                shutil.copy2(s, d)

    else:
        path_stack = [src, ]
        while len(path_stack) > 0:
            path = path_stack.pop()
            if os.path.isdir(path):
                for item in os.listdir(path):
                    abs_path = os.path.join(path, item)
                    if os.path.isdir(item):
                        if is_recursive:
                            path_stack.append(abs_path)
                        else:
                            continue
                    else:
                        path_stack.append(abs_path)
            else:
                rel_path = os.path.relpath(path, src)
                for ext in exts:
                    if path.endswith(ext):
                        dst_path = os.path.join(dst, rel_path)
                        rel_dir = os.path.dirname(dst_path)
                        if not os.path.isdir(rel_dir):
                            os.makedirs(rel_dir)
                        shutil.copy2(path, dst_path)


if __name__ == "__main__":
    release_name = "delethon"
    package_name = release_name

    here = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    os.chdir(here)
    pyinstaller_dist_path = ".build_and_dist/pyinstaller.build"
    dist_path = ".build_and_dist"

    if not os.path.isdir(dist_path):
        os.makedirs(dist_path)

    metadata = {}
    with open(os.path.join(here, package_name, "metadata.py")) as metafile:
        exec(metafile.read(), metadata)

    target = os.path.join(here, ".release", package_name)
    target_nuitka = os.path.join(target, package_name)
    target_data = os.path.join(target_nuitka, "data")
    target_pyi = target + "_pyinstaller"
    target_data_pyi = os.path.join(target_pyi, "data")
    if os.path.isdir(target):
        shutil.rmtree(target)
    os.makedirs(target)
    if os.path.isdir(target_pyi):
        shutil.rmtree(target_pyi)
    os.makedirs(target_pyi)
    # command = "pipreqs --encoding=utf-8 --force --savepath requirements.txt {}".format(package_name)
    # print(command)
    # if sys.platform.startswith('win'):
    #     args = command
    # else:
    #     args = shlex.split(command)
    # p = subprocess.Popen(args,
    #                      stdout=subprocess.PIPE,
    #                      stderr=subprocess.PIPE)
    # out, err = p.communicate()
    # if out:
    #     print(out.decode(sys.stdout.encoding))
    # if err:
    #     print(err.decode(sys.stdout.encoding))
    copytree(src=here, dst=target, exts=[".md", ".txt"])
    target_docs = os.path.join(target, "docs")
    os.makedirs(target_docs)
    copytree(src="docs", dst=target_docs, is_recursive=True)
    shutil.copy2("LICENSE", target)
    copytree(src=target, dst=target_pyi, is_recursive=True)
    shutil.copy2(".build_and_dist/pyinstaller.build/{}.exe".format(release_name), target_pyi)
    copytree(src="scripts/release_files_pyi", dst=target_pyi, is_recursive=True)
    copytree(src="scripts/release_files", dst=target, is_recursive=True)

    os.makedirs(target_data)
    os.makedirs(target_data_pyi)
    copytree(src="{}/data".format(package_name), dst=target_data, exts=[".mo"], is_recursive=True)
    copytree(src="{}/data".format(package_name), dst=target_data_pyi, exts=[".mo"], is_recursive=True)
    copytree(src=".build_and_dist/{}.dist".format(release_name), dst=target_nuitka, is_recursive=True)

    # command = "7z a -sdel \".release/{release_name}-{version}-win-x64-nuitka.7z\" \"{target}\"".format(
    #     release_name=release_name,
    #     version=metadata['VERSION'],
    #     target=target)
    # print(command)
    # if sys.platform.startswith('win'):
    #     args = command
    # else:
    #     args = shlex.split(command)
    # p = subprocess.Popen(args,
    #                      stdout=subprocess.PIPE,
    #                      stderr=subprocess.PIPE)
    # out, err = p.communicate()
    # if out:
    #     print(out.decode(sys.stdout.encoding))
    # if err:
    #     print(err.decode(sys.stdout.encoding))

    command = "7z a -sdel \".release/{release_name}-{version}-win-x64-pyinstaller.7z\" \"{target_pyi}\"".format(
        release_name=release_name,
        version=metadata['VERSION'],
        target_pyi=target_pyi)
    print(command)
    if sys.platform.startswith('win'):
        args = command
    else:
        args = shlex.split(command)
    p = subprocess.Popen(args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    if out:
        print(out.decode(sys.stdout.encoding))
    if err:
        print(err.decode(sys.stdout.encoding))

    command = "python scripts/generate_sha256.py .release"
    print(command)
    if sys.platform.startswith('win'):
        args = command
    else:
        args = shlex.split(command)
    p = subprocess.Popen(args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    if out:
        print(out.decode(sys.stdout.encoding))
    if err:
        print(err.decode(sys.stdout.encoding))
    input("输入任何字符以退出：")
