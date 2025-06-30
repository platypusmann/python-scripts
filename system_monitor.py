import psutil
from datetime import datetime

# Collect system usage data
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create the log entry
log_entry = f"[{timestamp}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n"

# Absolute path to log file
LOG_PATH = "/home/platypus/amazon_intern/python_scripts/system_log.txt"

# Append to log file
with open(LOG_PATH, "a") as log_file:
    log_file.write(log_entry)

print("System usage logged.")
