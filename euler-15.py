import random

# Note - is also solvable combinatorially with binomial - 40!/20!^2

def main():

  grid_size = 20
  routes = []

  while True:
    
    i, j = 0, 0
    directions = ""

    while True:

      direction_choice = random.randint(0,1)
      if direction_choice == 0:
        if i < grid_size:
          directions += "R"
          i += 1        
      else:
        if j < grid_size:  
          directions += "D"
          j += 1

      if i == grid_size and j == grid_size:
        if directions not in routes:
          routes.append(directions)
          break 

    print(routes)

main()