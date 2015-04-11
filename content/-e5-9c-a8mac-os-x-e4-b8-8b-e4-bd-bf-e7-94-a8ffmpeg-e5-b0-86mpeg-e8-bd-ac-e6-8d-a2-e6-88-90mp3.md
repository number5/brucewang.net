Title: 在Mac OS X下使用ffmpeg将mpeg转换成mp3
Date: 2008-05-04 22:51
Author: number5
Category: Geek, noteworthy
Tags: ffmpeg, macosx, mp3, mpeg
Slug: 133
Status: published
Wordpress-Id: 133
Link: http://brucewang.net/2008/05/04/133

五一假期期间受LD之命要将几个mpeg文件转换成mp3,
试了一大轮freeware/shareware/open
source软件之后发现[ffmpeg](http://ffmpeg.mplayerhq.hu/)最简单，命令行一行搞定：  
`ffmpeg -i video1.mpeg  video1.mp3`

因为是在Mac OS
X下（LD的MacBook)安装ffmpeg有点麻烦，如果没装[MacPorts](http://www.macports.org/)可以采用先安装[ffmpegX](http://www.versiontracker.com/dyn/moreinfo/macosx/15473)的“曲线救国”方式,
安装完之后可以在`/Applications/ffmpegX.app/Contents/Resources/ffmpeg`找到ffmpeg命令
