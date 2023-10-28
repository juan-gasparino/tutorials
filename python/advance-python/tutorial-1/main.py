# dunder- function with __something__
# example

class Person: #__init__ and __del__

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __del__(self):
    print('object Person have been destroy')


class Vector:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __repr__(self): #function strictly for debugging
    return f"X: {self.x}; Y:{self.y}"

  # def __str__(self):
  #   return f"X: {self.x}; Y:{self.y}"

  def __len__(self):
    return 10

  def __call__(self):
    print("hello I was called !")

  def __del__(self):
    print('object Vector have been destroy')


if __name__ == '__main__':
  p1 = Person('John', 20)
  v1 = Vector(15, 5)
  v2 = Vector(20, 25)
  v3 = v1 + v2
  print(v3.x)
  print(v3.y)
  print(v3) # __repr__
  print(len(v3)) # __len__ In this case in particular will return 10 just cuz it's hardcode
  v3() # __call__ method