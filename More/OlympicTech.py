"""
11.	Για την πρώτη φάση της Ολυμπιάδας Πληροφορικής δήλωσαν συμμετοχή 500 μαθητές. 
Οι μαθητές διαγωνίζονται σε τρεις γραπτές εξετάσεις και βαθμολογούνται με ακέραιους βαθμούς 
στη βαθμολογική κλίμακα από 0 έως και 100.
Να γράψετε πρόγραμμα το οποίο:
α. Να διαβάζει τα ονόματα των μαθητών και να τα αποθηκεύει σε λίστα.
β. Να διαβάζει τους τρεις βαθμούς που έλαβε κάθε μαθητής, να βρίσκει το μέσο όρο τους, τον 
οποίο θα αποθηκεύει σε άλλη λίστα.
γ. Να εκτυπώνει τα ονόματα των μαθητών και δίπλα τους το μέσο όρο των βαθμών τους ταξινομημένα 
με βάση τον μέσο όρο κατά φθίνουσα σειρά. Σε περίπτωση ισοβαθμίας η σειρά ταξινόμησης των ονομάτων 
να είναι αλφαβητική.
δ. Να υπολογίζει και να εκτυπώνει το πλήθος των μαθητών με το μεγαλύτερο μέσο όρο. Ο μεγαλύτερος 
μέσος όρος είναι ο πρώτος στη λίστα αφού η λίστα είναι ταξινομημένη με βάση τον μέσο όρο. Άρα 
ουσιαστικά ψάχνουμε να βρούμε πόσα στοιχεία της λίστας είναι ίσα με τον πρώτο αριθμό της λίστας.
"""
mathites=[]
bathmi=[]
for math in range (500):
    m=raw_input('onoma mathiti: ')
    mathites.append(m)
    a=int(input('bathmos mathiti: '))
    b=int(input('bathmos mathiti: '))
    c=int(input('bathmos mathiti: '))
    mo=(a+b+c)/3.0
    bathmi.append(mo)
n=len(bathmi)
for i in range(1,n,1):
    for j in range(n-1,i-1,-1):
        if bathmi[j]>bathmi[j-1]:
            bathmi[j],bathmi[j-1]=bathmi[j-1],bathmi[j]
            mathites[j],mathites[j-1]=mathites[j-1],mathites[j]
        elif bathmi[j]==bathmi[j-1]:
            if mathites[j]<mathites[j-1]: 
                mathites[j],mathites[j-1]=mathites[j-1],mathites[j]
for i in range(500):
    print 'onoma mathiti: ' , mathites[i] , 'me bathmo: ' , bathmi[i]
pl=0
    for i in range(1,501,1):
        if bathmi[0]==bathmi[i]:
            pl+=1
print 'το πλήθος των μαθητών με το μεγαλύτερο μέσο όρο είναι', i
"""
Ο μεγαλύτερος μέσος όρος είναι ο πρώτος στη λίστα αφού η λίστα είναι ταξινομημένη με 
βάση τον μέσο όρο. Άρα ουσιαστικά ψάχνουμε να βρούμε πόσα στοιχεία της λίστας είναι ίσα 
με τον πρώτο αριθμό της λίστας. Αν υπάρχουν τέτοια στοιχεία θα είναι ακριβώς μετά από το 
πρώτο στοιχείο αφού η λίστα είναι ταξινομημένη. Πχ [88,88,88,84,83,……….]. Άρα
"""
        flag = False
		i = 1
		While flag == False and i < 500:
			if bathmi[i] < bathmi[0]:                                  
				flag = True
			else:
				i = i + 1
		print 'το πλήθος των μαθητών με το μεγαλύτερο μέσο όρο είναι', i