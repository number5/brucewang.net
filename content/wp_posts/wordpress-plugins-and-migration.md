Title: Wordpress的升级和插件的版本管理
Date: 2007-03-18 20:36
Author: number5
Category: blog
Tags: dokuwiki, plugins, plugin_manager, upgrade, wordpress
Slug: 39
Status: published
Wordpress-Id: 39
Link: http://brucewang.net/2007/03/18/39

[wordpress](http://wordpress.org)的升级还是一件头疼的事, 尤其是�
需要在不同的主机管理多个wordpress的时候。最方便的是[dreamhost](http://www.dreamhost.com)的[one-click
install](http://wiki.dreamhost.com/index.php/KB_/_Account_Control_Panel_/_Goodies_::_One-Click_Installs_/_WordPress_Blog),
基本上从2.0.4到2.1.2都是这么升级过来的，也没出过什么问题。在其他主机或者VPS上的就没那么幸运了，要备份，�
掉原来目录下所有文件，用新的版本解压，再把原来的wp-content目录和wp-config.php复制回来。

接下来这部分就要看看运气了，走运的话[全部插件(plugins)](http://brucewang.net/plugins-used/)和theme都工作,
那就没事了；不走运的话就要开始调，看看不工作的plugins有没有升级，theme有没有更新，如果是自己改动过的也就只能自己修修补补了。

如果wordpress也有像[DokuWiki](http://www.splitbrain.org/projects/dokuwiki)一样的[plugin
manager](http://wiki.splitbrain.org/plugin:plugin_manager)就好了。
这几天看到wordpress.org推出自己的[插件中心](http://wordpress.org/extend/plugins/)了，希望很快会有类似的插件出来吧
