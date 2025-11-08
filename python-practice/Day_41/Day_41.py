import os
import sys

print("✅ Day 41 – Interacting with the Operating System\n")
print("-"*50 + "\n")

# ------------------------
# OS Module Practice
# ------------------------
# Current Working Directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List Files & Directories
contents = os.listdir(cwd)
print(f"\nFiles and Folders in CWD:\n{contents}")

# Change Directory (Example: go up one level)
os.chdir("..")
new_cwd = os.getcwd()
print(f"\nChanged Directory Up One Level: {new_cwd}")

print("\n" + "-"*50 + "\n")

# ------------------------
# Sys Module Practice
# ------------------------
# Python Version
print(f"Python Version: {sys.version}")

# Platform
print(f"Platform: {sys.platform}")

# Memory size of an object
sample_list = [1, 2, 3, 4, 5]
print(f"Memory Size of sample_list: {sys.getsizeof(sample_list)} bytes")

# Command-line arguments
print(f"Command-line Arguments: {sys.argv}")

print("\n" + "-"*50 + "\n")
