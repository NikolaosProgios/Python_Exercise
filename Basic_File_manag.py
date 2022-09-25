#1o

f=open("Text_File.txt")
f.closed
#false
f.close()
f.closed
#true


#2o

g=open('Text_File','w')
g.write('A New file begins')
g.write('...today!\n')
g.colse()


#3o

f=open('Text_File.txt')
for line in f:
   print(line)



#4o
my_list=[i**2 for i in range(1,11)]
f=open("Text_File.txt","w")
for item in my_list:
	f.write(str(item)+"\n")
f.close()



#5o
f=open('Text_File.txt')
for line in f:
   print(line)
  
  
#6
   logfile=open('test.log','w')
   logfile.write('test succeded')
   logfile.close()
   print file('test.log').read()
test succeded
   logfile=open('test.log','a')
   logfile.write('line 2')
   logfile.close()
   print file('test.log').read()
test succededline 2 