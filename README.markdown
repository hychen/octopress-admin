hychen's octopress admin script

# Requirement

- python (>=2.5)
- git
- sensible-editor
- python modules:
	- [UCLTIP](pypi.python.org/pypi/ucltip)

# Installation

## install dependecy for Ubuntu/Debian users

	user@host:~$ apt-get install git
	user@host:~$ apt-get install python-ucltip

## get source

	user@host:~$ git clone http://github.com/hychen/octopress-admin

## install script

	user@host:~$ cd octopress-admin
	user@host:octopress-admin$ python setup.py install

or just create a link

	user@host:octopress-admin$ ln -s ~/bin/blog $PWD/octopress-admin/bin/octopress-admin

*notice*: if you want to use command located in ~/bin, you need to add ~/bin to PATH variable, like this

	PATH=~/bin:$PATH

## How to use it

before using this tool, please setup your ruby enviroment for octopress

### create a new blog

cloned octopress source, setup for deploy to github

note: a user gh_page repository in github link is required

	$ octopress-admin new hyblog

### create a draft post

create a new post and commit in a git branch, every draft post is
mapping to a git branch name starts with a drafts prefix

	$ octopress-admin post 'this is a new post'

### list draft posts you have

list posts in drafts/* branchs

	$ octopress-admin drafts

### edit a draft post

checkout to a draft branch and use user favor editor to modify the draft post

	$ octopress-admin edit 1

1 is a number as a index of draft branchs

### publish a draft post

merge a draft post to source and also delete a draft branch which means
the draft post will be include in next blog site building

	$ octopress-admin publish 1

1 is a number as a index of draft branchs

### deploy blog

generate contents of blog site and push to github

	$ octopress-admin deploy

### upgrade blog

get lastest octopress source code and install

	$ octopress-admin upgrade

### preview blog

run `rake preview`

	$ octopress-admin preview
