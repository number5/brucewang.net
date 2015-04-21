Title: building ubuntu backports is HARD!
Date: 2007-06-19 19:37
Author: number5
Category: Ubuntu
Tags: backports, php5, Ubuntu
Slug: 47
Status: published
Wordpress-Id: 47
Link: http://brucewang.net/2007/06/19/47

今天因为想在edgy下面用php 5.2, 仔细研究了prevu,
想着有如此详细的指南总不会有问题吧

谁知prevu环境搭起来之后，先是遇到apt-get无法获取feisty的source package,
后来手工从网上wget下来之后，dependency又一直没法满足...

火大，直接去改了apt sources.lst全部指向feisty,
直接升级了apache和php以及相关包
