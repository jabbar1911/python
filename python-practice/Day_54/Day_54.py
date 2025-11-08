# Day 54: Writing Advanced RegEx Patterns
import re

# 1️⃣ Validate a strong password
# Requirement: At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

passwords = ["Password123!", "weakpass", "Strong@1", "NoSpecialChar1"]

for pwd in passwords:
    if re.match(password_pattern, pwd):
        print(f"{pwd} is a strong password")
    else:
        print(f"{pwd} is weak or invalid")

# 2️⃣ Validate a 10-digit phone number
phone_pattern = r'^\d{10}$'
phones = ["9876543210", "12345", "98765abcde"]

for phone in phones:
    if re.match(phone_pattern, phone):
        print(f"{phone} is a valid phone number")
    else:
        print(f"{phone} is invalid")

# 3️⃣ Extract hashtags from a text
text = "Learning #Python and #Regex is fun! #120DaysOfCode"
hashtags = re.findall(r'#\w+', text)
print("Hashtags found:", hashtags)

# 4️⃣ Match an email pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
emails = ["user@example.com", "invalid@@email.com", "test.user@mail.co"]

valid_emails = [e for e in emails if re.match(email_pattern, e)]
print("Valid emails:", valid_emails)
