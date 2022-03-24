def main():

  iter = 102400000
  top_number = 20
  while True:
    count = 0
    if iter % 100000 == 0:
      print(iter)
    for divisor in range(1,top_number+1):
      if iter % divisor == 0:
        count += 1
      if count == top_number:
        print(iter)
        exit()
    iter += 1

main()