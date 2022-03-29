def main():

  max_chain_length = 0
  max_chain = 1
  for number in range(1000000):
    chain_length = collatz(number)
    if chain_length > max_chain_length:
      max_chain_length = chain_length
      max_chain = number
      print(f"Max chain = {max_chain}, with length {max_chain_length}.")

  print(max_chain)

def collatz(i):
 
  iter = 0
  while i > 1:
    if i % 2 == 0:
      i /= 2
    else:
      i = 3*i + 1
    iter += 1
  
  return iter

main()