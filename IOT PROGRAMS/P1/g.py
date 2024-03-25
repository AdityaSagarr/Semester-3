# g) Print Current Time:
from datetime import datetime
import time

for i in range(10):
    current_time = datetime.now()
    print("Current time:", current_time)
    time.sleep(10)