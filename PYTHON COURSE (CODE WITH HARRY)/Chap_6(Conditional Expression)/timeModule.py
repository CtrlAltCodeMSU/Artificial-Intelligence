# import time
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print("Formatted time:", formatted_time)

# import time
# print("Pausing for 3 seconds...")
# time.sleep(3)
# print("Resumed")

# import time
# time_string = "2024-08-28 14:30:00"
# parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
# formatted_time = time.strftime("%A, %B %d, %Y %I:%M %p", parsed_time)
# print("Formatted time:", formatted_time)

import time
print(time.time())
print("Start")
# time.sleep(1)
print("End")

print(time.ctime())
current_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
print(current_time)

local = time.localtime()
print("Local time is: " , local)

utc = time.gmtime()
print("Local time is: " , utc)

format = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
print("Formatted time: " , format)



# import time
time_string = "2024-08-28 14:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
formatted_time = time.strftime("%A, %B %d, %Y %I:%M %p", parsed_time)
print("Formatted time:", formatted_time)



print(time.strftime("%d/%m/%y"))
print(time.strftime("%A, %B %d %Y"))
print(time.strftime("%I:%M:%S %p"))

current_time = time.localtime()

# Format the time as a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(formatted_time)

time_string = "2024-08-28 14:30:00"

# Parse the string into a struct_time object
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(parsed_time)

