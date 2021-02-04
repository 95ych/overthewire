from pwn import *

password ='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR'
session = ssh('bandit9' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("strings data.txt | grep == ")
nextpass = io.recv().decode('utf-8').split()[-1]
print('Completed level 9,\npass for level 10 is', nextpass)
io.close()