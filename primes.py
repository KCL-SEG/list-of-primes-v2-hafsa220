"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

prime30 =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def primes(number_of_primes):
    list1 = []
    list1 = prime30[:number_of_primes]

    print(list1)
    return list1


number = int(input("enter a positive number > 0: "))

primes(number)