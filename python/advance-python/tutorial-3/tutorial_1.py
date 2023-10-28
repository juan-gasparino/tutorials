#Generators Yield
import sys

def cubic_iterator(n):
  for x in range(n):
    yield x ** 3

def show_values(values):

  for item in values:
    print(item)

def infinite_sequence():
  result = 1
  while True:
    yield result
    result *= 5

if __name__ == '__main__':

  #example 1
  print('example 1') #you can use next or for without next
  values = cubic_iterator(10)
  print(next(values))
  print(next(values))
  print(next(values))

  #example 2
  print('\nexample 2')
  show_values(values)

  # example 3 the size is always the same. It doesnt matter the iterator because
  # we are not adding more data. the size is always the same
  print('\nexample 3')
  values = cubic_iterator(10)
  print(f'size in bytes: {sys.getsizeof(values)}')

  values = cubic_iterator(100000)
  print(f'size in bytes: {sys.getsizeof(values)}')

  # example 4
  print('\nexample 4')
  values = infinite_sequence()

  for item in range(1, 10):
    print(next(values))