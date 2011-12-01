hychen's octopress admin script

# Requirement

- python (>=2.5)
- git
- sensible-editor
- python modules:
	- [UCLTIP](pypi.python.org/pypi/ucltip)

# Installation

## get source

	user@host:~$ apt-get install git
	user@host:~$ git clone http://github.com/hychen/octopress-admin

## install script

	user@host:~$ cd octopress-admin
	user@host:octopress-admin$ python setup.py install

or just create a link

	user@host:octopress-admin$ ln -s ~/bin/blog $PWD/octopress-admin/bin/octopress-admin

*notice*: if you want to use command located in ~/bin, you need to add ~/bin to PATH variable, like this

	PATH=~/bin:$PATH

# USAGE

	usage: blog [-h]

	            {deploy,drafts,edit,new,page,post,preview,publish,update_octopress,upgrade}
	            ...

	optional arguments:
	  -h, --help            show this help message and exit

	subcommands:
	  {deploy,drafts,edit,new,page,post,preview,publish,update_octopress,upgrade}
	                        additional help
	    deploy              deploy content to remote server
	    drafts              list draft posts
	    edit                edit draft post
	    new                 create a new blog site
	    page                create a new page
	    post                create a new post
	    preview             start a server to preview blog
	    publish             let draft post is avaliable to publish
	    update_octopress    update octopress source
	    upgrade             upgrade blog