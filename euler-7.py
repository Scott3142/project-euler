import math

def main():

  count = 0
  iter = 1
  top_number = 10002
  while True:
    is_prime_value = is_prime(iter)
    if is_prime_value:
      count += 1
    if count == top_number:
      break
    iter += 1
  
  print(iter)

def is_prime(number):

  for i in range(2,int(math.sqrt(number))+1):
    if number % i == 0:
      return False

  return True

main()