#!/usr/bin/env python
from setuptools import setup, find_packages
import re
import os


def get_long_description():
    readme = open('README.rst').read()
    changelog = open('CHANGES.rst').read()
    return "\n\n".join([
        readme,
        changelog.replace(':func:', '').replace(':ref:', '')
    ])


setup(
    name='rentier-scrapy-advanced-rotating-proxies',
    version='0.6.2',
    author='Michal Hodur, Mikhail Korobov',
    author_email='mhodur@protonmail.com, kmike84@gmail.com',
    license='MIT license',
    long_description=get_long_description(),
    description="Advanced Rotating Proxies for Scrapy",
    url='https://github.com/TeamHG-Memex/scrapy-rotating-proxies',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'attrs > 16.0.0',
        'six',
        'typing',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
