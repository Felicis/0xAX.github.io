Title: Kindle and Read-only file system
Date: 2013-12-01
Tags: linux, amazon kindle
Authors:  Alexander Kuleshov


Some times ago i moved on 64 bit system and my first problem with new system was situation when i couldn't copy any files to my Amazon Kindle 5. Every time when i tried to delete some file from Kindle i got following error:

```
[Errno 30] Read-only file system
```

Here is the solution how to fix it: First of all you need to determine your device. Execute `mount` command for you device and you must have something like this:

```
$ mount

/dev/sdc1 on /media/alex/Kindle type vfat \
(rw, nosuid, nodev, uid=1000, gid=1000,   \
shortname=mixed, dmask=0077, utf8=1,      \
showexec,flush,uhelper=udisks2)
```

After that you mounted your device, just execute:

```
sudo fsck.vfat -r /dev/sdc1
```

Unmount and remove and plug again the USB cable of your Kindle device, and after this simple manipulations you'll  be able to copy any files to your `Kindle`.
