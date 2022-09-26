"""
Nα γραφεί πρόγραμμα που θα διαβάζει μια λίστα 50 αριθμών και στη συνέχεια 
θα υπολογίζει και θα εμφανίζει :  α) το άθροισμα των στοιχείων της, 
β) το πλήθος των μη μηδενικών του στοιχείων και γ) το ποσοστό των μηδενικών της στοιχείων.
"""
# -*- coding: utf-8 -*-
pl=[]
pl_arth=0
b=0
m=0
for i in range(50):
    a=input("Δωσε αριθμο")
    pl.append(a)
for i in range(50):
    pl_arth=pl_arth+pl[i]
    if pl[i]!=0:
        b=b+1
    else:
        m=m+1
pos_mid=(m/50.0)*100
print pl_arth, "το άθροισμα των στοιχείων της"
print b , "το πλήθος των μη μηδενικών του στοιχείων"
print pos_mid , "το ποσοστό των μηδενικών"

"""
2.	Να γραφεί πρόγραμμα που θα διαβάζει τις ηλικίες 30 μαθητών σε λίστα. 
Να εμφανιστεί η μικρότερη και η μεγαλύτερη ηλικία. Επίσης να υπολογιστεί 
και να εμφανιστεί ο αριθμός των μαθητών που έχουν τη μικρότερη ηλικία.
"""
# -*- coding: utf-8 -*-
math=[]
meg=0
for i in range(30):
    m=input("Δωσε ηλικία")
    math.append(m)
mik=math[0]
meg=math[0]
math_mik_age=0
for i in range(30):
    if math[i]<mik:
	    mik=math[i]
    if math[i]>meg:
	    meg=math[i]
for i in range(50):
    if math[i]==mik:
	    math_mik_age=math_mik_age+1
print mik , " μικροτερη ηλικια"
print meg, " μεγαλυτερη  ηλικια"
print math_mik_age , " μαθητες με ην μικροτερη ηλικια"




"""
3.	Δίνονται η έκταση, ο πληθυσμός και το όνομα καθεμιάς από τις 
15 χώρες της Ευρωπαϊκής Ένωσης. Να αναπτύξετε πρόγραμμα που 
α) θα διαβάζει τα παραπάνω δεδομένα σε 3 λίστες, 
β) θα εμφανίζει τη χώρα με τη μεγαλύτερη έκταση
γ) θα εμφανίζει τη χώρα με το μικρότερο πληθυσμό  και 
δ) θα εμφανίζει το μέσο όρο του πληθυσμού των 15 χωρών της Ευρωπαϊκής Ένωσης.
"""
# -*- coding: utf-8 -*-
ektasi=[]
plithismo=[]
xores=[]
for i in range(15):
            ek=input("δωσε εκταση")
	ektasi.append(ek)
	p=input("δωσε πληθος")
	plithismo.append(p)
	ono=input("δωσε όνομα")
	xores.append(ono)
meg_ek=ektasi[0]
meg_ek_xora=xores[0]
mik_pl=plithismo[0]
mik_pl_xora=xores[0]
pl_xoron=0
for i in range(15):
    if ektasi[i]>meg_ek:
        meg_ek=ektasi[i]
        meg_ek_xora=xores[i]
    if plithismo[i]<mik_pl:
        mik_pl=ektasi[i]
        mik_pl_xora=xores[i]
    pl_xoron=pl_xoron+plithismo[i]
mesos_oros_pl_xoron = pl_xoron/15.0
print meg_ek , "χώρα με τη μεγαλύτερη έκταση"
print mik_pl ,  "χώρα με το μικρότερο πληθυσμό"
print mesos_oros_pl_xoron , "ο μέσο όρο του πληθυσμού των 15 χωρών της Ευρωπαϊκής Ένωσης"


"""
1.	Να γραφεί πρόγραμμα που θα διαβάζει μια λίστα 100 ακέραιων αριθμών και θα εμφανίζει : 
α) το πλήθος των θετικών αριθμών της λίστας,
β) το άθροισμα των αριθμών της λίστας που βρίσκονται στο εύρος από -10 έως και 10
γ) τον μέσο όρο των αρνητικών αριθμών 
δ) το ποσοστό των αρνητικών αριθμών 
"""
# -*- coding: utf-8 -*-
lista=[]
for i in range(100):
    a=int(input(“δωσε ακαιρεο”))
    lista.append(a)
pl_thet=0.0
athrisma=0.0
m_arnitikon=0.0
pos_arnitikon=0.0
z=0
for i in range(100):
    if lista[i]>0:
        pl_thet=pl_thet+1
    if lista[i]>=-10 and lista[i]<=10:
       athrisma=athrisma+lista[i]
    if  lista[i]<0:
        m_arnitikon=m_arnitikon+lista[i]
       z=z+1
pos_arnitikon= (m_arnitikon/100)*100

print pos_arnitikon , “το ποσοστό των αρνητικών αριθμών“       
mesos_arnitikon= m_arnitikon/z
print  pl_thet , “ο πλήθος των θετικών αριθμών της λίστας,”
print athrisma , “   το άθροισμα των αριθμών της λίστας που βρίσκονται στο εύρος από -10 έως και 10”
print mesos_arnitikon ,  “ τον μέσο όρο των αρνητικών αριθμών“


