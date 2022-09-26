#i)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
text = 'the quick brown fox jumps over the lazy dog'
res = []
for i in alphabet:
    if i in text:
        res.append(i)
if res == alphabet :
    print 'is pangram'
else:
    print 'is not pangram'

#OR

#ii)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
text = 'the quick brown fox jumps over the lazy dog'
for i in alphabet(23,0):
    if i in inputText:
        aplabet.remove(i)
if alphabet==[]:
    print "panagram"
else:
    print " not panagram"
