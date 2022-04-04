import math

def main():

  number = math.factorial(100)
  
  sum = 0
  for character in str(number):
    sum += int(character)

  print(sum)

main()