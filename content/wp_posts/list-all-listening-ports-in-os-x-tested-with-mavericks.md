Title: List all listening ports in OS X (tested with Mavericks)
Date: 2014-04-22 11:54
Author: number5
Category: blog
Tags: command-line, listening, lsof, mavericks, oneliner, osx
Slug: 267
Status: published
Wordpress-Id: 267
Link: http://brucewang.net/2014/04/22/267

`sudo lsof -i4 -P -n |grep LISTEN`
