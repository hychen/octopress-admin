#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2011 Hsin Yi Chen
from distutils.core import setup

setup(
    name = 'octopress-admin',
    version = open('VERSION.txt').read().strip(),
    description = 'octopress blog management script',
    long_description="""
This library makes you to use command line tool in Python by OO way.
The concept is to transform 1) command as a instance, 2) options
of command as arguments and keyword arguments of function or
instance method when method be used as a sub command of a command.
""",
    author = 'Hsin-Yi Chen 陳信屹 (hychen)',
    author_email = 'ossug.hychen@gmail.com',
    url='http://github.com/hychen/octopress-admin',
    license = 'BSD-2-clause License',
    packages=['octopress-admin'],
    classifiers = [
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: BSD License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 2.5",
      "Programming Language :: Python :: 2.6",
      "Programming Language :: Python :: 2.7",
    ]
)
