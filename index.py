import pyqrcode
from pyqrcode import QRCode

# String input for the QR code
image = "https://media.istockphoto.com/photos/python-programming-language-concept-woman-developer-with-her-hand-picture-id1189210101?b=1&k=20&m=1189210101&s=170667a&w=0&h=JPPA3aVkd2O6csgAvZ1jO9QcS-KlaV25xGslHF1Rr7w="

# Generate QR code
qrcd = pyqrcode.create(image)

# Create and save the svg file
qrcd.svg("example.svg", scale=10)