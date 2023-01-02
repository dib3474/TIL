def plus(*args, **kwargs):
  result = 0
  for number in args:
    result += number
  print(result)

plus(1,56,732,43,73,32,4,4,3)

# *args 인자 무제한 / **kwargs 키워드 인자 무제한