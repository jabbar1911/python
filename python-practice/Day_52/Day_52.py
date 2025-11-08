# Day 52: File Handling in Python
import datetime

# Log file path
log_file = "app_log.txt"

def write_log(message):
    """Append a timestamped message to the log file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:  # 'a' mode to append
        file.write(f"{timestamp} - {message}\n")

def read_log():
    """Read and print the log file contents"""
    try:
        with open(log_file, "r") as file:  # 'r' mode to read
            content = file.read()
            print("Log Contents:\n", content)
    except FileNotFoundError:
        print("Log file not found!")

# Example Usage
write_log("Application started")
write_log("Performed a task successfully")
write_log("Application ended")

read_log()
