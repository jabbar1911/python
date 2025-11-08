# Day 8: Negative Slicing & Striding in Python 🐍

# Sample Data
text = "Codegnan"
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative Slicing
print("text[-4:]:", text[-4:])         # 'gnan'
print("text[-7:-2]:", text[-7:-2])     # 'odegn'

# Reversing with Negative Stride
print("text[::-1]:", text[::-1])       # 'nangedoC'
print("numbers[::-1]:", numbers[::-1]) # [9, 8, 7, ..., 0]

# Striding with Step
print("numbers[::2]:", numbers[::2])   # [0, 2, 4, 6, 8]
print("numbers[1::2]:", numbers[1::2]) # [1, 3, 5, 7, 9]

# Custom Slicing with Stride
print("text[1:7:2]:", text[1:7:2])     # 'odg'
print("numbers[2:8:3]:", numbers[2:8:3]) # [2, 5]

# Negative Slicing with Step
print("text[-1:-8:-1]:", text[-1:-8:-1]) # 'nangedo'
