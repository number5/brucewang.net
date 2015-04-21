Title: 获取Twitter Replies的简易方法
Date: 2008-06-26 16:22
Author: number5
Category: blog, Geek, Internet
Tags: code, python, twitter
Slug: 137
Status: published
Wordpress-Id: 137
Link: http://brucewang.net/2008/06/26/137

近日twitter 看replies功能不能用，但是twitter api还是好的，
所以试着用python-twitter来看replies, 效果不错,
不知道python是什么的同学请忽略此帖

首先安装[python-twitter](http://code.google.com/p/python-twitter/),
最方便的做法可能是用easy\_install  
` easy_install python-twitter`  
下面是代码

``` {.python name="code"}
import twitter
def getTwitterReplies():
     api = twitter.Api(username='twitter用户名', password='twitter密码')
     replies = api.GetReplies()
     replies.reverse()
     for item in replies:
          print item.user.screen_name, ': ', item.text
```

我是放在[ipython](http://ipython.scipy.org/)当中，直接输函数名就可以看到结果了
