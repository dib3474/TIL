def plus(a,b):
  return a - b

result = plus(b=41, a=6)
print(result)

#인자를 순서로 인식하는 것이 아니라 인자를 이름으로 인식함

def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

# ""앞에 f를 붙이고 원하는 변수에 {}를 씌우면 string에서 변수 사용 가능
hello = say_hello("suho", "19")
print(hello)