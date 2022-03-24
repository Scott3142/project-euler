def main():

  top_number = 100
  sum_of_squares = get_sum_of_squares(top_number)
  square_sum = get_square_sum(top_number)

  print(f"Difference: {square_sum - sum_of_squares}")

def get_sum_of_squares(top_number):

  sum_of_squares = 0
  for i in range(top_number+1):
    sum_of_squares += i**2
  
  return sum_of_squares

def get_square_sum(top_number):

  square_sum = 0
  for i in range(top_number+1):
    square_sum += i
  
  return square_sum**2

main()