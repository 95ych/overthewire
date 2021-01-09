from pwn import *

password ='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'
session = ssh('bandit12' ,'bandit.labs.overthewire.org' ,port=2220 ,password=password)
io = session.process('/bin/bash',env={'PS1':""})
io.interactive()
io.clean()
io.sendline("cat data.txt | tr 'A-Za-z' 'N-ZA-Ma-za-m'")
nextpass = io.recv().decode('utf-8').split()[-1]
print('Completed level 12,\npass for level 13 is', nextpass)
io.close()