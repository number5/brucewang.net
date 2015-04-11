Title: How to upgrade U8800 to genokolar's CyanogenMod7 20120107 ROM
Date: 2012-01-14 11:48
Author: number5
Category: Android, blog
Tags: android, clockworkmod, cm7, CyanogenMod, u8800
Slug: 228
Status: published
Wordpress-Id: 228
Link: http://brucewang.net/2012/01/14/228

Now with 20120107 cm7, all good, signal, battery, camera, etc.

Here is what I've done:

\* Download Huawei official 2.3.5 beta1 ROM ([google
U8800V100R001C00B517G001](http://www.google.com/search?q=U8800V100R001C00B517G001))

\* unzip and putting UPDATE.APP in your /sdcard/dload folder (I stupidly
put the whole zip in at the first time... )

\* following the rest of
[instructions](http://forum.xda-developers.com/showpost.php?p=19837995&postcount=31 "instructions")
to upgrade

\* I'm not able to root using SuperOneClick 2.2.3 automatically, so
manually rooted it as per [[TUTORIAL]How to manual root official
2.3](http://forum.xda-developers.com/showpost.php?p=20932026&postcount=1)
(only difference is I'm using zergRush in SuperOneClick)

\* remount cust\_backup read-write and replace recovery.img with
[clockworkmod
5.0.2.7](http://forum.xda-developers.com/showpost.php?p=19281310&postcount=1)

\* power off phone and get into CWM Recovery by VOL+POWER keys

\* normal cm7 upgrade process: wipe data, wipe dalivk cache, install the
zip from
[【rom】u8800pro&u8800-cm7-120107](http://forum.xda-developers.com/showpost.php?p=18585816&postcount=1)

\* reboot and done :)

Thanks genokolar for the ROM and julle131 helping me.
