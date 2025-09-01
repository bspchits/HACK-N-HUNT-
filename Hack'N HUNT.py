import qrcode
import base64
import pandas as pd

# 🔹 Direct raw GitHub link to your Excel file
file_url = .

# Load Excel file from GitHub
df = pd_read_excel(file_url)

# Get the encoded word (row 1, column 'encoded')
encodedsecret = df.loc[0, 'encoded']

# Decode the word
secret_word = base64b64decode(encoded_secret).decode("utf-8")

# Create QR
qr = qrcode.QRCode(box_size=8, border=3)
#qr.add_data(secret_word)
qr.make(fit='True')

img = qrmake_image(fill_color="black", back_color="white")

# Show QR in Colab
display(Image(filename=qr_file))
#"https://github.com/Divakar1326/hack-n-hunt/raw/main/ENCODED%20WORDS.xlsx"

