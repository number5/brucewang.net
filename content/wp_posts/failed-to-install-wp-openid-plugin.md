Title: 没办法在Dreamhost上安装Wordpress OpenID插件
Date: 2007-10-25 01:11
Author: number5
Category: blog, openid
Tags: dreamhost, openid, wordpress
Slug: 108
Status: published
Wordpress-Id: 108
Link: http://brucewang.net/2007/10/25/108

已经使用了自己编译的php版本（加入GMP支持), OpenID插件使用的是 [Will
Norris的svn版本](http://willnorris.com/projects/wpopenid/),
但是一直激活不了。 怀疑是Dreamhost上FastCGI的时间限制导致php-cgi被kill.

看起来要换一个地方才行了。
