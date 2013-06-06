from math import sqrt

problem_no = 3
description = '''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''


def solve():
    factors = []
    n = 600851475143
    posf = 3  # pos(sible) f(actor)
    while n > 1:
        if n % posf == 0:
            # The possible factor is indeed a factor of n. (*)
            factors.append(posf)
            n /= posf
        elif posf > sqrt(n):
            # If n is not a prime number, it could be written as n = a*b.
            # a and b cannot be both larger than sqrt(n).
            # (If they were, then a*b would be greater than n.)
            # If n was indeed not a prime number, we would not be here,
            # as we would have already reached posf = min(a,b) < sqrt(n)
            # and we would be at (*).
            # So if we are here, n must be a prime number itself.
            posf = n
        else:
            posf += 2  # 2 is not a prime factor of 60[..]43, so we can skip
                       # the even numbers. This halves execution time.
            # Note: a more complex algorithm for finding the next factor takes
            # longer to execute than this simple version. See the file
            # 'largest_prime_factor.py' for code and timings.
    return max(factors)


def complex_solve():
    factors = []
    primes = [2]
    limit = 600851475143
    i = 2
    while limit > 1:
        # print i, limit
        if limit % i == 0:
            factors.append(i)
            limit /= i
        else:
            # Find the next prime number.
            prime = False
            while not prime:
                i += 1
                prime = True
                for p in primes:
                    if i % p == 0:
                        prime = False
                        break
                # If 'i' was not a multiple of any of the previously found primes,
                # 'prime' will still be 'True', and we have found a new prime.
                if prime:
                    primes.append(i)
    # print factors
    return max(factors)

if __name__ == '__main__':
    import time
    print 'execution time of simple algo (ms):'
    start = time.clock()
    solve()
    print time.clock() - start, '\n'
    print 'execution time of complex algo (ms):'
    start = time.clock()
    complex_solve()
    print time.clock() - start, '\n'

    print solve(), complex_solve()
