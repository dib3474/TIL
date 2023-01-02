from math import ceil, fsum, fabs, factorial
#from math import fsum as suum -> 함수를 원하는 이름으로 바꾸기

print(ceil(1.2)) #반올림
print(fabs(-1.2)) #절대값
print(factorial(5))
print(fsum([1,2,3,4,5,6,7]))

from calculator import plus, minus
#모듈을 만들고 import 할 수 있음
print(plus(1,2), minus(1,2))