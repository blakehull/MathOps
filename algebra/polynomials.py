import math
import bisect
import random

class Operator:

    def __init__(self):
        return None

    def n_choose_i(self, n, i):
        if n >= i:
            c = n - i
            p = math.factorial(n)
            q = math.factorial(i)*math.factorial(c)
            return p/q
        else:
            return 0

    def power_set(self, numberofelements, order = None):
        if order == True:
            return pow(2, numberofelements)
        else:
            return None

    def product(self, list=[]):
        return pow(math.e,sum([math.log(x) for x in list]))

    def factorial(self,n, mod=None):
        if mod == None:
            if n == 0:
                return 1

            if n < 0:
                raise ValueError("undefined for negative numbers")

            small_swing = [1, 1, 1, 3, 3, 15, 5, 35, 35, 315, 63, 693, 231, 3003, 429, 6435, 6435,
                           109395, 12155, 230945, 46189, 969969, 88179, 2028117, 676039, 16900975,
                           1300075, 35102025, 5014575, 145422675, 9694845, 300540195, 300540195]

            def product(s, n, m):
                if n > m: return 1
                if n == m: return s[n]
                k = (n + m) // 2
                return product(s, n, k) * product(s, k + 1, m)

            def swing(m, primes):
                if m < 33: return small_swing[m]

                s = bisect.bisect_left(primes, 1 + math.sqrt(m))
                d = bisect.bisect_left(primes, 1 + m // 3)
                e = bisect.bisect_left(primes, 1 + m // 2)
                g = bisect.bisect_left(primes, 1 + m)

                factors = primes[e:g]
                factors += filter(lambda x: (m // x) & 1 == 1, primes[s:d])
                for prime in primes[1:s]:
                    p, q = 1, m
                    while True:
                        q //= prime
                        if q == 0: break
                        if q & 1 == 1:
                            p *= prime
                    if p > 1: factors.append(p)

                return product(factors, 0, len(factors) - 1)

            def odd_factorial(n, primes):
                if n < 2: return 1
                return (odd_factorial(n // 2, primes) ** 2) * swing(n, primes)

            if n < 20:
                return product(range(2, n + 1), 0, n - 2)

            b, bits = n, n
            while b != 0:
                bits -= b & 1
                b >>= 1
            bits = pow(2, bits)

            primes = algebra.Factorizer().rho(n)
            return odd_factorial(n, primes) * bits
        else:
            return 0
    def mod(self, a, b):
        return a % b

class IntFactorizer:

    def __init__(self):
        return None

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def rho(self, n, factors=[]):
        seen = []
        k = 1
        if n % 2 == 0:
            j = self.pulltwos(n, 0)
            if j[0] == 1:
                for i in range(0, j[1]):
                    factors.append(2)
                return factors
            else:
                for i in range(0, j[1]):
                    factors.append(2)
            n = j[0]


        x = lambda c: (pow(c, 2) + k) % n
        d = 1
        g = 1
        while d == 1:
            xy = abs(g - x(g))
            d = self.gcd(xy, n)
            g = x(g)
            if g in seen:
                seen = []
                k = k + 1
                while k % n == 0 or k % n == n - 2:
                    k = k + 1
                x = lambda c: (pow(c, 2) + k) % n
            else:
                seen.append(g)
        if d == n:
            factors.append(n)
            return factors
        else:
            factors.append(d)
            return self.rho(n / d, factors)

    def pulltwos(self, n, j):
        if n % 2 == 0 and n > 0:
            return self.pulltwos(n / 2, j + 1)
        else:
            return [n, j]

class Primes:

    def __init__(self):
        return None

    def wilsonsTheorem(self,n):
        operator = Operator()
        print operator.factorial(n)

    def generateprimes(self, eisenstein=None):
        if eisenstein is None:
            p = 256
        else:
            p = eisenstein.bit_length()
        # used in generating public information
        # The primes here are not very large, but this is more for fun than implementation.
        # This is the Miller-Rabin primality test. At 40 rounds, we can be fairly certain the number a is prime.
        # if you are not convinced of this, I suggest something-searching or working out the probability yourself.
        a = random.randint(2 ** p, 2 ** (2*p))
        while pow(2, a - 1, a) != 1:
            while (a % 2) == 0:
                a = random.randint(2 ** p, 2 ** (2*p))
            for i in range(1, 50):
                if pow(i, a, a) != i:
                    a = random.randint(2 ** p, 2 ** (2*p))
                    break
        return a

class Theorems:
    def Eisenstein(self, Coefficients=[]):
        usedprimes = []
        p = Primes().generateprimes(max(Coefficients))
        usedprimes.append(p)
        while p < max(Coefficients):
            if p > max(Coefficients):
                usedprimes.append(p)
                p = Primes().generateprimes(max(Coefficients))
            for i,c in enumerate(Coefficients):
                print pow(p, 2), c != 1
                if i == 0:
                    if p % c == 0 and c != 1:
                        return 'Reducible1'
                if p % c == 0 & c != 1:
                    next
                if i == len(Coefficients) - 1:
                    if pow(p, 2) % c == 0 and c != 1:
                        return 'Reducible2'
            p = Primes().generateprimes(max(Coefficients))
            if p > max(Coefficients) or p in usedprimes:
                print usedprimes
                usedprimes.append(p)
                p = Primes().generateprimes(max(Coefficients))
        return 'Irreducible'
