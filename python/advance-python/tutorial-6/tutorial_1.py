#Synchronizing threads
import threading
import time

x = 8192

lock = threading.Lock() #help to lock the resource completly until you release it to allow to use by a diff thread

def double():
  global x, lock
  lock.acquire()
  while x < 16384:
    x *= 2
    print(int(x))
    time.sleep(1)
  print('Reached the maximum!')
  lock.release()


def halve():
  global x, lock
  lock.acquire()
  while x > 1:
    x /= 2
    print(int(x))
    time.sleep(1)
  print('Reached the minimum!')
  lock.release()


if __name__ == '__main__':
  t1 = threading.Thread(target=halve)
  t2 = threading.Thread(target=double)

  t1.start()
  t2.start()