def find_uniq(arr):
    # your code here
    if arr[0] != arr[1] and arr[1] == arr[2]:
      return arr[0]
    else:
      n = arr[0]
      for i in arr:
        if i != n:             
          n = i
          break
      return n   # n: unique number in the array

print(find_uniq([ 1, -1, 1, 1, 1, 1 ]))