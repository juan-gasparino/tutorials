def test_1():
  try:
    x = int('First number: ')
    y = int('Second number: ')
    print(x/y)
  except ValueError:
    print('Please enter a valid number next time!')
  except ZeroDivisionError:
    print('Cannot divde by zero!')
    y = 1
    print(x/y)
  finally:
    print('Done!')


if __name__ == '__main__':
  test_1()