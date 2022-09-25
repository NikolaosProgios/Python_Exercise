"""
18.	Να κάνετε πρόγραμμα που θα δέχεται ένα αρχείο το οποίο θα περιέχει μία πρόταση. 
Αυτό σημαίνει ότι το αρχείο μας τελειώνει όταν διαβάσουμε το χαρακτήρα της τελείας. 
Κάθε λέξη χωρίζεται με την επόμενη με το κενό. Θα πρέπει να δημιουργήσετε μία λίστα που 
να περιέχει όλες τις λέξεις της πρότασης. Αν μία λέξη υπάρχει στο κείμενο παραπάνω από 
μία φορά να μην τη βάζετε ξανά στη λίστα. Για παράδειγμα αν σας δοθεί η πρόταση 
«A computer network or data network is a telecommunications network which allows nodes to share resources.»
τότε η λίστα σας πρέπει να είναι ως εξής:
[A,computer,network,or,data,is,a,telecommunications,which,allows,nodes,to,share,resources]
"""

# -*- coding: utf-8 -*-
def makis(lista,i):
    lista.pop(i)   
text=open('kalispera.txt')
leksi=''
lista=[]
l=text.read(1)
while l!='.':
    if l==' ':
        l=text.read(1)
        lista.append(leksi)
        leksi=''
    else:
        leksi+=l
        l=text.read(1)
        if l=='.':
          lista.append(leksi)      
for item in range(len(lista)-1,0,-1):
    pl=0
    for i in lista:
        if i==lista[item]:
            pl+=1
    if pl>1:
        makis(lista,item)
print lista
