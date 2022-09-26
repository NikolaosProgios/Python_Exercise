def Seira(ant1,ant2):
  print('oi times einai ',ant1,' kai ',ant2)
  print(' oi antistaseis einai se seira')
  print(' i sinoliki antuistasi einai ',ant1+ant2 )

def Paralila(ant1,ant2):
  print('oi times einai ',ant1,' kai ',ant2)
  print(' oi antistaseis einai se Paralila ')
  print(' i sinoliki antuistasi einai ',ant1*ant2/(ant1+ant2))
  
R1=input("dose tin timi R1")
R2=input("dose tin time R2")

print('dose tin timi 1 ean thes stin siera allios dose 2 an thes parallila')
diataksi=input('epelekse 1 ii 2')

if diataksi==1:
   Seira(R1,R2)
else:
   Paralila(R1,R2)