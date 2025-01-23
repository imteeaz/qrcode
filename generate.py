import qrcode

data = "https://ifoxcode.com/"
#data = f"WIFI:T:WEP;S:iFox-Code;P:TfNLFc3d9aV0QvoN2scq;;"

# Création d'une instance de QRCode
qr = qrcode.QRCode(
    version=1,  # version: 1-40, contrôlant la taille du QR code. Utilisez 1 pour la plus petite taille.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # niveau de correction d'erreur
    box_size=10,  # taille de chaque carré du QR code
    border=4,  # largeur de la bordure (en carrés)
)

# Ajouter les données au QR code
qr.add_data(data)
qr.make(fit=True)

# Créer une image à partir du QR code
img = qr.make_image(fill='black', back_color='white')

# Sauvegarder l'image
img.save("qrcode.png")
