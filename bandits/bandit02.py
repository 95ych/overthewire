from pwn import *

pass2 ='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'
session = ssh('bandit2', 'bandit.labs.overthewire.org',port=2220, password=pass2)
io = session.process('/bin/bash',env={"PS1":""})
#io.interactive()
io.sendline("cat 'spaces in this filename'")
io.recvuntil('$ ')
pass3 = io.recvline().decode('utf-8')
print('Completed level 2,\npass for level 3 is', pass3)
io.close()