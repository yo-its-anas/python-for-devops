import psutil


def get_threshold(prompt):
    """
    Safely get an integer threshold value from the user.
    Handles invalid input gracefully.
    """
    try:
        value = int(input(prompt))
        if value < 0 or value > 100:
            raise ValueError("Threshold must be between 0 and 100.")
        return value
    except ValueError as error:
        print(f"Invalid input: {error}")
        return None


def get_system_metrics():
    """
    Collect current system metrics using psutil.
    Handles unexpected psutil failures.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent
        return cpu_usage, memory_usage, disk_usage
    except Exception as error:
        print(f"Failed to retrieve system metrics: {error}")
        return None


def evaluate_usage(resource_name, current, threshold):
    """
    Compare current usage with threshold and print status.
    """
    if current > threshold:
        print(f"{resource_name} Usage HIGH: {current}%")
    else:
        print(f"{resource_name} Usage OK: {current}%")


def check_system_health():
    """
    Main function to run system health checks.
    """
    print("Enter threshold values (0–100)\n")

    cpu_threshold = get_threshold("CPU threshold (%): ")
    memory_threshold = get_threshold("Memory threshold (%): ")
    disk_threshold = get_threshold("Disk threshold (%): ")

    # Stop execution if any input is invalid
    if None in (cpu_threshold, memory_threshold, disk_threshold):
        print("\nSystem health check aborted due to invalid input.")
        return

    metrics = get_system_metrics()
    if metrics is None:
        print("\nSystem health check aborted due to system error.")
        return

    cpu_usage, memory_usage, disk_usage = metrics

    print("\n--- System Health Check ---")
    evaluate_usage("CPU", cpu_usage, cpu_threshold)
    evaluate_usage("Memory", memory_usage, memory_threshold)
    evaluate_usage("Disk", disk_usage, disk_threshold)


# Run the health check safely
if __name__ == "__main__":
    try:
        check_system_health()
    except KeyboardInterrupt:
        print("\nSystem health check interrupted by user.")
