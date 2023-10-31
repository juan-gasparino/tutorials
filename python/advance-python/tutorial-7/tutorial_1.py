#queues
import queue

if __name__ == '__main__':

  #fifo
  q1 = queue.Queue()

  numbers = [10, 20, 30, 40, 50, 60, 70]

  for number in numbers:
    q1.put(number)

  print('fifo list')
  print(q1.get())
  print(q1.get())
  print(q1.get())

  #lifo
  q1 = queue.LifoQueue()

  numbers = [10, 20, 30, 40, 50, 60, 70]

  for number in numbers:
    q1.put(number)

  print('lifo list')
  print(q1.get())
  print(q1.get())
  print(q1.get())

  print('Priority list')

  q1 = queue.PriorityQueue()

  q1.put((2, 'hello world'))
  q1.put((11, 1.1))
  q1.put((1, 1))
  q1.put((4, True))

  while not q1.empty():
    print(q1.get())