from pwn import *

session = ssh('bandit0', 'bandit.labs.overthewire.org',port=2220, password='bandit0')
io = session.process('/bin/bash',env={"PS1":""})
io.sendline('cat readme')
io.recvuntil('$ ')

pass1 = (io.recvline()).decode('utf-8')
print('Completed level 1,\npass for level1 is', str(pass1))
io.close()

# 'Hello, world!\n'