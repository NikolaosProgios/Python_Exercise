import os, sys
leksi='car'
anagram='arc'
listaLeksi=list(leksi)
listaAnagram=list(anagram)
if len(listaLeksi)==len(listaAnagram):
    for gramma in listaLeksi[::-1]:
        if gramma in listaAnagram
            listaLeksi.remove(gramma)
    if listaLeksi==[]:
        print 'Αναγραμματισμός'
else:
    print 'Μη αγραμματισμός'