# Decorators with parameters
# example

def logged(function):

  def wrapper(*args, **kwargs):
    value = function(*args, **kwargs)
    with open('logfile.txt', 'a+') as f:
      fname = function.__name__
      print(f'{fname} returned value {value}')
      f.write(f'{fname} returned value {value}\n')
    return value
  return wrapper

@logged
def add(x, y):
  return x + y

if __name__ == '__main__':
  print(add(20,2))