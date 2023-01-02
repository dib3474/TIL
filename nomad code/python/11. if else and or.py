def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18 or age == 19:
    print("you are new to this!!")
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")
# and == && / ot == || 
# if 는 c랑 작동원리는 비슷함

age_check(19)