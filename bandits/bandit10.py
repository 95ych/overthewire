from pwn import *

password ='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk'
session = ssh('bandit10' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("cat data.txt | base64 -d")
nextpass = io.recv().decode('utf-8').split()[-1]
print('Completed level 10,\npass for level 11 is', nextpass)
io.close()