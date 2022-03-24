import math

def main():

  num = 1000
  for i in range(1,num+1):
    for j in range(1,num+1):
      sqrt_square_sum = math.sqrt((i**2 + j**2))
      if sqrt_square_sum.is_integer():
        pythag_sum = i + j + sqrt_square_sum 
        if pythag_sum == 1000:
          print(f"{i}, {j}, {sqrt_square_sum}")
          print(f"{i*j*sqrt_square_sum}")
          exit()

main()