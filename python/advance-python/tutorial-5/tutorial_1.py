#Encapsulation


class Person:
  def __init__(self, name, age, gender):
    self.__name = name
    self.__age = age
    self.__gender = gender

  @property
  def Name(self):
    return self.__name

  @Name.setter
  def Name(self, value):
    self.__name = value

  def __str__(self):
    return f'name: {self.__name}\nage: {self.__age}\ngender: {self.__gender}'

if __name__ == '__main__':
  p1 = Person('John', 20, 'M')
  print(p1)
  p1.Name = 'Mike'
  print(p1)