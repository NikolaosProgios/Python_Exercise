#1.2 Αγορά Προκαταβολή Δόση
#2.7 Python
# -*- coding: utf-8 -*-
R=input("Δώσε ποσο αγοράς")
P=(float(R)*3)/10
print P, "Ποσό προκαταβολής"
T=R-P
print T, "Υπόλοιπο για δόσεις"
K-float(T)/36
print K, "Μηνιαίο ποσό 36 δόσεων"


#3.7 Python
# -*- coding: utf-8 -*-
R=float(input("Δώσε ποσο αγοράς"))
P=(float(R)*3)/10.0
print ( P , "Ποσό προκαταβολής")
T=R-P
print (T , "Υπόλοιπο για δόσεις")
K=float(T)/36
print (K , "Μηνιαίο ποσό 36 δόσεων")


#1.3 Αγορά Πόλη ΦΠΑ
#2,7
# -*- coding: utf-8 -*-
k=input("Για θεσσαλονικη γραψε 1 ή 2 για Σάμο:")
if k==1:
    L=input("Δώσε αρχική τιμή δύσκου")
    Th=L*0.23
    E=Th+L
    print E, " ειναι η τελική τιμή δισκου με 23% ΦΠΑ"
if k==2:
    M=input("Δώσε αρχική τιμή δύσκου")
    S=M*0.16
    E=S+M
    print E, " ειναι η τελική τιμή δισκου με 16% ΦΠΑ"
if k!=1 and k!=2:
    print " Έδωσες λάθος νούμερο"

3,7
# -*- coding: utf-8 -*- 
k=int(input("Για θεσσαλονικη γραψε 1 ή 2 για Σάμο:") )
if k==1: 
    L=float(input("Δώσε αρχική τιμή δύσκου") )
    Th=L*0.23 
    E=Th+L 
    print (E, " ειναι η τελική τιμή δισκου με 23% ΦΠΑ" )
if k==2: 
    M=float(input("Δώσε αρχική τιμή δύσκου") )
    S=M*0.16 
    E=S+M 
    print (E, " ειναι η τελική τιμή δισκου με 16% ΦΠΑ" )
if k!=1 and k!=2: 
    print( " Έδωσες λάθος νούμερο")

#1.4 αθροισμα ψηφιων αριθμού
# -*- coding: utf-8 -*-
L=input("Δωσε 3ψήδιο ακέριο αριθμό")
x=L%10
w=L%100
v=w/10
r=L/100
S=x+v+r
print S, "Έτοιμο"


#1.5 αντιστροφεί ψηφιων αριθμού

# -*- coding: utf-8 -*-
L=input("Δωσε 4ψήδιο ακέριο αριθμό")
x=L%10
w=L/100
v=w%10
r=L/100
k=r%10
j=L/1000
S=(x*1000)+(v*100)+(r*10)+j
print S, "Έτοιμο"


#1.6 Ποσο χωρισμενο σε χαρτινα και κέρματα
# -*- coding: utf-8 -*-
poso=input("Δωσε αριθμό")
u=((poso%100)/10)*10
p=u/10
print p, "ευρο"
x=poso%10
q=x/5
print q, "5ευρα"
w=x-(q*5)
e=w/2
print e, "2ευρά"
t=x-((q*5)+(e*2))
y=t/1
print y, " μονόευρα"

#1.7 αρτιος ζυγος μονος περιττος
# -*- coding: utf-8 -*-
A=input("Δώσε ακέραιο : ")
C=A%10
if C==0 or C==2 or C==4 or C==6 or C==8:
    print "άρτιος"
if C==1 or C==3 or C==5 or C==7 or C==9:
    print "Περιττός"

      A=input("Δώσε ακέραιο : ")
if a%2==0:
   print "ζυγός"
else:
   print "περιττος"

#1.8 δισεκτο ετος
# -*- coding: utf-8 -*-
E=input("Δώσε έτος : ")
if E%400==0:
   print "είναι δισεκτο"
elif E%4==0 and E%100!=0:
    print "δισεκτο"
else :
    print " δεν είναι δίσεκτο"
    
#1.9 Video club κασετες
# -*- coding: utf-8 -*-
N=input("πόσες ταινίες νοίκιασες;")
if  N<=5:
   print N*2
elif 5<N<=15:     #elif  5<N  and N<=15:
   print N*1.5
elif 15<N<=30:    #elif  15<N  and N<=30:
   print N*1.3
elif 30<N:
   print N*1


#1.12 ελεγχος βαθμού μαθητη καλος μετριος

# -*- coding: utf-8 -*-
a=input("μέσος όρος σχολική χρονιά μαθητή : ")
if a<9.5:
    print "απορρίπτεται"
elif 9.5<=a and a<13:
    print "Σχεδόν καλά"
elif 13<=a and a<16:
    print "Καλά"
elif 16<=a and a<18:
    print "Πολύ καλά"
elif 18<=a: #and a<=20:
    print "Άριστα"
#else :
    #print "λαθος αριθμός"


#1.13 ατμ λεγχος

# -*- coding: utf-8 -*-
G=input("διαθέσιμο υπόλοιπο του λογαριασμού  ; ")
B=input("ποσό ανάληψης από ένα ΑΤΜ του ΔΙΑΣ ; ")
C=G-B
K=B*0.01
if 1.0>K:
    K=1 
elif K>3.0:
    K=3
if B>G:
    print "δεν μπορεί να πραγματοποιηθεί η συναλλαγή "
else :
    print  K ," χρέωση πελάτης σύμφωνα με το ΔΙΑΣ ,  " , C-K , " υπόλοιπο του λογαριασμού"


#1.14 εφορια

# -*- coding: utf-8 -*-
O=raw_input("Όνομα Οφειλετή : ")
P=input("Ποσό οφειλής : ")
dosi=input("θες δωσεις ;; πόσες  ")
 
if P<500000:
    pliromi=P-P*0.3
else:
    pliromi=P-P*0.2
if dosi==1:
    pliromi=pliromi-pliromi*0.05
    print "Πληρωμή μετροτής", pliromi, "ευρό"
else:
    poso_dos=pliromi/dosi
    print "το ποσο της δοσεις ειναι " , poso_dos , "ευρώ"
