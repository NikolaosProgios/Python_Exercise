"""
Πρόγραμμα που να διαβάζει τους βαθμούς και τα επίθετα 15 μαθητών μιας τάξης 
και στην συνέχεια να τα εμφανίζει σε φθίνουσα σειρά ως προς τους βαθμούς τα ονόματα.
 Εαν κατα την διάρκεια της ταξινόμησης κάποιοι μαθητές έχουν ίδιο βαθμό να ταξινομείτε αλφαβητικά.
"""
# -*- coding: utf-8 -*-
bath=[]
onomata=[]
for i in range(15):
    b=input("Δώσε βαθμό")
    bath.append(b)
    o=raw_input('Δώσε όνομα')
    onomata.append(o)
for i in range(1,15):
    for j in range(14,i-1,-1):
        if bath[j]>bath[j-1]:
            bath[j],bath[j-1]=bath[j-1], bath[j]
            onomata[j],onomata[j-1]=onomata[j-1],onomata[j]
        elif bath[j]==bath[j-1]:
            if onomata[j]<onomata[j-1]:
                onomata[j],onomata[j-1]=onomata[j-1],onomata[j]
for i in onomata:
    print i
