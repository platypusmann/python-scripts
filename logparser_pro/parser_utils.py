# parser_utils.py (utility functions and classes)
from datetime import datetime

class LogEntry:
    def __init__(self, raw_line):
        self.raw = raw_line
        self.timestamp, self.level, self.message = self.parse_line(raw_line)

    def parse_line(self, line):
        try:
            parts = line.strip().split(" ", 2)
            timestamp = datetime.strptime(parts[0][1:] + " " + parts[1][:-1], "%Y-%m-%d %H:%M:%S")
            level = parts[2].split()[0]
            message = " ".join(parts[2].split()[1:])
            return timestamp, level, message
        except Exception:
            return None, None, line

    def __str__(self):
        return f"[{self.timestamp}] {self.level} {self.message}"

class LogParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def filter_logs(self, level=None, date=None, keyword=None):
        results = []
        with open(self.filepath, "r") as file:
            for line in file:
                entry = LogEntry(line)
                if level and entry.level != level:
                    continue
                if date and entry.timestamp and entry.timestamp.strftime("%Y-%m-%d") != date:
                    continue
                if keyword and keyword not in entry.message:
                    continue
                results.append(entry)
        return results
