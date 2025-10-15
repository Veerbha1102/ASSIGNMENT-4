# task2_write_append.py

file_name = "output.txt"

# 1. Takes user input and writes it to a file named output.txt.
user_input = input("Enter a string to write to the file (e.g., 'Initial data'): ")

try:
    # Open in 'w' (write) mode to create the file or overwrite existing content
    with open(file_name, 'w') as file:
        file.write(user_input + "\n")
    print(f"Successfully wrote initial data to '{file_name}'.")

    # 2. Appends additional data to the same file.
    additional_data = "This is appended on a new line."
    # Open in 'a' (append) mode
    with open(file_name, 'a') as file:
        file.write(additional_data + "\n")
    print(f"Successfully appended additional data to '{file_name}'.")

    # 3. Reads and displays the final content of the file.
    print(f"\n--- Final Content of {file_name} ---")
    with open(file_name, 'r') as file:
        final_content = file.read()
        print(final_content.strip()) # .strip() cleans up extra whitespace/newlines

except Exception as e:
    print(f"An error occurred during file operations: {e}")
