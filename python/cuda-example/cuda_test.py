import torch
import time

if __name__ == '__main__':

  if torch.cuda.is_available() == True:
    device = torch.device('cuda')
  else:
    device = torch.device('cpu')

matrix_size = 32*128

x_cpu = torch.randn(matrix_size, matrix_size)
y_cpu = torch.randn(matrix_size, matrix_size)

print("************************CPU SPEED****************************")
start = time.time()
result_cpu = torch.matmul(x_cpu, y_cpu)
print("Time taken for CPU: ", time.time() - start)
print("verify device: ", result_cpu.device)

x_gpu = x_cpu.to(device)
y_gpu = y_cpu.to(device)
torch.cuda.synchronize()
print("************************GPU SPEED****************************")
for i in range(3):  # warm up first and then we run the test 2 more times after the warm up
  start = time.time()
  result_gpu = torch.matmul(x_gpu, y_gpu)
  torch.cuda.synchronize()
  print("Time taken for GPU: ", time.time() - start)
  print("verify device: ", result_gpu.device)
