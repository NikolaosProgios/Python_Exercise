"""
Η κλίµακα Τορίνο είναι µία κλίµακα επικινδυνότητας πιθανής
πρόσπτωσης ή σύγκρουσης ουρανίου σώµατος µε τον πλανήτη
Γη. Η Κλίµακα Τορίνο φέρει δέκα διαβαθµίσεις σε ακέραιους
αριθµούς αρχής γενοµένης από το 0, ως κατάσταση ανύπαρκτου
κινδύνου ή αµελητέου, καταλήγοντας στο 10 ως κατάσταση
τελείας καταστροφής του ανθρώπινου πολιτισµού. Οι διαβαθµίσεις
αυτές κατανέµονται στις παρακάτω βασικές ζώνες: 


Χρώµα        Κλίµακα       Επικινδυνότητα
Λευκό          0             Κανένας Κίνδυνος
Πράσινο        1             Σύνηθες Επίπεδο
Κίτρινο      2 – 4           Αστρονοµικού Ενδιαφέροντος
Πορτοκαλί    5 – 7           Εν ∆υνάµει Απειλή
Κόκκινο      8 – 10          Βέβαιη Σύγκρουση
Να γράψετε ένα πρόγραµµα σε Python το οποίο για κάθε ένα από
30 ουράνια σώµατα θα: 
Γ1. διαβάζει τον αριθµό επικινδυνότητας

Γ2. εµφανίζει τη ζώνη επικινδυνότητας του ουράνιου σώµατος και
το αντίστοιχο χρώµα

Γ3. εµφανίζει το πλήθος των ουρανίων σωµάτων που δεν
αποτελούν κανέναν κίνδυνο

Γ4. εµφανίζει το µήνυµα “Κίνδυνος σύγκρουσης”, αν υπάρχει έστω
και ένα ουράνιο σώµα που βρίσκεται στην υψηλότερη κατηγορία
επικινδυνότητας. 
"""

# -*- coding: utf-8 -*-
name=[]
grade=[]
city=[]
athr=0
plithos=0
onom=raw_input('δωσε ονομα')
while onom!='T':
    name.append(onom)
    bath=input("δωσε ")
    grade.append(bath)
    poli=raw_input('δωσε')
    city.append(poli)
    if poli=='ioannina' :
        athr+=bath
        plithos+=1
    onom=raw_input(" δώσε όνομα")
if plithos!=0:
    MO=float(athr)/plithos   #δεν παμε στην μεταβλητη πληθος να βαλουμε 0.0 γιατι ποιανει ποιο πολυ χορο στο pc
    print MO
else:
    MO=-1
if MO==1:
    print"δεν υπαρχουν γιαννοτες"
else:
    for i in range(len(grade)):
        if grade[i]>MO:
            print name[i]