"""
2.	Να γραφεί πρόγραμμα που : 
α) θα διαβάζει μια θερμοκρασία για κάθε μια ημέρα του μήνα Ιουνίου 
και θα τις αποθηκεύει σε μια λίστα,
β) θα υπολογίζει και θα εμφανίζει την μέση θερμοκρασία του μήνα Ιουνίου,
γ) θα εμφανίζει τις ημέρες του μήνα που η θερμοκρασία του μήνα ξεπέρασε 
τον μέσο όρο του μήνα κατά 2 βαθμούς 
"""
# -*- coding: utf-8 -*-
therm=[]
meres=[]
for i in range(1,31):
    ther=input('')
    therm.append(ther)
    meres.append(i)
x=0
for i in therm:
    x+=i
xx=x/30
print xx
for i in range(30):
    if therm[i]>xx+2:
        print meres[i] " μερα πουη θερμ. ξεπέρασε τον μέσο όρο του μήνα κατά 2 βαθμούς"

"""
3.	Σε μια εταιρεία απασχολούνται 120 εργαζόμενοι. Να γραφεί πρόγραμμα που : 
α) για κάθε ένα εργαζόμενο να διαβάζει το όνομα του και τις μηνιαίες αποδοχές 
του καθενός και να τα αποθηκεύει σε λίστες εξασφαλίζοντας ότι ο μισθός είναι θετικός αριθμός
β) θα εμφανίζει τα ονόματα των εργαζομένων με μηνιαίες αποδοχές από 1000 μέχρι 1200€ 
"""
# -*- coding: utf-8 -*-
onomata=[]
lefta=[]
for i in range(120):
    o=raw_input(“δώσε ονομα”)
    onomata.append(ο)
    marouli=input(“δωσε μηνιαία αποδοχη ”)
    if marouli>0:
        lefta.append(marouli)
for i in range(120):
    if lefta[i] >=1000 and lefta[i]<1200:
        print onomata[i] , “ονόματα των εργαζομένων με μηνιαίες αποδοχές από 1000 μέχρι 1200€ “ 

"""
4.	Να γίνει πρόγραμμα που θα διαβάζει τα ονόματα και τις εισπράξεις 
10 καταστημάτων στη διάρκεια του έτους και θα τα αποθηκεύει σε αντίστοιχες λίστες. 
Το πρόγραμμα θα υπολογίζει και θα εμφανίζει :
α. τις συνολικές εισπράξεις όλων των καταστημάτων
β. το μέσο όρο των εισπράξεων  όλων των καταστημάτων
γ. το όνομα του καταστήματος που είχε τις μεγαλύτερες εισπράξεις
"""
katastimata=[]
eispraksis=[]
for i in range(10):
    onomata=raw_input()
    katastimata.append(onomata)
    lefta=input()
    eispraksis.append(lefta)
sinolikes_eispraksis=0.0
for i in range(10):
    sinolikes_eispraksis=sinolikes_eispraksis+eispraksis[i]
m_eispraksis=sinolikes_eispraksis/10.0
meg=eispraksis[0]
for i in range(10):
    if meg<eispraksis[i]:
        meg=eispraksis[i]
        on_kat_meg_eispr=katastima[i]
print sinolikes_eispraksis , “h συνολικές εισπράξεις όλων των καταστημάτων”
print m_eispraksis , “ο μέσο όρο των εισπράξεων  όλων των καταστημάτων”
print on_kat_meg_eispr , “το όνομα του καταστήματος που είχε τις μεγαλύτερες εισπράξεις”

"""
Να γραφεί πρόγραμμα που θα διαβάζει σε δύο λίστες τα ονόματα και τους 
βαθμούς 10 μαθητών και θα βρίσκει το όνομα του μαθητή με το μικρότερο βαθμό 
και το πλήθος των μαθητών που έχουν βαθμό πάνω από 15.
"""

# -*- coding: utf-8 -*-
bathmos=[]
onoma=[]
pl=0
for i in range(10):
    bath=input("δωσε βαθμο")
    on=input("δωσε αριθμο")
    bathmos.appende(bath)
    onoma.append(on)
minn=bathmos[0]
thesi = 0
for i in range(10):
    if bathmos[i]<minn:
        min=bathmos[i]
        thesi = onoma[i]
    if bathmos[i]>=15:
        pl=pl+1
print pl , " πλήθος των μαθητών που έχουν βαθμό πάνω από 15"
print thesi , "μαθητης με μικροτερο μαθητη"

"""
Να γραφεί πρόγραμμα που θα διαβάζει σε δύο λίστες τα ονόματα και 
και τους βαθμούς 50 μαθητών και θα τυπώνει τα ονόματα των μαθητών 
που έχουν το μεγαλύτερο βαθμό. (Προσοχή! Μπορεί να είναι περισσότεροι από ένας).
"""
# -*- coding: utf-8 -*-
onomata=[]
bathmous=[]
for i in range(50):
    onoma=raw_input("δωσε ονομα")
    bath=input("δωσε βαθμο")
    onomata.append(onoma)
    bathmous.append(bath)
meg=bathmous[0]
for i in range(50):
    if meg<bathmous[i]:
        meg=bathmous[i]
for i in range(50):
    if meg==bathmous[i]:
        print onomata[i] , "και αυτος με τον μεγαλύτερο βαθμό"