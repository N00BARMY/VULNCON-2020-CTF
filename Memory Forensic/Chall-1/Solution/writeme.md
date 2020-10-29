Given a memory dump file from dump.rar, named dump.raw. Now we need to find the profile for the volatility to go for further enumeration

Note I used volatility 2.6 that comes pre-installed with kali-linux 2019.4

Command: volatility -f dump.raw imageinfo

This will suggest some profiles

```
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/devil/Desktop/volatility/vulncon/vulncon/dump.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002bf20a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002bf3d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-12-12 14:05:05 UTC+0000
     Image local date and time : 2020-12-12 19:35:05 +0530

```

We can see it is Win7SP1x64. Since the user DEVINER visited some websites, all the logs were saved in chromehistory. TO see the history, there are plugins available for volatility to make stuffs easy.

Link of Plugins: https://github.com/superponible/volatility-plugins

Commands Used: volatility --plugins=./volatility-plugins/ -f dump.raw --profile=Win7SP1x64 chromehistory

Flag: vulncon{gamblingsites.org-12-12-2020}