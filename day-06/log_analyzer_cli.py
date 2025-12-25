import argparse
import os


class LogAnalyzer:
    def __init__(self, log_file):
        # Store log file path and initialize counters
        self.log_file = log_file
        self.counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "UNKNOWN": 0
        }

    def read_logs(self):
        # Read all lines from the log file
        try:
            with open(self.log_file, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Log file not found: {self.log_file}")
            return []

    def analyze(self, lines, level_filter=None):
        # Analyze each line and count log levels
        for line in lines:
            if "INFO" in line:
                level = "INFO"
            elif "WARNING" in line:
                level = "WARNING"
            elif "ERROR" in line:
                level = "ERROR"
            else:
                level = "UNKNOWN"

            if level_filter:
                if level == level_filter:
                    self.counts[level] += 1
            else:
                self.counts[level] += 1

        return self.counts


def build_summary(counts):
    # Build summary text for output
    summary = ["Log Analysis Summary:"]
    for level, count in counts.items():
        summary.append(f"{level}: {count}")
    return "\n".join(summary)


def parse_arguments():
    # Handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Simple CLI tool to analyze log files"
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file"
    )
    parser.add_argument(
        "--out",
        help="File to write the summary output"
    )
    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR", "UNKNOWN"],
        help="Filter logs by a specific level"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if not os.path.exists(args.file):
        print(f"File does not exist: {args.file}")
        return

    analyzer = LogAnalyzer(args.file)
    log_lines = analyzer.read_logs()

    if not log_lines:
        print("No logs found to analyze.")
        return

    results = analyzer.analyze(log_lines, args.level)
    summary_text = build_summary(results)

    # Print summary to terminal
    print(summary_text)

    # Write summary to output file if provided
    if args.out:
        try:
            with open(args.out, "w") as output_file:
                output_file.write(summary_text)
            print(f"\nSummary written to {args.out}")
        except OSError:
            print("Failed to write summary to output file.")


if __name__ == "__main__":
    main()
