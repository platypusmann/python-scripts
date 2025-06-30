# 🐍 Python System Automation Scripts

This repository contains beginner-to-intermediate level Python scripts for automating system tasks. It’s part of my preparation for the Amazon Systems Development Internship 2025.

---

## 📁 Project: File Logger

A script that:
- Scans a given directory
- Filters files by extension (e.g., `.txt`)
- Logs file names and sizes into a `log.txt` file

### Script: `file_logger.py`

---

## 📁 Project: File Organizer

A script that:
- Scans a folder and identifies files by extension
- Sorts them into folders like `Images`, `Text`, `PDFs`, etc.

### Script: `file_organizer.py`

---

## 📁 Project: System Monitor (with Crontab)

A Python script that:
- Collects system resource usage (CPU, Memory, Disk)
- Logs entries with timestamps to `system_log.txt`
- Is scheduled to run every 1 minute using Crontab

### Script: `system_monitor.py`

#### 💡 Features
- Uses the `psutil` library for system metrics
- Logs to a file even when terminal is closed
- Ideal for lightweight server monitoring

---

### 🕒 Crontab Setup

To run the script every minute:

```cron
* * * * * /usr/bin/python3 /home/platypus/amazon_intern/python_scripts/system_monitor.py


## 📌 Author

**Ranveer Bhasin**  
Bachelor of Computer Science (Data Science), Deakin University  
[GitHub](https://github.com/platypusmann) • [LinkedIn](https://www.linkedin.com/in/ranveer-bhasin)
