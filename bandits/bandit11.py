from pwn import *

password ='IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR'
session = ssh('bandit11' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
nextpass = io.recv().decode('utf-8').split()[-1]
print('Completed level 11,\npass for level 12 is', nextpass)
io.close()