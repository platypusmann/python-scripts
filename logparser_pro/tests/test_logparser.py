import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser_utils import LogParser

def test_level_filter():
    lp = LogParser("logs/sample.log")
    results = lp.filter_logs(level="ERROR")
    assert all("ERROR" in str(entry) for entry in results)

def test_date_filter():
    lp = LogParser("logs/sample.log")
    results = lp.filter_logs(date="2025-07-16")
    assert len(results) >= 1

def test_keyword_filter():
    lp = LogParser("logs/sample.log")
    results = lp.filter_logs(keyword="User")
    assert any("User" in entry.message for entry in results)
