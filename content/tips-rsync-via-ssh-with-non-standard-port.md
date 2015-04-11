Title: [tips] Rsync via SSH with non-standard port
Date: 2009-01-03 15:36
Author: number5
Category: Geek
Tags: rsync, snippet, ssh, tips
Slug: 151
Status: published
Wordpress-Id: 151
Link: http://brucewang.net/2009/01/03/151

just noted down here in case I forgot later :P

`rsync -avze "ssh -p 22222 -ax" host1:/SOURCE/DIR  /TARGET/DIR`

Bonus: [Rsync tips and tricks](http://sial.org/howto/rsync/)
