def is_valid_IP(strng):
  if len(strng.split(".")) != 4:
    return False

  for oct in strng.split("."):
    if " " in oct:
      return False
    if len(oct) > 1 and oct[0] == "0":
      return False
    try:
      if int(oct) < 0 or int(oct) > 255:
        return False    
    except:
      return False

  return True

value = is_valid_IP("1.2.3.4.5")
assert value == False

value = is_valid_IP("1.2.3.4")
assert value == True

value = is_valid_IP("1.2.3.400")
assert value == False

value = is_valid_IP("1.2.3.-10")
assert value == False

value = is_valid_IP('12.255.56.1')
assert value == True
value = is_valid_IP('')
assert value == False
value = is_valid_IP('abc.def.ghi.jkl')
assert value == False
value = is_valid_IP('123.456.789.0')
assert value == False
value = is_valid_IP('12.34.56')
assert value == False
value = is_valid_IP('12.34.56 .1')
assert value == False
value = is_valid_IP('12.34.56.-1')
assert value == False
value = is_valid_IP('123.045.067.089')
assert value == False
value = is_valid_IP('127.1.1.0')
assert value == True
value = is_valid_IP('0.0.0.0')
assert value == True
value = is_valid_IP('0.34.82.53')
assert value == True
value = is_valid_IP('192.168.1.300')
assert value == False