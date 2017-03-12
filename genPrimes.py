""" 
test
"""

import math

def genPrimes():
    primes_list = [2]
    while True:
        

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def generate_primes(number_of_primes):
    # Generate prime numbers until number_of_primes is reached
    counter = 0
    num = 0
    while counter < number_of_primes:
        # print("vor code| num:", num, "counter:", counter)
        if is_prime(num):
            counter += 1
            num += 1
            # print("true    | num:", num, "counter:", counter)
        else:
            num += 1
            # print("else    | num:", num, "counter:", counter)
    num -= 1
    return num


print(generate_primes(final_prime))