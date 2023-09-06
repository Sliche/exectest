logfile = open('/tmp/logfile.log', 'r')

import time

# Define the file path you want to read
file_path = "your_file.txt"  # Replace with your file path

while True:
    try:
        # Open the file for reading
        with open("/tmp/logfile.log", 'r') as file:
            # Read and print the content of the file
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

    # Wait for 2 seconds before reading the file again
    time.sleep(3)
