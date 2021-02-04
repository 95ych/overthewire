from pwn import *

pass3 ='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'
session = ssh('bandit3', 'bandit.labs.overthewire.org',port=2220, password=pass3)
io = session.process('/bin/bash',env={"PS1":""})
#io.interactive()
io.sendline("cat inhere/.hidden")
io.recvuntil('$ ')
pass3 = io.recvline().decode('utf-8')
print('Completed level 2,\npass for level 3 is', pass3)
io.close()