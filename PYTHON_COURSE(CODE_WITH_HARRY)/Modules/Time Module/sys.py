import time
import sys

try:
    while True:
        current_time = time.strftime("%Y-%m-%d %I:%M:%S")
        sys.stdout.write(current_time + "\r")
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
        print("\n Clock stopped")
