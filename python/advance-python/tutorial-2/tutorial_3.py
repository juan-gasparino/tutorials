# Decorators with parameters
# example

def my_decorator(function):

  def wrapper(*args, **kwargs):
    print('I am decorating your function')
    return function(*args, **kwargs) # Its important to keep in mind that the print cant go after the return. To do that, you should use variables to control 
  # the workflow of the function

  return wrapper

@my_decorator
def hello(person):
  return f'hello {person}'

if __name__ == '__main__':
  print(hello('john'))