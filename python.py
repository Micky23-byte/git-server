import os

# Directory to list
directory = "."

print(f"Listing files in {directory}:")

# Loop through files
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        print(f"File found: {filepath}")

