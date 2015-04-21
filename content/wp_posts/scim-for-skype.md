Title: scim for skype(或者其他QT程序)的配置方法 (不需要scim-bridge或者scim-qtimm)
Date: 2008-03-04 17:46
Author: number5
Category: archlinux, noteworthy
Tags: linux, qt, scim, skype, 中文输入
Slug: 129
Status: published
Wordpress-Id: 129
Link: http://brucewang.net/2008/03/04/129

装好scim 1.4.7 之后 在 xinitrc中加入下面内容  

` # scim setup export LANG="zh_CN.UTF-8" export XMODIFIERS=@im=SCIM export XIM="scim" export XINPUT="xim" export XIM_PROGRAM="scim -d" export GTK_IM_MODULE=scim export QT_IM_MODULE=scim scim -d &`

我用的是xfce4, xinitrc的位置在 \~/.config/xfce4/xinitrc

**Update**: 我现在已经放弃scim全面转向使用
[ibus](http://code.google.com/p/ibus/ "Intelligent Input Bus for Linux / Unix OS")
/ibus-pinyin了
