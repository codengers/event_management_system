import os
#from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# Twilio Configuration for SMS
# TWILIO_PHONE = 'your_twilio_phone_number'
# TWILIO_SID = 'your_account_sid'
# TWILIO_AUTH_TOKEN = 'your_auth_token'

# SMTP Configuration for Email (Gmail example)
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587
SENDER_EMAIL = 'atikrantupadhye@outlook.com'
SENDER_PASSWORD = 'Arihant@1008'

# def send_sms(phone_number, qr_code_path):
    # """Send QR code via SMS using Twilio."""
    # try:
        # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        # message = client.messages.create(
            # body="Here is your QR code for the event!",
            # from_=TWILIO_PHONE,
            # to=phone_number,
            # media_url=qr_code_path  # Send the QR code image URL
        # )
        # print(f"SMS sent to {phone_number} successfully!")
    # except Exception as e:
        # print(f"Error sending SMS: {e}")

def send_email(email, qr_code_path):
    """Send QR code via email."""
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = email
        msg['Subject'] = "Your Event QR Code"

        # Add email body text
        body = "Attached is your QR code for the event."
        msg.attach(MIMEText(body, 'plain'))

        # Attach the QR code image
        with open(qr_code_path, 'rb') as img:
            image = MIMEImage(img.read())
            image.add_header('Content-Disposition', 'attachment', filename=os.path.basename(qr_code_path))
            msg.attach(image)

        # Set up the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, email, text)
        server.quit()
        print(f"Email sent to {email} successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
