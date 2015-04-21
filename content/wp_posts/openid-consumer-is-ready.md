Title: OpenID consumer is ready! 
Date: 2007-03-18 21:04
Author: number5
Category: openid
Tags: openid, wordpress
Slug: 41
Status: published
Wordpress-Id: 41
Link: http://brucewang.net/2007/03/18/41

终于在dreamhost的主机上装好了[Wordpress OpenID
plugin](http://blog.verselogic.net/projects/wordpress/wordpress-openid-plugin/),
用的是svn的版本，加上Janrain的[PHP OpenID Library
1.2.1](http://www.openidenabled.com/openid/libraries/php/).

第一次尝试安装是在去年11月份，自己编译了PHP5(DH的PHP默认安装没有GMP或者BCMATH扩展),
采用FastCGI模式，但是怎么也没试成功，也没找到是什么原因，现在看来可能是之前的版本不支持CGI模式。
