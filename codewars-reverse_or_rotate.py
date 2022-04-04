def revrot(strng, sz):
    # your code
    
        
    if sz <= 0 or len(strng) == 0 or sz > len(strng):
    
        return ""
    
    else:
        number_of_chunks = int(len(strng)/sz)
        new_strng = ""
        ch = 0

        while ch < number_of_chunks:
            chunk = strng[ch*sz:(ch+1)*sz]
            case_type = get_sum(chunk)
            if case_type == "rev":
                new_strng += rev(chunk)    
            elif case_type == "rot":
                new_strng += rot(chunk)   

            ch += 1

        return new_strng
    
def get_sum(chunk):
    sum = 0
    for number in chunk:
        sum += int(number)**3
    if sum % 2 == 0:
        return "rev"
    else:
        return "rot"
    
def rev(strng):
    return strng[::-1]
    
def rot(strng):
    
    new_strng = strng[1]
    for charc in strng[2:]:
        new_strng += charc
    new_strng += strng[0]
    
    return new_strng

def testing(actual, expected):
  print(actual)
  print(expected)
  assert actual == expected
    
print(rot("33449271"))
    
s = "733049910872815764"
testing(revrot(s, 5), "330479108928157")
