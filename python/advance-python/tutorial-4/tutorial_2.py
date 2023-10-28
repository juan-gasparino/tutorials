#Parsing arguments getopt

import sys
import getopt


def save_message(filename, message):
  with open(filename, 'a+') as f:
    f.write(message+'\n')


def test_1():
  filename = sys.argv[1]
  message = sys.argv[2]
  print(f'python file name: {sys.argv[0]}')
  print(f'file to save message: {filename}')
  print(f'message: {message}')
  save_message(filename, message)

def test_2():
  opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])
  print(f'Opts values: {opts}')
  print(f'Args values: {args}')

def test_3():
  opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])
  filename = 'text.txt'
  message = 'hello world'
  for opt, arg in opts:
    if opt == '-f':
      filename = arg
    if opt == '-m':
      message = arg
  print(f'filename: {filename}')
  print(f'message: {message}')
  save_message(filename, message)

if __name__ == '__main__':
  #test_1() # uncomment this and run using python tutorial_2.py <filename> <message>
  #test_2() # uncomment this and run using python tutorial_2.py <filename> <message> or -f <filename> -m <message>
  #test_3() # uncomment this and run using python tutorial_2.py -f <filename> -m <message>