# Day 55: Form Validator using RegEx
import re

def validate_name(name):
    # Only alphabets, 2-30 characters
    pattern = r'^[A-Za-z]{2,30}$'
    return bool(re.match(pattern, name))

def validate_phone(phone):
    # 10-digit Indian numbers starting with 6-9
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, phone))

def validate_email(email):
    # Standard email format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return bool(re.match(pattern, email))

def validate_password(password):
    # At least 1 uppercase, 1 lowercase, 1 digit, 1 special char, 8-16 chars
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
    return bool(re.match(pattern, password))

# Sample inputs
users = [
    {"name": "Alice", "phone": "9876543210", "email": "alice@example.com", "password": "Strong@123"},
    {"name": "Bob123", "phone": "1234567890", "email": "bob.com", "password": "weakpass"}
]

for user in users:
    print(f"\nValidating user: {user['name']}")
    print("Name valid:", validate_name(user['name']))
    print("Phone valid:", validate_phone(user['phone']))
    print("Email valid:", validate_email(user['email']))
    print("Password valid:", validate_password(user['password']))
