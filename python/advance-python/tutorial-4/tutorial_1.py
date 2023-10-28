#Parsing arguments *args and **kwargs


def test_1(*args, **kwargs):

  print(args[0])
  print(args[1])
  print(args[2])
  print(args[3])
  print(kwargs["arg1"])
  print(kwargs["arg2"])


if __name__ == '__main__':

  test_1(1, 1.2, 'hello', [1,2,3],arg1="hello world", arg2={"test": 1, "test2": [0,1]})
