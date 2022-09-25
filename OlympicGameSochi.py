"""
ΘΕΜΑ 4.
Στους χειμερινούς Ολυμπιακούς αγώνες του Σότσι της Ρωσίας και στο αγώνισμα του καλλιτεχνικού πατινάζ 
συμμετέχουν 35 αθλητές, οι οποίοι βαθμολογούνται από 8 κριτές. Κάθε αθλητής βαθμολογείται για το τεχνικό 
μέρος από κάθε κριτή. Η συνολική βαθμολογία του αθλητή προκύπτει, αφού αφαιρεθούν η μεγαλύτερη και 
η μικρότερη βαθμολογία. Για παράδειγμα αν κάποιος αθλητής πάρει:
 5.2, 5.0, 4.3, 5.8, 5.1, 5.2, 5.9, 5.0, τότε αφαιρείται το 5.9 και το 4.3 που είναι 
 η καλύτερη και η χειρότερη βαθμολογία και η συνολική βαθμολογία του αθλητή είναι 31.3.
Να γράψετε πρόγραμμα σε Python  το οποίο:
Α. θα διαβάζει τα ονόματα των 35 αθλητών και θα τα αποθηκεύει στη λίστα onom
Β. θα διαβάζει τις βαθμολογίες που δίνουν οι 8 κριτές για κάθε αθλητή. 
Η βαθμολογία που δίνει κάθε κριτής να διασφαλίζεται ότι είναι από 0 μέχρι 6.
Γ. θα υπολογίζει τη συνολική βαθμολογία κάθε αθλητή και θα την αποθηκεύει στη λίστα vath.
Δ. θα ταξινομεί τις δύο λίστες κατά φθίνουσα σειρά με βάση τη βαθμολογία του και θα εμφανίζει 
τα ονόματα που πήραν το χρυσό, το ασημένιο και το χάλκινο μετάλλιο καθώς και τις επιδόσεις τους.
"""

onom = []
vath = []
for i in range(35):
    o = raw_input('dose to onoma')
    onom.append(o)
    meg = -1
    mik = 7
    athr = 0
    for j in range(8):
        b =input('dose to vathmo')
        while b < 0 or b > 6:
            b =input('dose to vathmo')
        athr = athr + b
        if b > meg :
            meg = b
        if b < mik :
            mik = b
    sun_vath = athr - mik - meg
    vath.append(sun_vath)
for i in range(1,35):
    for j in range(34, i - 1, -1):
        if vath[j] > vath[j-1]:
            vath[j],vath[j-1] = vath[j-1],vath[j]
            onom[j],onom[j-1] = onom[j-1],onom[j]
print 'Xryso metallio phre o athlhths',onom[0],'me epidosh',vath[0]
print 'Ahmenio metallio phre o athlhths',onom[1],'me epidosh',vath[1]
print 'Xalkino metallio phre o athlhths',onom[2],'me epidosh',vath[2]

#or

vath=[]
onom=[]
for i in range(35):
    onoma=raw_input('dose to onoma')
    onom.append(onoma)
    lista=[]
    for k in rane(8):
        bath=input('dose to vathmo')
        while bath<0 or bath>6:
            bath=input('dose to vathmo')
        lista.append(bath)
    for p in range(1,35,1):
        for j in range(34,p-1,-1):
            if lista[j]<lista[j]:
                lista[j],lista[j-1]=lista[j-1],lista[j]
    lista.pop()
    lista.pop(1)
    for i in lista:
        vath.append(i)
for i in range(1,35,1):
    for j in range(34,i-1,-1):
        if vath[j]>vath[j-1]:
            vath[j],vath[j-1]=vath[j-1],vath[j]
            onom[j],onom[j-1]=onom[j-1],onom[j]
print 'Xryso metallio phre o athlhths',onom[0],'me epidosh',vath[0]
print 'Ahmenio metallio phre o athlhths',onom[1],'me epidosh',vath[1]
print 'Xalkino metallio phre o athlhths',onom[2],'me epidosh',vath[2]
