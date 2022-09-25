# -*- coding: utf-8 -*-
O=raw_input("Όνομα πελάτη")
a=input("πόσα θες ")

if a>=800:
    j=a*17
    print j, " θα πληρωσεις για " , a , "τεμαχια  "
if a>=350 and a<800:
    j=a*21 
    print j, " θα πληρωσεις για " , a , "τεμαχια  "
if a>=150 and a<350:
    j=a*25
    print j, " θα πληρωσεις για " , a , "τεμαχια  "
if a<150:
    print "ακυρο"
if 1500>=j:
    print j-j*0.09

