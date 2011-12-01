#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2011 Hsin Yi Chen
from distutils.core import setup

setup(
    name = 'octopress-admin',
    version = open('VERSION.txt').read().strip(),
    description = 'Octopress blog management script',
    long_description="""This is a unofficial tool for Octopress
    which is a static blog framwork based on Ruby language,
    this tool help user to manage multiple blog site and introduce draft
    system of post (by using git branch).
""",
    author = 'Hsin-Yi Chen 陳信屹 (hychen)',
    author_email = 'ossug.hychen@gmail.com',
    url='http://github.com/hychen/octopress-admin',
    license = 'BSD-2-clause License',
    scripts=['bin/octopress-admin']
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
