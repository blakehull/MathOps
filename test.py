from algebra import polynomials
import math

o = polynomials.Theorems()
primes = []
for i in range(1,1000000):
    p = polynomials.Primes().generateprimes()
    if p not in primes:
        print p
        primes.append(p)
