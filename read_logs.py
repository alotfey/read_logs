import os
import time

def read_new_lines(file_path, last_processed_position):
    new_lines = []
    with open(file_path, "r") as file:
        file.seek(last_processed_position)
        new_data = file.read()
        new_processed_position = file.tell()

        if new_data:
            new_lines = new_data.splitlines()

    return new_lines, new_processed_position

def main(file_path):
    last_processed_position = os.path.getsize(file_path)

    try:
        while True:
            new_lines, new_processed_position = read_new_lines(file_path, last_processed_position)

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

if __name__ == "__main__":
    file_path = "/var/log/system.log"
    main(file_path)
