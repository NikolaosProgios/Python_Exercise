# -*- coding: utf-8 -*-
def bedit(lepta):
    if lepta>0 and lepta<=60:
        xreosi=lepta*0.15
    elif lepta>=61 and lepta<=120:
        xreosi=(60*0.15)+(lepta-60)*0,1
    else:
       xreosi=(60*0.15)+(60*0.1)+(lepta-120)*0.05
    return xreosi
customer=[]
minutes=[]
money=[]
onoma=raw_input("Δώσε όναμα πελάτη: ")
while onoma!='x':
    lepta=input('dose lepta omilia:')
    customer.append(onoma)
    minutes.append(lepta)
    xreosi=bedit(lepta)
    money.append(xreosi)
    onoma=raw_input("Δώσε όναμα πελάτη: ")
n=len(customer)
for i in range(1,n,1):
    for j in range(n-1,i-1,-1):
        if money[j]>money[j-1]:
            money[j],money[j-1]=money[j-1],money[j]
            customer[j],customer[j-1]=customer[j-1],customer[j]
            minutes[j],minutes[j-1]=minutes[j-1],minutes[j]
for i in range(5):
    print money[i]
for i in range(n):
    if minutes[i]>200:
        m=open('apot.txt','a')
        money[i]=money[i]-(money[i]*0,05) 
        #(Καλό θα ήταν να μην αλλάξεις την τιμή στη λίστα αλλά να το έβαζες σε άλλη μεταβλητή)
        #m.write(customer[i],money[i]) 
        #Η εντολή write στα αρχεία, δέχεται σαν όρισμα μόνο ένα string!
        #Άρα θα μπορούσες να το κάνεις έτσι:
        #str1 = customers[i] + str(money[i])
        #m.write(str1)
