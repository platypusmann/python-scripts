import os

#Ask the user for the directory
directory = input("Enter the directory path to scan: ").strip()

#Ask user for the file extension to filter
extension = input("Enter the file extension to filter ").strip()

#Create or overwrite the log file
log_file = open("log.txt", "w")
log_file.write(f"Logging files with '{extension}' extension in directory: {directory}\n\n")

# Check if the directory exists
if os.path.isdir(directory):
    for filename in os.listdir(directory):
        if filename.endswith(extension) and filename != "log.txt":
            filepath = os.path.join(directory, filename)
            size = os.path.getsize(filepath)
            log_file.write(f"{filename} - {size} bytes\n")
else:
    print("Directory does not exist.")

log_file.close()
print(f"Logging complete. Results saved to 'log.txt'")
