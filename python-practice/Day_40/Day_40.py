import datetime
import time
import calendar

print("✅ Day 40 – Date and Time in Python\n")
print("-"*40 + "\n")

# ------------------------
# Current Date & Time
# ------------------------
now = datetime.datetime.now()
print(f"Current Date & Time: {now}")

# ------------------------
# Formatting Date
# ------------------------
formatted_date = now.strftime("%B %d, %Y %H:%M:%S")
print(f"Formatted Date & Time: {formatted_date}")

# ------------------------
# Parsing String to Date
# ------------------------
date_str = "2025-10-07 14:30:00"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"Parsed Date from String: {parsed_date}")

print("\n" + "-"*40 + "\n")

# ------------------------
# Time Delay
# ------------------------
print("Wait for 2 seconds...")
time.sleep(2)
print("Done waiting!")

print("\n" + "-"*40 + "\n")

# ------------------------
# Calendar Module
# ------------------------
year = 2025
month = 10
print(f"Calendar for {calendar.month_name[month]} {year}:\n")
print(calendar.month(year, month))

# Check Leap Year
leap_check = calendar.isleap(year)
print(f"Is {year} a leap year? {leap_check}")

print("\n" + "-"*40 + "\n")
