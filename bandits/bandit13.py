from pwn import *

password ='8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL'
session = ssh('bandit13' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("ssh -i sshkey.private bandit14@localhost")
io.recv()
io.sendline("yes")
io.recv()
io.sendline("cat /etc/bandit_pass/bandit14")
#io.interactive()
io.recvuntil('$ ')
nextpass = io.recv().decode('utf-8')
#io.interactive()
io.clean()
io.sendline("cat /etc/bandit_pass/bandit14 | nc localhost 30000")
nextnextpass = io.recv().decode('utf-8').split('\n')[1]
print('Completed level 13,\npass for level 14 is', nextpass)
print('\nCompleted level 14,\npass for level 15 is', nextnextpass)
io.close()