#6
   logfile=open('test.log','w')
   logfile.write('test succeded')
   logfile.close()
   print file('test.log').read()
test succeded
   logfile=open('test.log','a')
   logfile.write('line 2')
   logfile.close()
   print file('test.log').read()
test succededline 2 