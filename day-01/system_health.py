import psutil

def check_system_health():
    # Take threshold values from user
    cpu_threshold = int(input("Enter CPU threshold (%): "))
    memory_threshold = int(input("Enter Memory threshold (%): "))
    disk_threshold = int(input("Enter Disk threshold (%): "))

    # Get current system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    print("\n--- System Health Check ---")

    # CPU check
    if cpu_usage > cpu_threshold:
        print(f"CPU Usage HIGH: {cpu_usage}%")
    else:
        print(f"CPU Usage OK: {cpu_usage}%")

    # Memory check
    if memory_usage > memory_threshold:
        print(f"Memory Usage HIGH: {memory_usage}%")
    else:
        print(f"Memory Usage OK: {memory_usage}%")

    # Disk check
    if disk_usage > disk_threshold:
        print(f"Disk Usage HIGH: {disk_usage}%")
    else:
        print(f"Disk Usage OK: {disk_usage}%")


# Run the function
check_system_health()
