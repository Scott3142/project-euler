def main():

  top_number = 4000000
  fib = fib_create(top_number)

  sum = 0
  for number in fib:
    if number % 2 == 0:
      sum += number

  print(sum)

def fib_create(limit):

  next_number = 2
  fib = [1,next_number]
  iter = 1
  while next_number < limit:
    next_number = fib[iter-1]+fib[iter]
    fib.append(next_number)
    iter += 1

  return fib

main()