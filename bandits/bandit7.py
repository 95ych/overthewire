from pwn import *

password ='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs'
session = ssh('bandit7' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
#io.interactive()
io.clean()
io.sendline("cat data.txt | grep millionth")
nextpass = io.recvline().decode('utf-8').split()[1]
print('Completed level 7,\npass for level 8 is', nextpass)
io.close()