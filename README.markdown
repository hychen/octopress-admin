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

### create a new blog site

cloned octopress source

	$ octopress-admin new hyblog


### install bundle, do setup of github

setup for deploy to github

note: a user gh_page repository in github link is required

	$ octopress-admin new hyblog

### create a draft post

create a new post and commit in a git branch, every draft post is
mapping to a git branch name starts with a drafts prefix

	$ octopress-admin post 'this is a new post'
	---
	layout: post
	title: ""hello""
	date: 2011-12-04 05:15
	comments: true
	categories:
	---

here is how log look likes

	2011-12-04 Hsin-Yi Chen (hyc~ o [source] enable facebook like
	2011-12-04 Hsin-Yi Chen (hyc~ │ o [drafts/2011-12-04-hiello] start to write hiello
	2011-12-04 Hsin-Yi Chen (hyc~ I─┘ Finished github deploy settings

### list draft posts you have

list posts in drafts/* branchs

	$ octopress-admin drafts
	[1] source/_posts/2011-12-04-hello.markdown (branch: drafts/2011-12-04-hello)

### edit a draft post

checkout to a draft branch and use user favor editor to modify the draft post

	$ octopress-admin edit 1
	---
	layout: post
	title: ""hello""
	date: 2011-12-04 05:15
	comments: true
	categories:
	---

1 is a number as a index of draft branchs, it is recommand to use
`octopress-admin drafts` to know the index of drafts now, because branch index is not always the same.

### publish a draft post

merge a draft post to source and also delete a draft branch which means
the draft post will be include in next blog site building

	$ octopress-admin publish 1

1 is a number as a index of draft branchs

here is the commit log after publish the draft

	2011-12-04 Hsin-Yi Chen (hyc~ M─┐ [source] Merge branch 'drafts/2011-12-04-hello' into source
	2011-12-04 Hsin-Yi Chen (hyc~ │ o start to write hello
	2011-12-04 Hsin-Yi Chen (hyc~ o │ enable facebook like
	2011-12-04 Hsin-Yi Chen (hyc~ o─┘ Finished github deploy settings

### deploy blog

generate contents of blog site and push to github

	$ octopress-admin deploy

### upgrade blog

get lastest octopress source code and install

	$ octopress-admin upgrade

### preview blog

run `rake preview`

	$ octopress-admin preview
