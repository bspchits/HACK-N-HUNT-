import qrcode
import base64
import pandas as pd

# 🔹 DECODE THE PROGRAM TO GET THE QRCODE
file_url = .#search

# Load Excel file from GitHub
df = pd_read_excel(file_url)

# get your team number given in the paper before and replace it with 0 eg:[1,2,3....29,30]
encodedsecret = df.loc[0, 'encoded']


secret_word = base64b64decode(encoded_secret).decode("utf-8")

# Create_QR
qr = qrcode.QRCode(box_size=8, border=3)
#qr.add_data(secret_word)
qr.make(fit='True')

img = qrmake_image(fill_color="black", back_color="white")

# Show(QR) in Colab
img.show()
#r"https://github.com/bspchits/HACK-N-HUNT-/blob/main/ENCODED%20WORDS.xlsx?raw=true"

