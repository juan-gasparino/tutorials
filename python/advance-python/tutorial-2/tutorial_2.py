# Decorators
# example

def my_decorator(function):

  def wrapper():
    print('I am decorating your function')
    function() # hello_world function you can put this first and then the decorator print or vice-versa

  return wrapper

@my_decorator
def hello_world():
  print('hello world')

if __name__ == '__main__':
  hello_world()