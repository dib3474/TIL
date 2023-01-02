class Car():

  #method
  def start(what):
    print(what.color)
    print("I started")
  
  def __str__(self):
    return f"Car with {self.wheels} wheels"

  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.door = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black") #get("키워드", "기본값"))
    self.price = kwargs.get("price", "$20")

#function
def start():
  print("I started")

porche = Car() 
porche.color = "Red"
porche.start()
#파이썬은 method를 실행할 때 method에 실행한 instance 를 인자로 준다

ferrari = Car(color = "green", price = "$40")
print(ferrari.color, ferrari.price)

mini = Car()
print(mini.color, mini.price)
#지정된 color와 price가 없기 때문에 기본으로 정해진 내용이 출력

print(dir(Car))
#dir은 class에 있는 모든 메소드를 확인함
#class를 생성했을 때 생기는 만들어지는 메소드를 확인 할 수 있음

print(porche)

#__str__ 도 메소드, 클래스는 string으로 출력할 때 실행되는 메소드

