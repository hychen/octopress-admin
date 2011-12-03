#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2011 Hsin Yi Chen
from distutils.core import setup

setup(
    name = 'octopress-admin',
    version = open('VERSION.txt').read().strip(),
    description = 'octopress blog management script',
    long_description="""Octopress is a framework designed by Brandon Mathis for Jekyll, the blog aware static site generator powering Github Pages. This tool provides enhancement of Octopress management such as creat a post as draft, create or upgrad Octopress bog site.
""",
    author = 'Hsin-Yi Chen 陳信屹 (hychen)',
    author_email = 'ossug.hychen@gmail.com',
    url='http://github.com/hychen/octopress-admin',
    license = 'BSD-2-clause License',
    scripts=['bin/octopress-admin'],
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
