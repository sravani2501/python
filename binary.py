f2=open('stud_binary.txt','wb')
sent=(b"Hi Sravani,Your Binary File written Congratulations")
f2.write(sent)
print('Binary File Created')
f2.close()
import os
file=open('stud_binary.txt','rb')
print(file.read(10))
file.seek(0,os.SEEK_END)
file.seek(-10,1)
print(file.read(5))
file.seek(0) 
print(file.read(25))
file.close()