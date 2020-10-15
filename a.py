import time

st = time.time()


for i in range(10000):
  if(i%10==0):
    print(i)

et = time.time()

print(et-st)