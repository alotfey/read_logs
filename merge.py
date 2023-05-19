import os
import fileinput

def merge_files(directory, output_file):
    # List to store .INFO file paths
    info_files = []

    # Walk through directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # Check if file has .INFO extension
            if filename.endswith('.INFO'):
                # Append full file path to list
                info_files.append(os.path.join(dirpath, filename))

    # Open output file in write mode
    with open(output_file, 'w') as outfile:
        # Use fileinput.input() to read each file line by line
        for line in fileinput.input(info_files):
            # Write each line to the output file
            outfile.write(line)

# Call the function with the directory and output file path
merge_files('/path/to/directory', 'merged.INFO')
