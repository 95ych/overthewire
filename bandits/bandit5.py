from pwn import *

password ='koReBOKuIDDepwhWk7jZC0RTdopnAYKh'
session = ssh('bandit5' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.sendline("cd inhere")
io.clean()
io.sendline("find . -size 1033c")
io.recvuntil('$ ')
filename = io.recvline().decode('utf-8')
#print(filename)
io.sendline('cat %s' %filename)
io.recvuntil('$ ')
nextpass = io.recvline().decode('utf-8')
print('Completed level 5,\npass for level 6 is', nextpass)

io.close()