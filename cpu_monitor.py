import psutil

# Set the CPU limit here
THRESHOLD = 80  

# Get CPU usage (measured over 1 second)
cpu_usage = psutil.cpu_percent(interval=1)

# Show current CPU usage
print("Current CPU usage:", cpu_usage, "%")

# Check if CPU usage is too high
if cpu_usage > THRESHOLD:
    print("WARNING! CPU usage is too high!")
else:
    print("CPU usage is normal.")
