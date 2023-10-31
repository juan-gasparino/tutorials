#Synchronizing Event
import threading

def test_1(event):
  print('waiting for event to trigger...')
  event.wait()
  print('performing action XYZ now...')


if __name__ == '__main__':
  event = threading.Event()

  t1 = threading.Thread(target=test_1, args=(event,))
  t1.start()

  x = input('Do you want to trigger the event? (y/n)')

  if x == 'y':
    event.set()