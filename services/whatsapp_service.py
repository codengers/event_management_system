import pywhatkit as kit
from PIL import Image

def send_whatsapp_qr(phone_number, qr_code_path):

    phone_number = str("+91"+phone_number)
    """
    Send a QR code via WhatsApp using pywhatkit.
    
    :param phone_number: Recipient's WhatsApp number with country code (e.g., '+911234567890').
    :param qr_code_path: Path to the QR code image.
    """
    try:
        # Open and display the QR code (optional)
        #img = Image.open(qr_code_path)
        #img.show()

        # Send image through WhatsApp
        kit.sendwhats_image(
            receiver=phone_number,
            img_path=qr_code_path,
            caption="Here is your QR code for the event. See you there!",
            wait_time=15,
            tab_close=True              
        )
        print("QR Code sent successfully via WhatsApp!")
    except Exception as e:
        print(f"Error sending QR Code via WhatsApp: {e}")
