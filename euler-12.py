import math

def main():

  triangle_number, iter = 0, 1
  top_limit = 500
  while True:
    triangle_number += iter
    number_of_divisors = get_all_divisors(triangle_number)
    if number_of_divisors > top_limit:
      print(triangle_number)
      break
    iter += 1

def get_all_divisors(number):

  divisors = [1,number]
  for i in range(2,int(math.sqrt(number))):
    if number % i == 0:
      divisors.append(i)
      if int(number/i) not in divisors:
        divisors.append(int(number/i))

  return len(divisors)

main()