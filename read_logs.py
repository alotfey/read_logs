import os
import time
import datetime


def read_new_lines(file_path, last_processed_position):
    new_lines = []
    print("{}".format(new_lines))
    with open(file_path, "r") as file:
        file.seek(last_processed_position)
        new_data = file.read()
        new_processed_position = file.tell()

        if new_data:
            new_lines = new_data.splitlines()
            print("test: {}".format(new_lines))

    return new_lines, new_processed_position


def main(file_path):
    last_processed_position = os.path.getsize(file_path)

    try:
        while True:
            new_lines, new_processed_position = read_new_lines(
                file_path, last_processed_position
            )

            if new_lines:
                for line in new_lines:
                    if "DeviceConnected" in line:
                        print("Device Connected")
                    elif "DeviceDisconnected" in line:
                        print("Device Disconnected")

            last_processed_position = new_processed_position
            time.sleep(1)
    except KeyboardInterrupt:
        pass




# Get the current time
current_time = datetime.datetime.now()

# List all the files in the current directory
files = os.listdir('.')

# Iterate through the files and print the ones that have been updated in the current time
for file in files:
    # Get the file modification time
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    # Check if the file has been modified in the current time
    if modified_time.date() == current_time.date() and modified_time.hour == current_time.hour:
        print(file)


if __name__ == "__main__":
    file_path = "/var/log/system.log"
    main(file_path)
