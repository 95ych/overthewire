from pwn import *

password ='cvX2JJa4CFALtqS87jk27qwqGhBM9plV'
session = ssh('bandit8' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("cat data.txt | sort | uniq -u")
nextpass = io.recvline().decode('utf-8')
print('Completed level 8,\npass for level 9 is', nextpass)
io.close()