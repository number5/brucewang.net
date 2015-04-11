Title: Install gitweb using Nginx fastcgi
Date: 2008-10-22 12:56
Author: number5
Category: blog
Tags: fastcgi, git, gitserve, gitweb, nginx
Slug: 147
Status: published
Wordpress-Id: 147
Link: http://brucewang.net/2008/10/22/147

[gitweb](http://git.or.cz/gitwiki/Gitweb) 是cgi,
[Nginx](http://wiki.codemongers.com/Main "powerful lightweight httpd server")
只支持FastCGI, 所以需要加个wrapper

下面是网上搜回来的资料，放在这里备忘：

[Slicehost Forum - Nginx +
SCM](http://forum.slicehost.com/comments.php?DiscussionID=1144)  
[cactuswax.net gitweb helper scripts  
](http://code.cactuswax.net/git/?p=gitweb.git)[NginxSimpleCGI](http://wiki.codemongers.com/NginxSimpleCGI)

等晚上做好了再回来报告  
------------------------  
装好了，很顺利  
不过后来发现有个 [gitserve](http://pypi.python.org/pypi/gitserve/0.2.0)
更简单，用python 做的http server
包在gitweb.cgi外面，用起来感觉和`hg serve`一样方便了 :)
