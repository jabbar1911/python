# Day 53: Regular Expressions in Python
import re

# Sample data
text = """
Contact List:
John Doe: john.doe@example.com, +1-555-123-4567
Jane Smith: jane_smith@website.co, +44 7700 900123
Invalid email: test@@example..com, Phone: 123-456
"""

# 1️⃣ Find all email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# 2️⃣ Validate a single email
single_email = "user@example.com"
if re.match(email_pattern, single_email):
    print(f"{single_email} is valid")
else:
    print(f"{single_email} is invalid")

# 3️⃣ Extract all phone numbers
phone_pattern = r'\+?\d[\d\s\-]{7,}\d'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)

# 4️⃣ Replace invalid email placeholders
clean_text = re.sub(r'test@@example..com', 'unknown@example.com', text)
print("\nCleaned Text:\n", clean_text)

# 5️⃣ Split text into lines containing contacts
lines = re.split(r'\n', text)
contact_lines = [line for line in lines if re.search(email_pattern, line)]
print("\nLines with contacts:", contact_lines)
