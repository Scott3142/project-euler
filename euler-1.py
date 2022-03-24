top_number = 1000

sum = 0
for iter in range(top_number):
  if iter % 3 == 0 or iter % 5 == 0:
    sum += iter

print(f"The sum of the multiples of 3 or 5 below {top_number} is {sum}.")