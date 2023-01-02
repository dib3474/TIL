def plus(a,b):
  if type(b) is int or type(b) is float:
    return a+b
  else:
    return None
# is 가 C언어에서 =와 같다
#영어 문법과 비슷하다

print(plus(12, 1.2))