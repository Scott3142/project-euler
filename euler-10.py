import math

def main():
  
  top_number = 2000000
  primes = collect_primes(top_number)

  sum = 0 
  for prime in primes:
    sum += prime

  print(sum)

def collect_primes(top_number):

  primes = []
  for i in range(2,top_number):
    if is_prime(i):
      primes.append(i)

  return primes

def is_prime(number):

  for i in range(2,int(math.sqrt(number))+1):
    if number % i == 0:
      return False

  return True

main()