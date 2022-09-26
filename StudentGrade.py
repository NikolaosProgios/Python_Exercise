"""
Να ορίσετε την κλάση Student η οποία περιέχει τα παρακάτω
δεδοµένα: 
• το όνοµα του µαθητή(name) 
• µια λίστα µε τους βαθµούς του µαθητή (grades) 
• µια µεταβλητή κλάσης η οποία µετράει πόσα αντικείµενα
υπάρχουν κάθε στιγµή (students_count) 
και τις παρακάτω µεθόδους: 
• κατασκευαστής (constructor) αντικειµένων της κλάσης
µαθητής ( __init__ ) 
• εµφανίζει µήνυµα “καληµέρα” και το όνοµα του µαθητή 
• υπολογίζει και επιστρέφει το µέσο όρο των βαθµών του
µαθητή (average) 
• εµφανίζει το περιεχόµενο της µεταβλητής πλήθος_µαθητών, 
δηλαδή είναι µέθοδος κλάσης και µπορεί να κληθεί και µε το
όνοµα της κλάσης. 
Στη συνέχεια να γράψετε ένα πρόγραµµα το οποίο: 
4) ∆ηµιουργεί 5 αντικείµενα student µε στοιχεία συµµαθητών
σας. 
5) Αποθηκεύει τα αντικείµενα αυτά σε µια λίστα. 
6) ∆ιατρέχει τη λίστα και εµφανίζει τα ονόµατα όσων έχουν µέσο
όρο πάνω από 18. 
7) Εµφανίζει το όνοµα του µαθητή µε το µεγαλύτερο µέσο όρο.
"""
class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def kal (self):
        print 'kalhmera',self.name
    def av(self):
        athr = 0
        for i in self.grades:
            athr = athr + i
        return float(athr)/len(self.grades)

st1 = Student('Nikos',[15,17,18,19])
st2 = Student('Giorgos',[18,16,20,14])
st3 = Student('Thanasis',[18,20,19,20])
lista = [st1,st2,st3]
print 'oi mathites pou exoun  meso oro kato apo 18 einai:'
for i in lista:
    if i.av() < 18:
        print i.name
meg = lista[0].av()
meg_on = lista[0].name
for i in lista:
    if i.av() > meg:
        meg = i.av()
        meg_on = i.name
print 'to megalutero meso oro ton exei o',meg_on