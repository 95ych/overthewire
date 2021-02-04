from pwn import *

password ='pIwrPrtPN36QITSp3EQaw936yaFoFgAB'
session = ssh('bandit4' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})

io.sendline("cd inhere")
io.clean()
io.sendline("file ./* | grep ASCII")
io.recvuntil('$ ')
filename = io.recvline().decode('utf-8').split(':')[0]
io.sendline('cat %s' %filename)
io.recvuntil('$ ')
nextpass = io.recvline().decode('utf-8')
#print(filename)
print('Completed level 4,\npass for level 5 is', nextpass)

io.close()