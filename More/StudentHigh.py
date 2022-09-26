"""
Πρόγραμμα που να διαβάζει τους ύψος και τα επίθετα 15 μαθητων μιας 
τάξης και στην συνέχεια να τα εμφανίζεισε αύξουσα σειρά ως προς το 
ύψος τα επίθετα.
"""

# -*- coding: utf-8 -*-
ipsos=[]
onomata=[]
for i in range(15):
    ip=input("Δώσε ύψος")
    ipsos.append(ip)
    o=raw_input('Δώσε όνομα')
    onomata.append(o)
for i in range(1,15):
    for j in range(14,i-1,-1):
        if ipsos[j]<ipsos[j-1]:
            ipsos[j],ipsos[j-1]=ipsos[j-1],ipsos[j]
            onomata[j],onomata[j-1]=onomata[j-1],onomata[j]
for i in onomata:
    print i
