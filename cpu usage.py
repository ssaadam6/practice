import time
import psutil

cpu = 60

while True:
    cpu_usage = psutil.cpu_percent(interval = 1)
    print(f"the cpu percentage is {cpu_usage}")

    if cpu_usage > cpu:
        print(" alert, the cpu usage is high, please check {cpu_usage}")

