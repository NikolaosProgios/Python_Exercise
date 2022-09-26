"""
Σε αγώνα στοιβου 20 μαθητες παίζουν .Περνάει όποιος μαθητης πετύχει πανω απο 4,5 μετρα . 
Ο καθενας δικαιούτε 3 προσπάθειες. Να εφανίζει την καλύτερη αποδοσει με το ονομα του  
και πόσα άτομα πέρασαν.
"""
# -*- coding: utf-8 -*-
epidosei=[]
onomata=[]
for i in range(3):
    onoma=raw_input('doseonoma')
    onomata.append(onoma)
    almaa=float(input('dvse almaa'))
    almab=float(input('dvse almab'))
    almac=float(input('dvse almac'))
    bestalma=0
    if almaa>almab:
        if almaa>almac:
            bestalma=almaa
        else:
            bestalma=almac
    elif almab>almaa:
        if almab>almac:
            bestalma=almab
        else:
            bestalma=almac
    else:
        bestalma=almac
    epidosei.append(bestalma)
meg=epidosei[0]
thesi=0
for i in range(len(epidosei)):
    if epidosei[i]>meg:
        meg=epidosei[i]
        thesi=i
print meg , onomata[thesi]
counter=0
for i in epidosei:
    if i>4.5:
        counter+=1
print counter