class Car():  
  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.door = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black") #get("키워드", "기본값"))
    self.price = kwargs.get("price", "$20")

  def __str__(self):
    return f"Car with {self.wheels} wheels"


class Convertible(Car): #인자 안에 클래스로 extend
  def __init__(self, **kwargs): 
    super().__init__(**kwargs) #super 함수로 상속받음
    self.time = kwargs.get("time", 10)

  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"

porche = Convertible(color="green", price="$40")
porche.take_off()
porche.wheels
print(porche)
print(porche.color)