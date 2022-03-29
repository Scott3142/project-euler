def main():

  sum_of_letters = get_number_of_letters()
  print(sum_of_letters)

def get_number_of_letters():
  
  numbers_in_words = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

  sum_in_numbers_less_than_ten = 0 # 1 - 20
  for i in range(9):
    sum_in_numbers_less_than_ten += len(numbers_in_words[i]) 

  sum_in_numbers_ten_to_nineteen = 0 # 1 - 20
  for i in range(9,19):
    sum_in_numbers_ten_to_nineteen += len(numbers_in_words[i]) 
  
  sum_of_tens_identifiers = 0 # 20,30,40,50,60,70,80,90
  for i in range(19,27):
    sum_of_tens_identifiers += len(numbers_in_words[i])

  sum_in_twenty_to_ninetynine = 10*sum_of_tens_identifiers + 8*sum_in_numbers_less_than_ten  

  sum_in_one_to_ninetynine = sum_in_numbers_less_than_ten + sum_in_numbers_ten_to_nineteen + sum_in_twenty_to_ninetynine

  sum_of_hundred_to_999 = 100*sum_in_numbers_less_than_ten + 9*sum_in_one_to_ninetynine + 9*len("hundred") + 891*(len("hundred") + len("and"))

  sum_of_letters = sum_in_one_to_ninetynine + sum_of_hundred_to_999 + len("onethousand")

  return sum_of_letters

main()
