import time
import sys

try:
    while True:
        current_time = time.strftime("%Y-%m-%d %I:%M:%S")
        sys.stdout.write("\r" + current_time)
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")



import sys

# Print the version of Python being used
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# Access command-line arguments
print("Command-line arguments:")
for arg in sys.argv:
    print(arg)

# Exit the program
sys.exit("Exiting the program")



