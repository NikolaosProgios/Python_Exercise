def primes_sieve(limit):
	limitn=limit + 1
	not_prime=set()
	primes=[]
	for i in range(2,limitn):
	    if i in not_prime:
	        continue
	    for f in range(2*1,limitn,i):
	        not_prime.add(f)
	    primes.append(i)
	return primes
print primes_sieve(1000)