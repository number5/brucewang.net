Title: 让scim支持skype (Archlinux)
Date: 2007-12-08 01:59
Author: number5
Category: Geek
Tags: archlinux, aur, scim, scim-qtimm, skype
Slug: 124
Status: published
Wordpress-Id: 124
Link: http://brucewang.net/2007/12/08/124

**Update**:  不需要scim-qtimm或者scim-bridge也可以支持skype(qt), 
[具体配置见这里](http://brucewang.net/2008/03/04/129)

关键的问题在于编译一个[scim-qtimm](http://www.scim-im.org/projects/scim_qtimm)的模块(Ubuntu上也是用这个方案），似乎很久都没有人维护了，只有cvs版本才支持qt4，
鉴于我的skype 2.0.0.13 beta已经是动态链接到qt4的，所以决定用cvs版本。

好在Archlinux为自己建package提供了非常方便的工具 makepkg/PKGBUILD
系统，在认真了解scons这个python
make工具以及被人遗忘的bksys系统之后，终于让我build成功并安装了。

配置参考[scim官方文档](http://www.scim-im.org/wiki/documentation/installation_and_configuration/all/system_configuration "SCIM Configuration"),
其实也挺简单的，在 \~/.xinitrc里面加上这三行就行  

`export XMODIFIERS=@im=SCIM    #case matters for this variable! export GTK_IM_MODULE=scim export QT_IM_MODULE=scim`

附件是我写的[scim-qtimm-cvs
PKGBUILD](http://brucewang.net/wp-content/uploads/2007/12/pkgbuild "scim-qtimm-cvs PKGBUILD")
