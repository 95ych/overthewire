from pwn import *

password ='DXjZPULLxYr17uwoI01bNLQbtFemEgo7'
session = ssh('bandit6' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("find / -size 33c -user bandit7 -group bandit6 2>/dev/null")
filename = io.recvline().decode('utf-8')
#print(filename)
io.clean()
io.sendline('cat %s' %filename)
nextpass = io.recvline().decode('utf-8')
print('Completed level 6,\npass for level 7 is', nextpass)
io.close()