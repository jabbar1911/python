import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("✅ Day 42 – Sending Your First Email with Python\n")
print("-"*50 + "\n")

# ------------------------
# Email Setup
# ------------------------
sender_email = "2100031733cser@gmail.com"      # Replace with your Gmail
receiver_email = "jkharan2@gmail.com"  # Replace with recipient email
app_password = "jatn luuw yxew hhrx"         # Use Gmail App Password, NOT your main password

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Hello from Python!"

# Body of the email
body = "This is my first Python-generated email. 🚀"
message.attach(MIMEText(body, 'plain'))

# ------------------------
# Sending the Email
# ------------------------
try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)
    
    # Send the email
    server.send_message(message)
    print("Email sent successfully! ✅")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()

print("\n" + "-"*50 + "\n")
