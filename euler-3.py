def main():

  number = 600851475143
  factors = get_prime_factors(number)
  print(max(factors))

def get_prime_factors(number):

  factors = []
  for i in range(2,int(number/2)+1):
    if number % i == 0:
      print(i)
      

  return factors

main()
        

  