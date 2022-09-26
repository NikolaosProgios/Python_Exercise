"""
Να γράψετε µια συνάρτηση η οποία θα ελέγχει αν µια
συµβολοσειρά αποτελεί ηλεκτρονική διεύθυνση αλληλογραφίας
ελληνικού ιστότοπου, δηλαδή περιέχει το σύµβολο ‘@’, δεν
περιέχει κενά και έχει κατάληξη ‘.gr’.
"""
# -*- coding: utf-8 -*-
def check(email):
    g=0
    symbol=True
    while symbol!=False:
        y=0
        x=0
        z=0
        n=len(email)
        for i in email:
            if i==' ':
                x+=1
                symbol=False
            if i=='@':
                symbol=True
            else:
                y+=1
        if y<n-1 or x!=0:
                print 'Your email is false'
                symbol=False
        while symbol!=False:
            g=''
            for i in range(n-1,n-4,-1):
                g+=email[i]
            if g=='rg.':
                print "It's ok your email"
                symbol=False
            else:
               print 'Your email is false'
               symbol=False 
email="nikos@gmail.gr"
check(email)