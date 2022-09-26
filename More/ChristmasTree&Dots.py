# Dots

# -*- coding: utf-8 -*-
simbol='*'
numb=0
counter=0
for i in range(1,10):
    if counter==5:
        numb=numb-1
        print numb*simbol
    else:
        print i*simbol
        numb=numb+1
        counter=counter+1

#OR

for i in range(5):
    print i* '*'
for i in range(4,0,-1):
    print i * '*'

#Christmas Tree

# -*- coding: utf-8 -*-
simbol='*'
space=' '
numb=1
N=input('δωσε αστερουδια')
for i in range(N,0,-1):
    print i*space+(numb*simbol)
    numb+=2
mok=N-2
for j in range(3):
    print (mok*space) , "***" 

