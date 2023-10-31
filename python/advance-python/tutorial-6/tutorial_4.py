#Synchronizing Daemon threads
import threading
import time 

path = ''
text = ''

def read_file():
  global path, text
  while True:
    with open('text.txt', 'r') as f:
      text = f.read()
    time.sleep(3)


def print_loop():
  for i in range(30):
    print(f'iteration number: {i+1} {text}')
    time.sleep(1)


if __name__ == '__main__':

  t1 = threading.Thread(target=read_file, daemon=True)
  t2 = threading.Thread(target=print_loop)

  t1.start()
  t2.start()