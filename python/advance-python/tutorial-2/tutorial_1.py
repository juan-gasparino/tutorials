# Decorators
# example

def my_decorator(function):

  def wrapper():
    print('I am decorating your function')
    function()

  return wrapper

def hello_world():
  print('hello world')

if __name__ == '__main__':
  my_decorator(hello_world)() #however, this is not the common way to decorate functions in python