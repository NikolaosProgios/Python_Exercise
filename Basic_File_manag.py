#1o
my_list=[i**2 for i in range(1,11)]
f=open("outpuut.txt","w")
for item in my_list:
	f.write(str(item)+"\n")

	
f.close()

#2o
f=open("new_file.txt")
f.closed
#false
f.close()
f.closed
#true

#3o

g=open('new_file','w')
g.write('A New file begins')
g.write('...today!\n')
g.colse()

#4o
f=open('input_file.txt')
for line in f:
   print(line)