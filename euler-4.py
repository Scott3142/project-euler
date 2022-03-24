def main():

  max_palindrome = 0
  for num1 in range(100,1001):
    for num2 in range(100,1001):
      number = num1*num2
      if is_palindrome(number):
        if number > max_palindrome:
          max_palindrome = number

          print(max_palindrome)
    

def is_palindrome(number):

  switch = True
  number_as_string = str(number)
  if len(number_as_string) % 2 != 0:
    int(number_as_string.replace(str(len(number_as_string)-1/2),""))
    
  for iter in range(int(len(number_as_string)/2)):
    if number_as_string[iter] != number_as_string[-iter-1]:
      switch = False

  return switch

main()