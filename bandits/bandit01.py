from pwn import *

pass1 ='boJ9jbbUNNfktd78OOpsqOltutMc3MY1'
session = ssh('bandit1', 'bandit.labs.overthewire.org',port=2220, password=pass1)
io = session.process('/bin/bash',env={"PS1":""})
io.sendline('cat ./-')
io.recvuntil('$ ')
pass2 = io.recvline().decode('utf-8')
print('Completed level 1,\npass for level 2 is', pass2)
io.close()