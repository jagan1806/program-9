f=open("C:\\Users\\Administrator s\\Desktop\\demojagan.txt",'r')
print("The filepointer is at byte :",f.tell())
f.seek(10);
print("After reading, the filepointer is at:",f.tell())
