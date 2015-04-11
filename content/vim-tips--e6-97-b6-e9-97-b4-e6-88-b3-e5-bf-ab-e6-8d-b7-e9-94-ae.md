Title: Vim tips: 时间戳快捷键
Date: 2006-12-31 14:47
Author: admin
Category: Geek
Tags: shortcut, tips, vim
Slug: 25
Status: published
Wordpress-Id: 25
Link: http://brucewang.net/2006/12/31/25

`:map <f2> a<c-r>=strftime("%c")</c-r></f2>`

  
在非编辑模式下，按F2就会在光标位置插入一个当天时间的时间戳  
  
  
去掉前面的冒号, 加入到.vimrc, 以后用vim的时候就都有这个快捷键了  

