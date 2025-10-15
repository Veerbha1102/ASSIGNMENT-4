# Python Module 5: Files, Exceptions, and Errors - Assignment 4

This repository contains the solutions for Assignment 4 of Module 5: Files, Exceptions, and Errors in Python.

## Task 1: Read a File and Handle Errors (`task1_read_file.py`)

This program attempts to open and read a file named `sample.txt`. It uses a `try...except FileNotFoundError` block to gracefully handle the situation where the file does not exist, providing a user-friendly error message. If the file exists, it prints its contents line by line.

## Task 2: Write and Append Data to a File (`task2_write_append.py`)

This program demonstrates writing and appending data to a single file named `output.txt`:
1.  It prompts the user for initial data and **writes** it to `output.txt` (overwriting previous content).
2.  It then **appends** a predefined line of text to the same file.
3.  Finally, it **reads** the entire content of `output.txt` and displays the final result to the user.
