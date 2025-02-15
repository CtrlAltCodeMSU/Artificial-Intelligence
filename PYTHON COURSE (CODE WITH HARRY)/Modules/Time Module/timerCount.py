
import time
duration_input = input("Enter Countdown duration (e.g., '10' , '10m' , '3h 20m'): " )

total_seconds = 0 
parts = duration_input.lower().split()

for part in parts:
  if 's' in part:
    total_seconds += int(part.replace('s' , ''))
  elif 'm' in part:
    total_seconds += int(part.replace('m' , ''))*60
  elif 'h' in part:
    total_seconds += int(part.replace('h',''))*3600

while total_seconds > 0:
  mins , secs = divmod(total_seconds, 60)
  hours , mins = divmod(mins , 60)
  format_time = f"{hours:02}:{mins:02}:{secs:02}"
  print("  " + str(format_time) , end='\r')
  time.sleep(1)
  total_seconds -= 1
print("00:00:00")  