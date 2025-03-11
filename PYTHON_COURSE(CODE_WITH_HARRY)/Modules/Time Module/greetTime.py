import time
import sys
current_time = time.strftime("%I:%M:%S %p")
current_hour = time.localtime().tm_hour

if 5<= current_hour < 12:
  greeting = "Good Morning!"
elif 12 <= current_hour < 17:
  greeting = "Good Afternoon!"
elif 17 <= current_hour < 21:
  greeting = "Good Evening!"
else:
  greeting = "Good night!"

print(greeting)
print("The Current time is: ")
try:
    while True:
        current_time = time.strftime("%A-%d-%B,%Y %I:%M:%S %p")
        sys.stdout.write("\r" + current_time)
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")

