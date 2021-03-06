#!/usr/bin/env python3
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

metadata = {}

here = os.path.abspath(os.path.dirname(__file__))

NAME = "delethon"

with open(os.path.join(here, NAME, "metadata.py")) as metafile:
    exec(metafile.read(), metadata)

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=metadata['NAME'],
    version=metadata['VERSION'],
    description=metadata['DESCRIPTION'],
    long_description=long_description,
    author=metadata['AUTHOR'],
    author_email=metadata['AUTHOR_EMAIL'],
    url=metadata['HOMEPAGE'],
    packages=['delethon'],
    entry_points={
        'console_scripts': [
            'delethon = delethon:main',
        ]
    },
    package_data={'delethon': ['data/locale/zh_CN/LC_MESSAGES/*mo']},
    install_requires=[
        'pytz>=2019.3',
        'Telethon>=1.11.3',
        'PySocks>=1.7.0',
    ],
    license=open(os.path.join(here, "LICENSE")).read()
)
