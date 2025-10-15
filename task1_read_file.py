# task1_read_file.py

# Define the file name
file_name = "sample.txt"

# 1. Opens and reads a text file named sample.txt.
# 3. Handles errors gracefully if the file does not exist.
try:
    with open(file_name, 'r') as file:
        print(f"--- Content of {file_name} ---")
        
        # 2. Prints its content line by line.
        for line in file:
            print(line.strip()) # .strip() removes trailing newline characters
            
        print("--------------------------------")

except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"Error: The file '{file_name}' was not found. Please ensure it exists.")
except Exception as e:
    # Handle any other potential reading errors
    print(f"An unexpected error occurred: {e}")
