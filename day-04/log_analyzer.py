def analyze_log(input_file, output_file):

    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Log file is empty.")
                return

            for line in lines:
                line = line.strip()

                if not line:
                    continue

                if "INFO" in line:
                    log_counts["INFO"] += 1
                elif "WARNING" in line:
                    log_counts["WARNING"] += 1
                elif "ERROR" in line:
                    log_counts["ERROR"] += 1

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return

    print("\nLog Summary:")
    for level, count in log_counts.items():
        print(f"{level}: {count}")

    with open(output_file, "w") as file:
        for level, count in log_counts.items():
            file.write(f"{level}: {count}\n")


analyze_log("app.log", "log_summary.txt")
