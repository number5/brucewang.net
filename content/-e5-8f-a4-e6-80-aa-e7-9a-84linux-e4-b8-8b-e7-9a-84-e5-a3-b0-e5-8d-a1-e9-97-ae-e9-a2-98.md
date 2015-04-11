Title: 古怪的Linux下的声卡问题
Date: 2007-12-13 14:56
Author: number5
Category: archlinux
Tags: alsa, linux, snd_intel8x0, soundcard, t43
Slug: 127
Status: published
Wordpress-Id: 127
Link: http://brucewang.net/2007/12/13/127

系统是 Archlinux, kernel 2.6.23-ARCH  
声卡是 ICH6 T43主板集成的，snd\_intel8x0驱动，禁用了snd\_intel8x0m驱动

经常会在播放音乐中间出错，下面有dmesg的log, 重启之后又没事了  
尝试过开启 snd\_intel8x0的buggy\_irq选项，但是会导致Synaptics
Touchpad的另外一个bug （全部输入无效，看上去和死机一样)

哪位Linux达人教教我怎么解决？

> ` `
>
>     irq 18: nobody cared (try booting with the "irqpoll" option)
>     [] __report_bad_irq+0x24/0x80
>     [] note_interrupt+0x28b/0x2d0
>     [] handle_IRQ_event+0x30/0x60
>     [] handle_fasteoi_irq+0x87/0xe0
>     [] do_IRQ+0x3b/0x70
>     [] do_IRQ+0x40/0x70
>     [] common_interrupt+0x23/0x28
>     [] acpi_pm_read+0x7/0x10
>     [] getnstimeofday+0x34/0xf0
>     [] ktime_get_ts+0x1e/0x60
>     [] ktime_get+0x18/0x40
>     [] tick_nohz_restart_sched_tick+0x2e/0x140
>     [] cpu_idle+0x86/0xe0
>     [] start_kernel+0x30a/0x3a0
>     [] unknown_bootoption+0x0/0x1f0
>     =======================
>     handlers:
>     [] (snd_intel8x0_interrupt+0x0/0x240 [snd_intel8x0])
>     Disabling IRQ #18

**Update**: 换了个zen source的kernel
（[kernel26zen-git](http://aur.archlinux.org/packages.php?do_Details=1&ID=13900))
就解决了
