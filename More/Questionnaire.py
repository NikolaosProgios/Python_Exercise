"""
12.	Σ’ ένα διαγωνισμό συμμετέχουν πολλοί υποψήφιοι. Κάθε υποψήφιος διαγωνίζεται σε 50 ερωτήσεις 
πολλαπλής επιλογής. Να αναπτύξετε πρόγραμμα που να κάνει τα παρακάτω: 
α. Να διαβάζει τα ονόματα των υποψηφίων μέχρι να δοθεί ως όνομα η λέξη ‘’telos’’ και να τα αποθηκεύει
 σε μία λίστα
β. Για κάθε υποψήφιο :
	i. Να διαβάζει την απάντησή του σε καθεμία από τις πενήντα ερωτήσεις κάνοντας έλεγχο εγκυρότητας
    ώστε οι απαντήσεις να είναι μόνο 
	     Σ αν είναι σωστή η απάντηση
	     Λ αν είναι λάθος η απάντηση
	     Ξ αν ο υποψήφιος δεν απάντησε
    ii. Να υπολογίζει τη συνολική βαθμολογία του κάθε υποψηφίου αν κάθε Σ βαθμολογείται με 2 μονάδες, 
    κάθε Λ με -1 μονάδες και κάθε Ξ με 0 μονάδες και να την εισάγει σε μία λίστα.
γ. Να τυπώνει το πλήθος των υποψηφίων που συγκέντρωσαν βαθμολογία μεγαλύτερη από 50.
δ. Να τυπώνει το όνομα του υποψηφίου με την μεγαλύτερη βαθμολογία (υποθέστε ότι είναι μόνο ένας).

"""

# -*- coding: utf-8 -*-
onomata=[]
bathmoi=[]
bathmos = 0 
onoma=raw_input('όνομα παίκτη: ')
while onoma!='telos':
    onomata.append(onoma)
    for i in range(50):
        apantisi=raw_input('ti apadise: ')
        while apantisi!='Σ' and apantisi!='Λ' and apantisi!='Ξ':
            apantisi=raw_input('ti apadise: ')
        if apantisi=='Σ':
            bathmos+=2
        elif apantisi=='Λ' :
            bathmos-=1
    bathmoi.append(bathmos) 
    onoma=raw_input('όνομα παίκτη: ')
    bathmos=0
pl=0
for i in bathmoi:
    if i>50:
        pl+=1
print pl , 'ειχαν πανω απο 50'
meg=bathmoi[0]
meg_bath_onom=onomata[0] #(Πρέπει να μπει)   ;;;;;γιατι ;;;;;;
for i in range(len(bathmoi)): 
    if bathmoi[i]>meg:
        meg=bathmoi[i]
        meg_bath_onom=onomata[i]
print 'το παιδι με την μεγαλύτερη βαθμολογία: ' , meg_bath_onom