import time

count = int(input("Enter seconds for countdown: "))
while count > 0:
  print( " " + str(count) , end="")
  time.sleep(1)
  count -= 1
print(" \n Times's up")

# start_time= time.time()
# time.sleep(1)
# end_time = time.time()
# print("Execution time: " , end_time - start_time , "Seconds")


