import cv2
from pyzbar.pyzbar import decode

# Chemin vers l'image contenant le QR code
image_path = 'qrcode.png'

# Lire l'image
image = cv2.imread(image_path)

# Décoder le QR code
decoded_objects = decode(image)

# Afficher les données décodées
for obj in decoded_objects:
    print('Type:', obj.type)
    print('Data:', obj.data.decode('utf-8'))
