# ✅ Day 21 – Iterating Like a Pro in Python


print("\n--- List: Print elements divisible by 2 ---")
# Sample Input: 1 2 3 4 5 6
lst_input = input("Enter list elements separated by space: ").split()
lst = [int(x) for x in lst_input]
for num in lst:
    if num % 2 == 0:
        print(num)  # Output: 2 4 6

    

print("\n--- Tuple: Print squares of numbers > 5 ---")
# Sample Input: 3 6 7 2
tpl_input = input("Enter tuple elements separated by space: ").split()
tpl = tuple(int(x) for x in tpl_input)
for num in tpl:
    if num > 5:
        print(num**2)  # Output: 36 49

        

print("\n--- Dictionary: Print keys with values > 10 ---")
# Sample Input: a 5, b 15, c 20
d = {}
num_items = int(input("Enter number of dictionary items: "))
for _ in range(num_items):
    key = input("Enter key: ")
    value = int(input(f"Enter value for {key}: "))
    d[key] = value
for key, value in d.items():
    if value > 10:
        print(key)  # Output: b c

        

print("\n--- Set: Capitalize each name ---")
# Sample Input: alice bob charlie
set_input = input("Enter names separated by space: ").split()
s = set(set_input)
for name in s:
    print(name.capitalize())  # Output: Alice Bob Charlie (order may vary)

print("\n--- List of strings: Print only those starting with a vowel ---")
# Sample Input: apple banana orange umbrella grape
str_list = input("Enter strings separated by space: ").split()
vowels = "aeiouAEIOU"
for word in str_list:
    if word[0] in vowels:
        print(word)  # Output: apple orange umbrella
