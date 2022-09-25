# -*- coding: utf-8 -*-
a=input("Δώσε α")
b=input("Δώσε β")
g=input("Δώσε γ")

#a*x**2+b*x+g=0  Εξίσωση δευτέρου βαθμού
D=b**2-4*a*g
print D,"είναι το Δ"
import math
if D>0:
    x1=((-1*b)+math.sqrt(D))/(2*a)
    print x1,("είναι η πρώτη ρίζα")
    x2=((-1*b)-math.sqrt(D))/(2*a)
    print x2,("είναι η δεύτερη ρίζα")
elif D==0:
    x=(-1*b)/float(2*a)
    print x,"είναι η διπλή ρίζα"
else:
    print "Δεν υπάρχουν ρίζες, Αδύνατη"
