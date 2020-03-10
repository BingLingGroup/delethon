#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import os
import sys

text = '''| 文件名 | SHA256 |
| :- | :- |'''


def checksum(filename):
    algorithm = hashlib.sha256()
    with open(filename, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            algorithm.update(byte_block)
    return str(algorithm.hexdigest())


def filelist(path):
    r = []
    n = os.listdir(path)
    for f in n:
        if not os.path.isdir(f):
            r.append(f)
    return r


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(text)
        for item in os.listdir(sys.argv[1]):
            file_name = os.path.join(sys.argv[1], item)
            if os.path.isfile(file_name):
                print('| {0} | {1} |'.format(item, checksum(file_name)))
