def main():

  sum = sum_of_digits(2**1000)

  print(sum)

def sum_of_digits(number):

  sum = 0
  for character in str(number):
    sum += int(character)

  return sum

main()