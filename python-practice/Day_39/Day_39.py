import random
import string

print("✅ Day 39 – OTP & CAPTCHA Generator\n")
print("-"*40 + "\n")

# ------------------------
# OTP Generator
# ------------------------
def generate_otp(length=4):
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

otp = generate_otp()
print(f"Your 4-digit OTP is: {otp}")
print("\n" + "-"*40 + "\n")

# ------------------------
# CAPTCHA Generator
# ------------------------
def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    captcha_list = random.choices(characters, k=length)
    random.shuffle(captcha_list)
    captcha = ''.join(captcha_list)
    return captcha

captcha = generate_captcha()
print(f"Your CAPTCHA is: {captcha}")
print("\n" + "-"*40 + "\n")
