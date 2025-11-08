import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

print("✅ Sending Email with Attachments to Multiple Recipients\n")
print("-"*50 + "\n")

# ------------------------
# Email Setup
# ------------------------
sender_email = "2100031733cser@gmail.com"
app_password = "jatn luuw yxew hhrx"
recipient_emails = ["jkharan2@gmail.com", "skjabbar2003@gmail.com", "skjabbar1911@gmail.com", "skjabbar1651@gmail.com"]

# ------------------------
# Create Email
# ------------------------
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ", ".join(recipient_emails)
message['Subject'] = "Attached Files 📎"

# Email body
body = "Hello!\n\nPlease find the attached files."
message.attach(MIMEText(body, 'plain'))

# ------------------------
# Attach Files
# ------------------------
files_to_attach = [
    r"C:\Users\DELL\Desktop\email\dummy.pdf",
    r"C:\Users\DELL\Desktop\email\samplepptx.pptx",
    r"C:\Users\DELL\Desktop\email\sample-red-square-grunge-stamp-260nw-1469671010.webp"
]

for file_path in files_to_attach:
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
        message.attach(part)
        print(f"Attached file: {file_path}")
    else:
        print(f"File not found: {file_path}")

# ------------------------
# Send Email
# ------------------------
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient_emails, message.as_string())
    print("\nEmail sent successfully to all recipients! ✅")
except Exception as e:
    print(f"\nError sending email: {e}")
finally:
    server.quit()

print("\n" + "-"*50 + "\n")
