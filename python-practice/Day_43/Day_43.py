import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
print("✅ Day 43 – Sending OTPs & Bulk Emails in Python\n")
print("-"*50 + "\n")

# -----------------------
# Function to generate OTP
# ------------------------
def generate_otp(length=6):
    chars = string.digits + string.ascii_letters  # Mix of letters and digits
    otp = ''.join(random.choices(chars, k=length))
    return otp
# ------------------------
# Email Setup
# ------------------------
sender_email = "2100031733cser@gmail.com"      # Replace with your Gmail
app_password = "jatn luuw yxew hhrx"         # Use Gmail App Password
recipient_emails = ["jkharan2@gmail.com", "skjabbar2003@gmail.com", "skjabbar1911@gmail.com", "skjabbar1651@gmail.com"]  # Bulk recipients

# ------------------------
# Sending OTPs
# ------------------------
for receiver_email in recipient_emails:
    otp = generate_otp()
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Your OTP Code 🔐"

    # Email body with OTP
    body = f"Hello!\n\nYour One-Time Password (OTP) is: {otp}\nUse this to verify your account."
    message.attach(MIMEText(body, 'plain'))
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        
        # Send the email
        server.send_message(message)
        print(f"OTP sent successfully to {receiver_email}! ✅ (OTP: {otp})")
    except Exception as e:
        print(f"Error sending to {receiver_email}: {e}")
    finally:
        server.quit()
print("\n" + "-"*50 + "\n")
