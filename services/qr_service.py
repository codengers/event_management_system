import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import os

QR_CODE_DIR = os.path.join(os.path.dirname(__file__), '..', 'qrcodes')

def generate_qr_code(data, phone):
    if not os.path.exists(QR_CODE_DIR):
        os.makedirs(QR_CODE_DIR)
        
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(file='black', black_color='white')
    qr_path = os.path.join(QR_CODE_DIR, '{}.png'.format(phone))
    img.save(qr_path)
    return qr_path
    
def scan_qr_code(img_path):
    img = cv2.imread(img_path)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        return obj.data.decode('utf-8')
    return None
    
    
