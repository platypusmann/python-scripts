# logparser.py (CLI entry point)
import argparse
from parser_utils import LogParser
from decorators import log_execution, time_it

@log_execution
@time_it
def main():
    parser = argparse.ArgumentParser(description="LogParser Pro - Filter and analyze log files.")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--level", help="Log level to filter (e.g., INFO, ERROR)")
    parser.add_argument("--date", help="Filter logs by date (YYYY-MM-DD)")
    parser.add_argument("--keyword", help="Filter logs by keyword")
    args = parser.parse_args()

    lp = LogParser(args.file)
    results = lp.filter_logs(level=args.level, date=args.date, keyword=args.keyword)
    for entry in results:
        print(entry)

if __name__ == "__main__":
    main()
