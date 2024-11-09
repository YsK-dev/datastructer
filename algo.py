import time
def sum_list(lst):
  start = time.time()
  total = 0
  for num in lst:
    total += num
  end = time.time()

  return total , 1000*(end-start)